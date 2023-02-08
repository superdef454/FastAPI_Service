import uvicorn

from settings import settungs

print(settungs.server_host)

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host=settungs.server_host,
        port=settungs.server_port,
        reload=True,
    )