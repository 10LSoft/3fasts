from fasts.core.fastcss.css import CSSBuilder

_builder = CSSBuilder()


def css(selector: str, **styles):
    _builder.add(selector, **styles)


def render():
    return _builder.render()


def reset():
    global _builder
    _builder = CSSBuilder()
