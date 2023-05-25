# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import copy
import os

import pytest

from datadog_checks.dev import docker_run, get_here
from datadog_checks.dev.conditions import CheckEndpoints
from datadog_checks.dev.http import MockResponse
from datadog_checks.torchserve import TorchserveCheck

from .common import API_URL, HERE, INSTANCE, MOCKED_INSTANCE, OPENMETRICS_ENDPOINT


@pytest.fixture(scope='session')
def dd_environment():

    with docker_run(
        compose_file=os.path.join(
            get_here(),
            "docker",
            "docker-compose.yaml",
        ),
        conditions=[
            CheckEndpoints(f"{API_URL}/ping"),
            CheckEndpoints(OPENMETRICS_ENDPOINT),
        ],
    ):
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
