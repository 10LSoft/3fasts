import os

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from fasts.core.fastcss.css import load_css
from fasts.core.settings import get_server_config


def start_server():
    """Inicializa o servidor com base no RUN_MODE"""
    config = get_server_config()

    app = FastAPI()

    # Servir arquivos estáticos
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.mount("/media", StaticFiles(directory="media"), name="media")

    # Carregar CSS com FastCSS
    load_css(mode=os.getenv("RUN_MODE", "dev"))

    # Rodar servidor
    uvicorn.run(
        "3fast:app",
        host=config["HOST"],
        port=config["PORT"],
        reload=config["RELOAD"],
        workers=config["WORKERS"],
    )
