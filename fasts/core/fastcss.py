from pathlib import Path


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
