import aiohttp
import requests
from typing import List
import datetime

from models.models import ID as id

from settings import token

class ID:
    headers = {
            "x-auth-token":token,
            "Content-Type": "application/x-www-form-urlencoded" # Хз что это из документации апи
    }

    async def request(session: aiohttp.ClientSession(), url):
        async with session.get(url) as response:
            return await response.text()

    async def get_list_of_records_from_webinar(from_data: datetime.date, to_date: datetime.date = datetime.datetime.now()): # -> List[id]:
        url = f"https://userapi.webinar.ru/v3/records?from={from_data}&to={to_date}"
        request = requests.get(url, headers=ID.headers) # Заменить на асинхронный
        # Здесь бы разобрать ответ и вернуть список объектов ID из модели, но мне не приходит ответ из-за токена ("\"Invalid apiToken\"")
        return request.text

    def Check_conversion_status(conversionID: str):
        url = f"https://userapi.webinar.ru/v3/records/conversions/{conversionID}"
        request = requests.get(url, headers=ID.headers) # Заменить на асинхронный
        return request.text

    def Start_conversion(recordID: List[str]):
        data = {
            "quality": "1080"
        }
        for i in recordID:
            url = f"https://userapi.webinar.ru/v3/records/{i}/conversions"
            request = requests.post(url, headers=ID.headers, data=data) # Заменить на асинхронный
            # Нужно будет разобрать ответ, я хз в каком виде придёт
            yield request.text

    def Delete(recordID: List[str]):
        for i in recordID:
            url = f"https://userapi.webinar.ru/v3/records/{i}"
            request = requests.delete(url, headers=ID.headers)
            yield request.text

    def Download(downloadUrl: str):
        path = "//data/"

    async def test(int):
        t = datetime.datetime.now()
        print(t)
        requestss = []
        url = "http://httpbin.org/uuid"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as respons:
                requestss.append( await respons)
            # request = requests.get(url)
            # requestss.append(request.text)
        print(datetime.datetime.now() - t)
        return requestss