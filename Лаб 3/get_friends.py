from base_client import *
import requests
import json
from datetime import datetime, date, time, timedelta

class GetFriends(BaseClient):
    BASE_URL = 'http://api.vk.com/method/'
    method = 'friends.get'
    http_method = 'POST'

    def __init__(self, uid):
        self.uid = uid

    def get_params(self):
        return 'user_id=' + str(self.uid) + '&fields=bdate'

    def _get_data(self,method, http_method):
        response = requests.get(self.generate_url(self.method) + '?' + self.get_params())
        return self.response_handler(response)


    def response_handler(self, response):
        try:
            friends = json.loads(response.text)['response']
            dates = {}
            i=0
            for d in friends:
                try:
                    bdate = datetime.strptime(d['bdate'], '%d.%m.%Y')
                except:
                    continue
                cur_date = datetime.now()
                time_delta = (cur_date - bdate).days
                years = time_delta //365.25
                if (years not in dates):
                    dates[years] = ''
                dates[years] += '#'
            return dates
        except:
            print('Error')
