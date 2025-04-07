import re


def to_kebab_case(s: str) -> str:
    return re.sub(r'_', '-', s)
