import os
from dotenv import load_dotenv

load_dotenv()

RUN_MODE = os.getenv("RUN_MODE", "dev")

DEFAULTS = {
    "DEV_HOST": "127.0.0.1",
    "DEV_PORT": 8000,
    "DEV_WORKERS": 1,
    "DEV_RELOAD": True,
    "PROD_HOST": "0.0.0.0",
    "PROD_PORT": 8000,
    "PROD_WORKERS": 4,
    "PROD_RELOAD": False,
}


def get_server_config():
    prefix = f"{RUN_MODE.upper()}_"
    return {
        "HOST": os.getenv(f"{prefix}HOST", DEFAULTS[f"{prefix}HOST"]),
        "PORT": int(
            os.getenv(f"{prefix}PORT", DEFAULTS[f"{prefix}PORT"])
        ),
        "WORKERS": int(
            os.getenv(f"{prefix}WORKERS", DEFAULTS[f"{prefix}WORKERS"])
        ),
        "RELOAD": os.getenv(
            f"{prefix}RELOAD", str(DEFAULTS[f"{prefix}RELOAD"])
        ) == "True",
    }
