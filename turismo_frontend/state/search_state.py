import reflex as rx


class SearchState(rx.State):
    destino: str = ""
    fecha: str = ""
    personas: str = ""

    def set_destino(self, value: str):
        self.destino = value

    def set_fecha(self, value: str):
        self.fecha = value

    def set_personas(self, value: str):
        self.personas = value

    def buscar(self):
        return rx.redirect(
            f"/descripcion?destino={self.destino}"
        )

def on_load(self):
    self.destino = self.router.page.full_raw_path.split("destino=")[-1] if "destino=" in self.router.page.full_raw_path else ""