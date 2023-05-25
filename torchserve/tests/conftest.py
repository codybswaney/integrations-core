# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import copy
import os

import pytest

from datadog_checks.dev import get_docker_hostname, get_here, docker_run
from datadog_checks.torchserve import TorchserveCheck

from datadog_checks.dev.conditions import CheckEndpoints

API_PORT = "8080"
OPENMETRICS_PORT = "8082"

API_URL = f"http://{get_docker_hostname()}:{API_PORT}"
OPENMETRICS_ENDPOINT = f"http://{get_docker_hostname()}:{OPENMETRICS_PORT}/metrics"

INSTANCE = {
    "openmetrics_endpoint": OPENMETRICS_ENDPOINT,
}


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
def check(instance):
    return TorchserveCheck('torchserve', {}, [instance])
