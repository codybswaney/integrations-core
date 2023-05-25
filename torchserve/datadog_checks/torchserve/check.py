# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from datadog_checks.base import OpenMetricsBaseCheckV2
from datadog_checks.torchserve.config_models import ConfigMixin
from datadog_checks.torchserve.metrics import METRIC_MAP


class TorchserveCheck(OpenMetricsBaseCheckV2, ConfigMixin):
    __NAMESPACE__ = 'torchserve'
    DEFAULT_METRIC_LIMIT = 0

    def get_default_config(self):
        return {
            "metrics": [METRIC_MAP],
        }
