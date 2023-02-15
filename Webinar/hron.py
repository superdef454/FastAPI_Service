import requests

from settings import settungs

response = requests.post(url=f"http://{settungs.server_host}:{settungs.server_port}/records/check")