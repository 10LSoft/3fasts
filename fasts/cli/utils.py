import shutil
from pathlib import Path


def copy_scaffold(
        template_type: str,
        destination: str,
        context: dict | None = None
):
    """
    Copia o scaffold base de projeto ou app para o destino indicado.

    Args:
        template_type (str): 'project' ou 'app'
        destination (str): Caminho de destino onde os arquivos serão criados
        context (dict): Substituições opcionais no conteúdo dos arquivos (ex:
        {"__APP_NAME__": "blog"})
    """
    base_path = Path(__file__).parent.parent / "scaffold" / template_type
    dest_path = Path(destination).resolve()

    if not base_path.exists():
        raise FileNotFoundError(
            f"Template '{template_type}' não encontrado em {base_path}"
        )

    if dest_path.exists():
        raise FileExistsError(f"O destino '{dest_path}' já existe.")

    shutil.copytree(base_path, dest_path)

    if context:
        for file in dest_path.rglob("*"):
            if file.is_file():
                content = file.read_text()
                for key, value in context.items():
                    content = content.replace(key, value)
                file.write_text(content)

    print(f"✅ Scaffold '{template_type}' copiado para: {dest_path}")
