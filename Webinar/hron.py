import aiohttp
import asyncio

# Скрипт для обращения к серверу по расписанию

from settings import settungs

async def update():
    async with aiohttp.ClientSession(trust_env = True) as session:
        async with session.post(url=f"http://{settungs.server_host}:{settungs.server_port}/records/check") as resp:
            request = resp
            # return request

asyncio.run(update())