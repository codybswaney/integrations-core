# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from datadog_checks.base import AgentCheck


class TorchserveManagementAPICheck(AgentCheck):
    __NAMESPACE__ = 'torchserve'

    def check(self, _):
        pass
