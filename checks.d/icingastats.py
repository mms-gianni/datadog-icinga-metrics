# stdlib
import requests
import json

from checks import AgentCheck

# Docs 
# http://docs.icinga.org/latest/de/cgiparams.html#matrixparamscgis

class Icingastats(AgentCheck):

    FIELDS = [
        'network_outages',
        'percent_host_health',
        'percent_service_health',
        'total_hosts',
        'total_services',
        'hosts_pending',
        'hosts_pending_active',
        'hosts_pending_passive',
        'hosts_pending_disabled',
        'hosts_up',
        'hosts_up_active',
        'hosts_up_passive',
        'hosts_up_disabled',
        'hosts_down',
        'hosts_down_active',
        'hosts_down_passive',
        'hosts_down_disabled',
        'hosts_down_scheduled',
        'hosts_down_active_scheduled',
        'hosts_down_passive_scheduled',
        'hosts_down_disabled_scheduled',
        'hosts_down_acknowledged',
        'hosts_down_active_acknowledged',
        'hosts_down_passive_acknowledged',
        'hosts_down_disabled_acknowledged',
        'hosts_down_unacknowledged',
        'hosts_down_active_unacknowledged',
        'hosts_down_passive_unacknowledged',
        'hosts_down_disabled_unacknowledged',
        'hosts_unreachable',
        'hosts_unreachable_active',
        'hosts_unreachable_passive',
        'hosts_unreachable_disabled',
        'hosts_unreachable_scheduled',
        'hosts_unreachable_active_scheduled',
        'hosts_unreachable_passive_scheduled',
        'hosts_unreachable_disabled_scheduled',
        'hosts_unreachable_acknowledged',
        'hosts_unreachable_active_acknowledged',
        'hosts_unreachable_passive_acknowledged',
        'hosts_unreachable_disabled_acknowledged',
        'hosts_unreachable_unacknowledged',
        'hosts_unreachable_active_unacknowledged',
        'hosts_unreachable_passive_unacknowledged',
        'hosts_unreachable_disabled_unacknowledged',
        'services_pending',
        'services_pending_host_down',
        'services_pending_active',
        'services_pending_active_host_down',
        'services_pending_passive',
        'services_pending_passive_host_down',
        'services_pending_disabled',
        'services_pending_disabled_host_down',
        'services_ok',
        'services_ok_host_down',
        'services_ok_active',
        'services_ok_active_host_down',
        'services_ok_passive',
        'services_ok_passive_host_down',
        'services_ok_disabled',
        'services_ok_disabled_host_down',
        'services_warning',
        'services_warning_host_down',
        'services_warning_active',
        'services_warning_active_host_down',
        'services_warning_passive',
        'services_warning_passive_host_down',
        'services_warning_disabled',
        'services_warning_disabled_host_down',
        'services_warning_scheduled',
        'services_warning_scheduled_host_down',
        'services_warning_active_scheduled',
        'services_warning_active_scheduled_host_down',
        'services_warning_passive_scheduled',
        'services_warning_passive_scheduled_host_down',
        'services_warning_disabled_scheduled',
        'services_warning_disabled_scheduled_host_down',
        'services_warning_acknowledged',
        'services_warning_acknowledged_host_down',
        'services_warning_active_acknowledged',
        'services_warning_active_acknowledged_host_down',
        'services_warning_passive_acknowledged',
        'services_warning_passive_acknowledged_host_down',
        'services_warning_disabled_acknowledged',
        'services_warning_disabled_acknowledged_host_down',
        'services_warning_unacknowledged',
        'services_warning_unacknowledged_host_down',
        'services_warning_active_unacknowledged',
        'services_warning_active_unacknowledged_host_down',
        'services_warning_passive_unacknowledged',
        'services_warning_passive_unacknowledged_host_down',
        'services_warning_disabled_unacknowledged',
        'services_warning_disabled_unacknowledged_host_down',
        'services_critical',
        'services_critical_host_down',
        'services_critical_active',
        'services_critical_active_host_down',
        'services_critical_passive',
        'services_critical_passive_host_down',
        'services_critical_disabled',
        'services_critical_disabled_host_down',
        'services_critical_scheduled',
        'services_critical_scheduled_host_down',
        'services_critical_active_scheduled',
        'services_critical_active_scheduled_host_down',
        'services_critical_passive_scheduled',
        'services_critical_passive_scheduled_host_down',
        'services_critical_disabled_scheduled',
        'services_critical_disabled_scheduled_host_down',
        'services_critical_acknowledged',
        'services_critical_acknowledged_host_down',
        'services_critical_active_acknowledged',
        'services_critical_active_acknowledged_host_down',
        'services_critical_passive_acknowledged',
        'services_critical_passive_acknowledged_host_down',
        'services_critical_disabled_acknowledged',
        'services_critical_disabled_acknowledged_host_down',
        'services_critical_unacknowledged',
        'services_critical_unacknowledged_host_down',
        'services_critical_active_unacknowledged',
        'services_critical_active_unacknowledged_host_down',
        'services_critical_passive_unacknowledged',
        'services_critical_passive_unacknowledged_host_down',
        'services_critical_disabled_unacknowledged',
        'services_critical_disabled_unacknowledged_host_down',
        'services_unknown',
        'services_unknown_host_down',
        'services_unknown_active',
        'services_unknown_active_host_down',
        'services_unknown_passive',
        'services_unknown_passive_host_down',
        'services_unknown_disabled',
        'services_unknown_disabled_host_down',
        'services_unknown_scheduled',
        'services_unknown_scheduled_host_down',
        'services_unknown_active_scheduled',
        'services_unknown_active_scheduled_host_down',
        'services_unknown_passive_scheduled',
        'services_unknown_passive_scheduled_host_down',
        'services_unknown_disabled_scheduled',
        'services_unknown_disabled_scheduled_host_down',
        'services_unknown_acknowledged',
        'services_unknown_acknowledged_host_down',
        'services_unknown_active_acknowledged',
        'services_unknown_active_acknowledged_host_down',
        'services_unknown_passive_acknowledged',
        'services_unknown_passive_acknowledged_host_down',
        'services_unknown_disabled_acknowledged',
        'services_unknown_disabled_acknowledged_host_down',
        'services_unknown_unacknowledged',
        'services_unknown_unacknowledged_host_down',
        'services_unknown_active_unacknowledged',
        'services_unknown_active_unacknowledged_host_down',
        'services_unknown_passive_unacknowledged',
        'services_unknown_passive_unacknowledged_host_down',
        'services_unknown_disabled_unacknowledged',
        'services_unknown_disabled_unacknowledged_host_down',
        'flap_disabled_services',
        'flapping_services',
        'flap_disabled_hosts',
        'flapping_hosts',
        'notification_disabled_services',
        'notification_disabled_hosts',
        'event_handler_disabled_services',
        'event_handler_disabled_hosts',
        'min_service_check_execution_time',
        'max_service_check_execution_time',
        'average_service_check_execution_time',
        'min_service_check_latency',
        'max_service_check_latency',
        'average_service_check_latency',
        'min_host_check_execution_time',
        'max_host_check_execution_time',
        'average_host_check_execution_time',
        'min_host_check_latency',
        'max_host_check_latency',
        'average_host_check_latency',
        'total_active_host_checks',
        'total_passive_host_checks',
        'total_disabled_host_checks',
        'total_active_host_checks_with_passive_disabled',
        'total_active_service_checks',
        'total_passive_service_checks',
        'total_disabled_service_checks',
        'total_active_service_checks_with_passive_disabled'
    ]


    requests.packages.urllib3.disable_warnings()

    def __init__(self, name, init_config, agentConfig, instances=None):

        AgentCheck.__init__(self, name, init_config, agentConfig, instances=instances)

    def check(self, instance):

        if instance.get("site", None) is None:
            raise Exception("Check is not configured: add site")
        site = instance.get('site')
        if instance.get("cgiurl", None) is None:
            raise Exception("Check is not configured: add cgiurl")
        cgiurl = instance.get('cgiurl')

        username = instance.get('username', None)
        password = instance.get('password', None)
        if username is not None and password is not None:
            auth = (username, password)
        else:
            auth = None

        basetags = instance.get('tags', [])

        dataHeaders = {'Content-Type': 'application/json;charset=UTF-8'}

        dataRequest = requests.get(cgiurl+'/tac.cgi?jsonoutput', auth=auth, headers=dataHeaders, verify=False)
        self.log.debug(dataRequest.text)

        try:
            res = json.loads(dataRequest.text)
        except ValueError:
            self.log.error("Failed to load json data")
            return

        try:
            for field in self.FIELDS:
                data = str(res['tac']['tac_overview'][field])
                self.log.debug(data)
                tags = ['site:%s' % site] + basetags
                self.gauge('icinga.stats.'+field, data, tags=tags)
        except ValueError:
            self.log.error("Failed to save data")
            return