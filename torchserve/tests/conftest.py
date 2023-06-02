# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import copy
import os

import pytest
import requests

from datadog_checks.dev import docker_run, get_here
from datadog_checks.dev.conditions import CheckEndpoints, WaitFor
from datadog_checks.dev.http import MockResponse
from datadog_checks.torchserve import TorchserveCheck

from .common import INFERENCE_API_URL, HERE, INSTANCE, MOCKED_INSTANCE, OPENMETRICS_ENDPOINT


def run_prediction(model):
    try:
        response = requests.post(f"{INFERENCE_API_URL}/predictions/{model}", data='{"input": 2.0}', headers={'Content-Type': 'application/json'})
        response.raise_for_status()
    except requests.HTTPError:
        return False
    else:
        return response.status_code == 200


@pytest.fixture(scope='session')
def dd_environment():
    conditions = [
        CheckEndpoints(f"{INFERENCE_API_URL}/ping"),
        CheckEndpoints(OPENMETRICS_ENDPOINT),
        WaitFor(run_prediction, args=("linear_regression_1_1",)),
        WaitFor(run_prediction, args=("linear_regression_1_2",)),
        WaitFor(run_prediction, args=("linear_regression_2_2",)),
        WaitFor(run_prediction, args=("linear_regression_2_3",)),
        WaitFor(run_prediction, args=("linear_regression_3_2",)),
    ]

    with docker_run(
            compose_file=os.path.join(
                get_here(),
                "docker",
                "docker-compose.yaml",
            ),
            conditions=conditions,
    ):
        for _ in range(10):
            for model in ("linear_regression_1_1", "linear_regression_1_2", "linear_regression_2_2", "linear_regression_2_3", "linear_regression_3_2"):
                run_prediction(model)

        yield copy.deepcopy(INSTANCE)


@pytest.fixture
def instance():
    return copy.deepcopy(INSTANCE)


@pytest.fixture
def mocked_instance():
    return copy.deepcopy(MOCKED_INSTANCE)


@pytest.fixture
def check():
    return lambda instance: TorchserveCheck('torchserve', {}, [instance])


def mock_http_responses(url, **_params):
    mapping = {
        'http://torchserve:8082/metrics': 'openmetrics/metrics.txt',
        'http://torchserve:8081/ping': 'api/healthy.txt',
    }

    metrics_file = mapping.get(url)

    if not metrics_file:
        pytest.fail(f"url `{url}` not registered")

    with open(os.path.join(HERE, 'fixtures', metrics_file)) as f:
        return MockResponse(content=f.read())
