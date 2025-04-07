import os
from typing import Any

from fastapi.responses import HTMLResponse

try:
    from htmlmin import minify  # type: ignore[import]
    HTML_MINIFY_AVAILABLE = True
except ImportError:
    HTML_MINIFY_AVAILABLE = False


def render_component(component: Any) -> HTMLResponse:
    """
    Converte um componente FastHTML em uma resposta HTML do FastAPI.

    Isso mantém a flexibilidade de adicionar headers, status codes ou
    wrappers personalizados no futuro.
    """
    html = str(component)
    run_mode = os.getenv("RUN_MODE", "dev")

    if HTML_MINIFY_AVAILABLE and run_mode == "prod":
        html = minify(html, remove_empty_space=True)

    return HTMLResponse(content=html, status_code=200)
