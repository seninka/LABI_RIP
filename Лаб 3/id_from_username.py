from base_client import *
import requests
import json

class IdFromUsername(BaseClient):
    BASE_URL = 'http://api.vk.com/method/'
    method = 'users.get'
    http_method = 'POST'

    def __init__(self, username):
        self.username = username

    def get_params(self):
        return 'user_ids=' + self.username

    def _get_data(self,method, http_method):
        response = requests.get(self.generate_url(self.method) + '?' + self.get_params())
        return self.response_handler(response)

    def response_handler(self, response):
        try:
            string = json.loads(response.text)
            return string['response'][0]['uid']
        except:
            print('Error')
