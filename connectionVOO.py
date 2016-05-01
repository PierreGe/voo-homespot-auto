# -*- coding: utf8 -*-

import requests
import config

class ConnectionVOO(object):
    """docstring for ConnectionVOO"""
    def __init__(self):
        self._payload = {
            "partner": "/?lng=fr&target=&lastAuthResult=&username=&partner=voo&from=&fromURI=&authURI=",
            "username": config.USERNAME,
            "password": config.PASSWORD,
            "rememberme": "rememberme",
            "accept":"accept",
            "target":""
        }
        
    def sendRequest(self):
        """ """
        r = requests.post("https://wifree.voo.be/authenticate.html", data=self._payload)
        return r

    def isLive(self):
        """ """
        try:
            r = requests.get("http://captive.apple.com/", timeout=2)
            return ("Success" in r.text)
        except:
            return False
