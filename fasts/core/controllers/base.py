from typing import Type
# from fasts.core.fastcss import load_css


class BaseController:
    def __init__(self, component: Type):
        """
        component: classe Python (componente FastHTML) que representa a
        resposta do controlador.
        """
        self.component = component

    def render(self, **kwargs):
        """
        Retorna uma instância renderizável do componente.
        """
        return self.component(**kwargs)
