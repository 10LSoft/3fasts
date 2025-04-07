from functools import wraps


def requires_permission(permission_name: str):
    def decorator(func):
        setattr(func, "_required_permission", permission_name)

        @wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)

        return wrapper

    return decorator
