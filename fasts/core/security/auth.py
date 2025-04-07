from fastapi import Request


class User:
    def __init__(self, username: str, permissions: list[str]):
        self.username = username
        self.permissions = permissions


async def get_user_from_token(request: Request) -> User | None:
    """
    Aqui o ideal seria usar as permissões de usuário dentro do token, o que
    poderia ser usado para comparar com as permissões do controlador.

    Posteriormente este cara pode ser integrado com OAuth2, sessão ou outro
    modo de autenticação, mas por hora, o objetivo é apenas obter as permissões
    a partir do token do usuário que está na requisição.
    """
    token = request.headers.get("Authorization")

    if token == "Bearer admin":
        return User("admin", ["admin_access", "view_dashboard"])
    elif token == "Bearer user":
        return User("user", ["view_dashboard"])
    else:
        return None
