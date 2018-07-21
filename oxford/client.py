import requests
import logging
import json
from config import config
from oxford import filter


class OxfordHTTPClient(object):

    def __init__(self, basic_url="https://od-api.oxforddictionaries.com/api/v1", auto_complete_url="https://en.oxforddictionaries.com/search?query={}&filter=dictionary"):
        self.basic_url = basic_url
        self.auto_complete_url = auto_complete_url

        self.basic_header = {
            "Accept": "application/json",
            "app_id": config.OXFORD_ID,
            "app_key": config.OXFORD_KEY
        }
        self.auto_complete_headers = {
            "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
        }

    def send_request(self, url, headers):
        try:
            r_obj = requests.get(url, headers=headers)
            logging.info("OxfordHTTPClient response" + r_obj.text)
            if r_obj.status_code == 200:
                return True, r_obj.text
            else:
                logging.error("OxfordHTTPClient send request" + str(r_obj.text))
                return False, ""
        except Exception as e:
            logging.error("OxfordHTTPClient send request" + str(e))

    def get_word_entries(self, word):
        r_url = "{}/entries/en/{}".format(self.basic_url, word)
        status, r_data = self.send_request(r_url, self.basic_header)
        if status == False:
            return None
        return filter.filter_word_sense(r_data)
