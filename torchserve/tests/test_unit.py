# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest

from datadog_checks.base import AgentCheck  # noqa: F401
from datadog_checks.base.stubs.aggregator import AggregatorStub  # noqa: F401
from datadog_checks.dev.utils import get_metadata_metrics

from .common import METRICS
from .conftest import mock_http_responses

pytestmark = pytest.mark.unit


def test_check(dd_run_check, aggregator, check, mocked_instance, mocker):
    mocker.patch('requests.get', wraps=mock_http_responses)
    dd_run_check(check(mocked_instance))

    for expected_metric in METRICS:
        aggregator.assert_metric(
            f"torchserve.{expected_metric}",
            tags=['Hostname:88665a372f4b.ant.amazon.com', 'Level:Host', 'endpoint:http://torchserve:8082/metrics'],
        )

    aggregator.assert_all_metrics_covered()
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())

    aggregator.assert_service_check(
        "torchserve.openmetrics.health",
        status=AgentCheck.OK,
    )
