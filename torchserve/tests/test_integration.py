# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest

from datadog_checks.base import AgentCheck  # noqa: F401
from datadog_checks.base.stubs.aggregator import AggregatorStub  # noqa: F401
from datadog_checks.dev.utils import get_metadata_metrics

from .common import METRICS, OPENMETRICS_ENDPOINT

pytestmark = [pytest.mark.integration, pytest.mark.usefixtures("dd_environment")]


def test_check(dd_run_check, aggregator, check, instance):
    dd_run_check(check(instance))

    for expected_metric in METRICS:
        aggregator.assert_metric(f"torchserve.{expected_metric}")
        aggregator.assert_metric_has_tag(f"torchserve.{expected_metric}", f'endpoint:{OPENMETRICS_ENDPOINT}')

    aggregator.assert_all_metrics_covered()
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())

    aggregator.assert_service_check(
        "torchserve.openmetrics.health",
        status=AgentCheck.OK,
    )
