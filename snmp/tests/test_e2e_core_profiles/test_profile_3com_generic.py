# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
import pytest

from .. import common
from ..test_e2e_core_metadata import assert_device_metadata

pytestmark = [pytest.mark.e2e, common.py3_plus_only, common.snmp_integration_only]


def create_profile_test_config(profile_name):
    config = common.generate_container_instance_config([])
    config['init_config']['loader'] = 'core'
    instance = config['instances'][0]
    instance.update({'community_string': profile_name})
    return config


def get_device_ip_from_config(config):
    return config['instances'][0]['ip_address']


def test_e2e_profile_3com_generic(dd_agent_check):
    config = create_profile_test_config('3com-generic')
    aggregator = common.dd_agent_check_wrapper(dd_agent_check, config, rate=True)

    ip_address = get_device_ip_from_config(config)
    common_tags = [
        'snmp_profile:3com-generic',
        'snmp_host:3com.device.name',
        'device_namespace:default',
        'snmp_device:' + ip_address,
    ]

    # --- TEST METRICS ---
    common.assert_common_metrics(aggregator, tags=common_tags, is_e2e=True, loader='core')
    aggregator.assert_metric('snmp.ifNumber', metric_type=aggregator.GAUGE, tags=common_tags)
    aggregator.assert_all_metrics_covered()

    # --- TEST METADATA ---
    device = {'description': '3Com Device Desc',
              'id': 'default:' + ip_address,
              'id_tags': ['device_namespace:default', 'snmp_device:' + ip_address],
              'ip_address': '' + ip_address,
              'name': '3com.device.name',
              'profile': '3com-generic',
              'status': 1,
              'sys_object_id': '1.3.6.1.4.1.43.1.99999999',
              'tags': ['device_namespace:default',
                       'snmp_device:' + ip_address,
                       'snmp_host:3com.device.name',
                       'snmp_profile:3com-generic'],
              'vendor': '3com'}
    assert_device_metadata(aggregator, device)
