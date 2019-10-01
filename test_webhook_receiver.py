import requests
import json
import datetime
import urllib3
from requests.auth import HTTPBasicAuth  # for Basic Auth
from config import WEBHOOK_URL, WEBHOOK_USERNAME, WEBHOOK_PASSWORD

from urllib3.exceptions import InsecureRequestWarning  # for insecure https warnings
urllib3.disable_warnings(InsecureRequestWarning)  # disable insecure https warnings

basic_auth = HTTPBasicAuth('admin', 'r3c3iv3r06z')

dnac_param = {"version": "", "instanceId": "84bc5a0d-b211-4c50-81e0-a142da540d45", "eventId": "NETWORK-NON-FABRIC_WIRED-1-200", "namespace": "ASSURANCE", "name": "", "description": "", "type": "NETWORK", "category": "ALERT", "domain": "Connectivity", "subDomain": "Non-Fabric Wired", "severity": 1, "source": "ndp", "timestamp": 1569449708000, "tags": "", "details": {"Type": "Network Device", "Assurance Issue Details": "This network device PDX-3850-CAMPUS is unreachable from controller. The device role is ACCESS", "Assurance Issue Priority": "P1", "Device": "10.93.130.47", "Assurance Issue Name": "Network Device 10.93.130.47 Is Unreachable From Controller", "Assurance Issue Category": "Availability", "Assurance Issue Status": "active"}, "ciscoDnaEventLink": "dna/assurance/issueDetails?issueId=84bc5a0d-b211-4c50-81e0-a142da540d45", "note": "To programmatically get more info see here - https://<ip-address>/dna/platform/app/consumer-portal/developer-toolkit/apis?apiId=8684-39bb-4e89-a6e4", "tntId": "", "context": "", "tenantId": ""}

sdwan_param = {"devices": [{"system-ip": "10.1.0.1"}], "eventname": "system-reboot-issued", "type": "system-reboot-issued", "rulename": "system-reboot-issued", "component": "System", "entry_time": 1569479153138, "statcycletime": 1569479153138, "message": "The device rebooted", "severity": "Medium", "severity_number": 3, "uuid": "31832379-ee8d-4b8f-a1d8-1aaf745649c2", "values": [{"host-name": "DC1-VEDGE1", "site-id": 200, "system-ip": "10.1.0.1", "reboot-reason": "Initiated by user"}], "rule_name_display": "System_Reboot_Issued", "receive_time": 1569479153138, "values_short_display": [{"host-name": "DC1-VEDGE1", "system-ip": "10.1.0.1"}], "acknowledged": False, "cleared_events": ["0519b356-7def-4b4d-babf-9171380e0e82"], "active": False}


def pprint(json_data):
    """
    Pretty print JSON formatted data
    :param json_data:
    :return:
    """
    print(json.dumps(json_data, indent=4, separators=(' , ', ' : ')))

"""

url = 'http://127.0.0.1:5000/webhook'
header = {'content-type': 'application/json'}
response = requests.post(url, auth=basic_auth, data=json.dumps(dnac_param), headers=header, verify=False)
response_json = response.json()
print(response_json)

"""

import requests
import json

basic_auth = HTTPBasicAuth(WEBHOOK_USERNAME, WEBHOOK_PASSWORD)

url = WEBHOOK_URL
header = {'content-type': 'application/json'}
response = requests.post(url, auth=basic_auth, data=json.dumps(sdwan_param), headers=header, verify=False)
response_json = response.json()
print(response_json)
