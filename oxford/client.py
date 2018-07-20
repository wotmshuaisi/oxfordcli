import requests
import logging
import json

class OxfordHTTPClient(object):

    def __init__(self, basic_url="https://od-api.oxforddictionaries.com/api/v1"):
        self.basic_url = basic_url

    def send_request(self, uri, headers):
        r_url = self.basic_url + uri
        try:
            r_obj = requests.get(r_url, headers=headers)
            logging.info("OxfordHTTPClient response" + r_obj.text)
        except Exception as e:
            logging.error("OxfordHTTPClient send request" + str(e))
