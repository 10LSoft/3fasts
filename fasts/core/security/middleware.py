from fastapi import HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware

from fasts.core.security.auth import get_user_from_token


class PermissionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        endpoint = request.scope.get("endpoint")

        if endpoint:
            required_permission = getattr(
                endpoint,
                "_required_permission",
                None
            )

            if required_permission:
                user = await get_user_from_token(request)

                if not user or required_permission not in user.permissions:
                    raise HTTPException(
                        status_code=403,
                        detail="Permission denied."
                    )

        return await call_next(request)
