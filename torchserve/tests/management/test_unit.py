# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest

from datadog_checks.base import AgentCheck  # noqa: F401
from datadog_checks.base.stubs.aggregator import AggregatorStub  # noqa: F401

from ..conftest import mock_http_responses

pytestmark = pytest.mark.unit


def test_check(dd_run_check, aggregator, check, mocked_management_instance, mocker):
    mocker.patch('requests.get', wraps=mock_http_responses)
    dd_run_check(check(mocked_management_instance))

    aggregator.assert_all_metrics_covered()
