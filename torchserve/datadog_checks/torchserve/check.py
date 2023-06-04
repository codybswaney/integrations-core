# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from datadog_checks.base import AgentCheck, ConfigurationError
from datadog_checks.torchserve.inference_api_check import TorchserveInferenceAPICheck
from datadog_checks.torchserve.management_api_check import TorchserveManagementAPICheck
from datadog_checks.torchserve.openmetrics_check import TorchserveOpenMetricsCheck

CONFIGURATION_SECTION = (
    "openmetrics_endpoint",
    "inference_api_url",
    "management_api_url",
)


class TorchserveCheck(AgentCheck):
    def __new__(cls, name, init_config, instances):
        instance = instances[0]

        configured_endpoint = [config for config in CONFIGURATION_SECTION if config in instance]

        if not configured_endpoint:
            raise ConfigurationError('TODO: not enough')

        if len(configured_endpoint) > 1:
            raise ConfigurationError('TODO: too many')

        if instance.get('openmetrics_endpoint'):
            return TorchserveOpenMetricsCheck(name, init_config, instances)

        if instance.get('inference_api_url'):
            return TorchserveInferenceAPICheck(name, init_config, instances)

        if instance.get('management_api_url'):
            return TorchserveManagementAPICheck(name, init_config, instances)
