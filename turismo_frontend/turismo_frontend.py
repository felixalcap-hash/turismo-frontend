import reflex as rx
from turismo_frontend.ps.inicio import inicio
from turismo_frontend.ps.descripcion import descripcion
from turismo_frontend.ps.reservas import reservas
from turismo_frontend.state.search_state import SearchState

app = rx.App()
app.add_page(inicio, route="/")
app.add_page(descripcion, route="/descripcion")
app.add_page(reservas, route="/reservas")