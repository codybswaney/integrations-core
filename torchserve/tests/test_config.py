# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest

from datadog_checks.base import AgentCheck, ConfigurationError  # noqa: F401
from datadog_checks.base.stubs.aggregator import AggregatorStub  # noqa: F401

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    'instance, error_message',
    [
        pytest.param({}, "TODO: not enough", id='empty config'),
        pytest.param({"option"}, "TODO: not enough", id='no endpoint configured'),
        pytest.param({"openmetrics_endpoint", "inference_api_url"}, "TODO: too many", id='openmetrics and inference'),
        pytest.param({"openmetrics_endpoint", "management_api_url"}, "TODO: too many", id='openmetrics and management'),
        pytest.param({"inference_api_url", "management_api_url"}, "TODO: too many", id='inference and management'),
    ],
)
def test_invalid_configs(check, instance, error_message):
    with pytest.raises(ConfigurationError, match=error_message):
        check(instance)
