# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import pytest

from datadog_checks.dev.utils import get_metadata_metrics
from datadog_checks.strimzi import StrimziCheck

from .common import (
    CLUSTER_OPERATOR_METRICS,
    MOCKED_CLUSTER_OPERATOR_INSTANCE,
    MOCKED_CLUSTER_OPERATOR_TAGS,
    MOCKED_TOPIC_OPERATOR_INSTANCE,
    MOCKED_TOPIC_OPERATOR_TAGS,
    MOCKED_USER_OPERATOR_INSTANCE,
    MOCKED_USER_OPERATOR_TAGS,
    TOPIC_OPERATOR_METRICS,
    USER_OPERATOR_METRICS,
)
from .conftest import mock_http_responses

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    'namespace, instance, metrics, tags',
    [
        ('cluster_operator', MOCKED_CLUSTER_OPERATOR_INSTANCE, CLUSTER_OPERATOR_METRICS, MOCKED_CLUSTER_OPERATOR_TAGS),
        ('topic_operator', MOCKED_TOPIC_OPERATOR_INSTANCE, TOPIC_OPERATOR_METRICS, MOCKED_TOPIC_OPERATOR_TAGS),
        ('user_operator', MOCKED_USER_OPERATOR_INSTANCE, USER_OPERATOR_METRICS, MOCKED_USER_OPERATOR_TAGS),
    ],
)
def test_check_unique_operator(
    dd_run_check,
    aggregator,
    check,
    namespace,
    instance,
    metrics,
    tags,
    mocker,
):
    mocker.patch('requests.get', wraps=mock_http_responses)
    dd_run_check(check(instance))

    for expected_metric in metrics:
        aggregator.assert_metric(
            name=expected_metric["name"],
            value=float(expected_metric["value"]) if "value" in expected_metric else None,
            tags=expected_metric.get("tags", tags),
            count=expected_metric.get("count", 1),
        )

    aggregator.assert_all_metrics_covered()
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())

    aggregator.assert_service_check(
        f"strimzi.{namespace}.openmetrics.health",
        status=StrimziCheck.OK,
        tags=tags,
        count=1,
    )
    assert len(aggregator.service_check_names) == 1


def test_check_all_operators(dd_run_check, aggregator, check, mocker):
    mocker.patch('requests.get', wraps=mock_http_responses)
    dd_run_check(
        check(
            {
                **MOCKED_CLUSTER_OPERATOR_INSTANCE,
                **MOCKED_TOPIC_OPERATOR_INSTANCE,
                **MOCKED_USER_OPERATOR_INSTANCE,
            }
        )
    )
    for endpoint_metrics in (CLUSTER_OPERATOR_METRICS, TOPIC_OPERATOR_METRICS, USER_OPERATOR_METRICS):
        for expected_metric in endpoint_metrics:
            aggregator.assert_metric(
                name=expected_metric["name"],
                count=expected_metric.get("count", 1),
            )

    aggregator.assert_all_metrics_covered()
    aggregator.assert_metrics_using_metadata(get_metadata_metrics())

    for namespace in ('cluster_operator', 'topic_operator', 'user_operator'):
        aggregator.assert_service_check(
            f"strimzi.{namespace}.openmetrics.health",
            status=StrimziCheck.OK,
            count=1,
        )
    assert len(aggregator.service_check_names) == 3


@pytest.mark.parametrize(
    'instance',
    [
        {},
        {'openmetrics_endpoint': 'http://cluster-operator:8080/metrics'},
    ],
)
def test_instance_without_operator_endpoint(dd_run_check, check, instance):
    with pytest.raises(
        Exception,
        match="Must specify at least one of the following:"
        "`cluster_operator_endpoint`, `topic_operator_endpoint` or `user_operator_endpoint`.",
    ):
        dd_run_check(check(instance))
