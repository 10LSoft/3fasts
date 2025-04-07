import os

RUN_MODE = os.getenv("RUN_MODE", "dev")

DEV_SERVER_HOST = "127.0.0.1"
DEV_SERVER_PORT = 8000
DEV_SERVER_WORKERS = 1
DEV_SERVER_RELOAD = True

PROD_SERVER_HOST = "0.0.0.0"
PROD_SERVER_PORT = 8000
PROD_SERVER_WORKERS = 4
PROD_SERVER_RELOAD = False


def get_server_config():
    prefix = f"{RUN_MODE.upper()}_"

    return {
        key.removeprefix(prefix): value
        for key, value in globals().items()
        if key.startswith(prefix)
    }
