from pathlib import Path

from fasts.utils import to_kebab_case


class CSSBuilder:
    def __init__(self):
        self.rules = []

    def add(self, selector: str, **styles):
        css_rule = {
            "selector": selector,
            "properties": {
                to_kebab_case(k): v for k, v in styles.items()
            }
        }
        self.rules.append(css_rule)

    def render(self) -> str:
        output = ""
        for rule in self.rules:
            props = "\n  ".join(
                f"{k}: {v};" for k, v in rule["properties"].items()
            )
            output += f"{rule['selector']} {{\n  {props}\n}}\n\n"
        return output.strip()


css = CSSBuilder()


def load_css(mode: str = "dev"):
    """
    Carrega os arquivos CSS do diretório static/styles e minifica se
    necessário.
    """
    css_dir = Path("static/styles")
    output_dir = Path("static/build")

    output_dir.mkdir(parents=True, exist_ok=True)

    for css_file in css_dir.glob("*.css"):
        content = css_file.read_text()

        if mode == "prod":
            content = "".join(line.strip() for line in content.splitlines())

        out_path = output_dir / css_file.name
        out_path.write_text(content)

        print(
            f"[FastCSS] {'Minified' if mode == 'prod' else 'Loaded'}: "
            f"{css_file.name}"
        )
