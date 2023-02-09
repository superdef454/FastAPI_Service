import requests
from typing import List
import datetime

from models.models import ID as id

from settings import token

class ID:
    def zapros():
        url = "https://userapi.webinar.ru/v3/records"
        params = {
            "token":token
        }
        request = requests.get(url, params=params)
        return request

    def get_list_of_records(from_data: datetime.date, to_date: datetime.date = datetime.datetime.now().day) -> List[id]:
        pass