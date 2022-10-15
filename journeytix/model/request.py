import random
import sys
sys.path.insert(0, './journeytix/model')
sys.path.insert(0, './journeytix/config')
from requests import get, post
import json
from user_agents import _useragent_list

class Request(object):

    def __init__(self) -> None:
        pass

    def _get_proxy(self):
        """
        """
        try:
            url = "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/json/proxies.json"
            proxies = get(
                    url=url,
                    headers={
                        "User-Agent": self._get_useragent()
                    }
            )
            proxy = random.choice(json.loads(proxies.text)['socks5'])
            return {proxy.split(":")[0] : proxy.split(":")[1]}
        except Exception as e:
            return {"":""}

    def _get_useragent(self):
        """
        """
        return random.choice(_useragent_list)

    def get_req(self, url):
        """
        """
        user_agent = self._get_useragent()
        proxy = self._get_proxy()
        resp = get(
            url=url,
            headers={
                "User-Agent": user_agent
            }
        )
        resp.raise_for_status()
        return resp

    def post_req(self, url, payload):
        """
        """
        user_agent = self._get_useragent()
        resp = post(
            url=url,
            headers={
                "User-Agent": user_agent,
                "Content-Type": "application/json",
                "Accept": "*/*",
                "Connection": "keep-alive"
            },
            json=payload
        )
        resp.raise_for_status()
        return resp 
