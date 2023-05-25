# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from datadog_checks.dev import get_docker_hostname, get_here

HERE = get_here()

API_PORT = "8080"
OPENMETRICS_PORT = "8082"

API_URL = f"http://{get_docker_hostname()}:{API_PORT}"
OPENMETRICS_ENDPOINT = f"http://{get_docker_hostname()}:{OPENMETRICS_PORT}/metrics"

INSTANCE = {
    "openmetrics_endpoint": OPENMETRICS_ENDPOINT,
}

MOCKED_INSTANCE = {
    "openmetrics_endpoint": "http://torchserve:8082/metrics",
}

METRICS = {
    'frontend.requests.2xx.count',
}
