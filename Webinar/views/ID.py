import aiohttp
import asyncio
import requests
from typing import List
import datetime

from models.models import ID as id

from settings import settungs

async def request(session: aiohttp.ClientSession, url, data=None): # Надо проверить дату
    async with session.get(url, data=data) as response:
        return await response.json()

class ID:
    headers = {
            "x-auth-token":settungs.token,
            "Content-Type": "application/x-www-form-urlencoded" # Хз что это из документации апи
    }

    async def get_list_of_records_from_webinar(from_data: datetime.date, to_date: datetime.date = datetime.datetime.now().date()): # -> List[id]:
        url = f"https://userapi.webinar.ru/v3/records?from={from_data}&to={to_date}"
        print(url)
        async with aiohttp.ClientSession(trust_env = True, headers=ID.headers) as session:
            async with session.get(url) as resp:
                data = await resp.json()
        # Здесь бы разобрать ответ и вернуть список объектов ID из модели, но мне не приходит ответ из-за токена ("Invalid apiToken")
        return data

    async def Check_conversion_status(conversionID: str):
        url = f"https://userapi.webinar.ru/v3/records/conversions/{conversionID}"
        async with aiohttp.ClientSession(trust_env = True, headers=ID.headers) as session:
            async with session.get(url) as resp:
                data = await resp.json()
        return data

    async def Start_conversion(recordID: List[str]):
        data = { # Надо проверить
            "quality": "1080"
        }
        conversIDs = []
        async with aiohttp.ClientSession(trust_env = True, headers=ID.headers) as session:
            tasks = []
            for i in recordID:
                url = f"https://userapi.webinar.ru/v3/records/{i}/conversions"
                tasks.append(asyncio.ensure_future(request(session, url, data=data)))
            answers_to_tasks = await asyncio.gather(*tasks)
            for i in answers_to_tasks:
                conversIDs.append(i)
            # Нужно будет разобрать ответ, я хз в каком виде придёт
        return conversIDs

    async def Delete_records_from_webinar(recordID: List[str]):
        list_response = []
        async with aiohttp.ClientSession(trust_env = True, headers=ID.headers) as session:
            tasks = []
            for i in recordID:
                url = f"https://userapi.webinar.ru/v3/records/{i}"
                tasks.append(asyncio.ensure_future(request(session, url)))
            answers_to_tasks = await asyncio.gather(*tasks)
            for i in answers_to_tasks:
                list_response.append(i)
                # Добавить проверку на выполнение
            return list_response

    def Download(downloadUrl: str):
        path = "//data/"