# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# from datadog_checks.dev.utils import get_metadata_metrics
from datadog_checks.silk import SilkCheck


def test_check(aggregator, instance):
    check = SilkCheck('silk', {}, [instance])
    check.check(instance)

    for metric in []:
        aggregator.assert_metric(metric)

    aggregator.assert_all_metrics_covered()
    # aggregator.assert_metrics_using_metadata(get_metadata_metrics())


# def test_emits_critical_service_check_when_service_is_down(dd_run_check, aggregator, instance):
#     # type: (Callable[[AgentCheck, bool], None], AggregatorStub, Dict[str, Any]) -> None
#     check = SilkCheck('silk', {}, [instance])
#     dd_run_check(check)
#     aggregator.assert_service_check('silk.can_connect', SilkCheck.CRITICAL)
