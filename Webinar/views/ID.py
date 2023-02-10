import requests
from typing import List
import datetime

from models.models import ID as id

from settings import token

class ID:
    def get_list_of_records_from_webinar(from_data: datetime.date, to_date: datetime.date = datetime.datetime.now()): # -> List[id]:
        url = f"https://userapi.webinar.ru/v3/records?from={from_data}&to={to_date}"
        headers = {
            "x-auth-token":token,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        request = requests.get(url, headers=headers)
        # Здесь бы разобрать ответ и вернуть список объектов ID из модели, но мне не приходит ответ из-за токена ("\"Invalid apiToken\"")
        return request.text

    def Check_conversion_status(conversionID: str):
        url = f"https://userapi.webinar.ru/v3/records/conversions/{conversionID}"
        headers = {
            "x-auth-token":token,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        request = requests.get(url, headers=headers)
        return request.text

    def Start_conversion(recordID: List[str]):
        headers = {
            "x-auth-token":token,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "quality": "1080"
        }
        IDs = []
        for i in recordID:
            url = f"https://userapi.webinar.ru/v3/records/{i}/conversions"
            request = requests.post(url, headers=headers, data=data)
            # Нужно будет разобрать ответ, я хз в каком виде придёт
            add_id = request.text
            IDs.append(add_id)
            # Добавить id конвертации в бд
        return IDs

    def Delete():
        pass

    def Download():
        pass