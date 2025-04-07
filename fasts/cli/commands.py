import typer

from fasts.cli.utils import copy_scaffold
from fasts.core.server import start_server

app = typer.Typer()


@app.command()
def runserver():
    """Inicia o servidor 3fast."""
    start_server()


@app.command()
def generate(type: str, name: str):
    """
    Gera um novo projeto ou app baseado em scaffold.

    Observação:
    Nos arquivos que estão sendo copiados no scaffold, você pode usar qualquer
    trecho que queira personalizar de acordo com o nome do app ou projeto. Por
    exemplo, se você quiser que o nome do controller em um app seja
    BlogController, basta passar isto na variável name.
    """
    if type not in {"project", "app"}:
        print("Tipo inválido. Use 'project' ou 'app'.")
        return

    destination = name if type == "project" else f"apps/{name.lower()}"
    context = {"__APP_NAME__": name} if type == "app" else {}

    copy_scaffold(template_type=type, destination=destination, context=context)
