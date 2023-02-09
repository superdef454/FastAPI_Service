import uvicorn

from settings import settungs

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host=settungs.server_host,
        port=settungs.server_port,
        reload=True,
    )