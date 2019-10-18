import re
import requests
import system_config_

requests.packages.urllib3.disable_warnings()
requests_with_session = requests.Session()


def network(url):
    requests.adapters.DEFAULT_RETRIES = 5
    response = requests_with_session.get(url=url, headers=system_config_.browser_config, timeout=9,verify=False)
    # print(response.apparent_encoding)
    return response.text



