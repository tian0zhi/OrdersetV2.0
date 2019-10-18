import re
import requests
import system_config

requests.packages.urllib3.disable_warnings()
requests_with_session = requests.Session()


def obtain_js(html):
    js = '<script src="(.*?)"'
    href = re.compile(js, re.S).findall(html)
    return href


def network(url):
    requests.adapters.DEFAULT_RETRIES = 5
    response = requests_with_session.get(url=url, headers=system_config.browser_config, timeout=9,verify=False)
    return response.text


def into_index(url):
    response = network(url)
    return response


def booking(url):
    response = network(url)
    return response

