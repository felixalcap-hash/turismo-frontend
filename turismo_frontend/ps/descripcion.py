import reflex as rx
from turismo_frontend.componentes.navbar import navbar
from turismo_frontend.componentes.footer import footer
from turismo_frontend.state.search_state import SearchState


OCEAN  = "#0A2342"
SKY    = "#1A6B8A"
SUN    = "#F4A01C"
WHITE  = "#FFFFFF"
MUTED  = "#5C6E7E"
LIGHT  = "#F4F8FB"
BORDER = "#DDE6EE"


# ── Helpers ───────────────────────────────────────────────────────────────────

def label_strip(text: str) -> rx.Component:
    return rx.hstack(
        rx.box(width="3px", height="14px",
               background=SUN, border_radius="2px"),
        rx.text(
            text,
            font_size="0.68rem", font_weight="700",
            letter_spacing="0.18em", text_transform="uppercase",
            color=SKY, font_family="'DM Sans', sans-serif",
        ),
        align="center", spacing="2",
    )


def info_badge(icon: str, label: str, valor: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.icon(icon, size=14, color=SKY),
            width="34px", height="34px",
            border_radius="9px",
            background="#E8F3F8",
            display="flex",
            align_items="center",
            justify_content="center",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.text(label,
                    font_size="0.62rem", font_weight="700",
                    letter_spacing="0.1em", text_transform="uppercase",
                    color=MUTED),
            rx.text(valor,
                    font_size="0.88rem", font_weight="600",
                    color=OCEAN, line_height="1"),
            spacing="0", align="start",
        ),
        align="center", spacing="3",
    )


def itinerario_item(hora: str, actividad: str, last: bool = False) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.box(
                rx.text(hora[:5],
                        font_size="0.6rem", font_weight="700",
                        color=WHITE, text_align="center",
                        line_height="1", white_space="nowrap"),
                background=f"linear-gradient(135deg, {SKY}, {OCEAN})",
                border_radius="6px",
                padding="5px 8px",
                flex_shrink="0",
            ),
            rx.cond(
                ~last,
                rx.box(width="2px", height="26px",
                       background="linear-gradient(to bottom, #C9D8E4, transparent)",
                       margin_x="auto"),
                rx.box(),
            ),
            align="center", spacing="0",
        ),
        rx.text(actividad,
                font_size="0.84rem", color=MUTED,
                line_height="1.55", padding_bottom="2px",
                font_family="'DM Sans', sans-serif"),
        align="start", spacing="3",
    )


def dot_separator() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.box(flex="1", height="1px", background=BORDER),
            rx.box(width="8px", height="8px", border_radius="50%",
                   background=SUN, flex_shrink="0"),
            rx.box(flex="1", height="1px", background=BORDER),
            align="center", gap="14px", width="100%",
        ),
        width="100%", padding_y="4px",
    )


# ── Main card ─────────────────────────────────────────────────────────────────

def lugar_descripcion(
    imagen: str,
    titulo: str,
    descripcion: str,
    duracion: str,
    transporte: str,
    incluye: str,
    precio: str,
    itinerario: list[tuple[str, str]],
    reverse: bool = False,
) -> rx.Component:

    img_col = rx.box(
        rx.image(src=imagen, width="100%", height="100%", object_fit="cover"),
        rx.box(
            rx.vstack(
                rx.text("desde",
                        font_size="0.65rem", font_weight="600",
                        letter_spacing="0.12em", text_transform="uppercase",
                        color="rgba(255,255,255,0.7)"),
                rx.text(precio,
                        font_family="'Cormorant Garamond', serif",
                        font_size="1.7rem", font_weight="700",
                        color=WHITE, line_height="1"),
                spacing="0", align="start",
            ),
            position="absolute", bottom="0", left="0", right="0",
            background="linear-gradient(to top, rgba(10,35,66,.88) 0%, transparent 100%)",
            padding="40px 24px 20px",
        ),
        position="relative",
        border_radius="20px",
        overflow="hidden",
        height="480px",
        min_width="280px",
        flex="1",
        box_shadow="0 16px 48px rgba(10,35,66,0.16)",
    )

    info_col = rx.vstack(
        rx.vstack(
            label_strip("Destino destacado"),
            rx.heading(
                titulo,
                font_family="'Cormorant Garamond', serif",
                font_size="2.5rem",
                font_weight="700",
                color=OCEAN,
                line_height="1.05",
                as_="h2",
            ),
            rx.text(
                descripcion,
                font_size="0.94rem", color=MUTED,
                line_height="1.78",
                font_family="'DM Sans', sans-serif",
            ),
            spacing="3", align="start",
        ),
        rx.box(
            rx.grid(
                info_badge("clock",    "Duración",    duracion),
                info_badge("bus",      "Transporte",  transporte),
                info_badge("utensils", "Incluye",     incluye),
                columns="2",
                spacing="4",
                width="100%",
            ),
            width="100%",
            padding="20px",
            border_radius="14px",
            border=f"1px solid {BORDER}",
            background=WHITE,
            box_shadow="0 2px 12px rgba(10,35,66,0.05)",
        ),
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.box(width="20px", height="2px",
                           background=SUN, border_radius="2px"),
                    rx.text("Itinerario del día",
                            font_size="0.68rem", font_weight="700",
                            letter_spacing="0.15em", text_transform="uppercase",
                            color=SKY, font_family="'DM Sans', sans-serif"),
                    align="center", spacing="2",
                ),
                *[
                    itinerario_item(hora, act, last=(i == len(itinerario) - 1))
                    for i, (hora, act) in enumerate(itinerario)
                ],
                spacing="0",
                align="start",
                width="100%",
            ),
            width="100%",
            padding="20px",
            border_radius="14px",
            border=f"1px solid {BORDER}",
            background=WHITE,
            box_shadow="0 2px 12px rgba(10,35,66,0.05)",
        ),
        rx.link(
            rx.button(
                rx.icon("calendar-check", size=15),
                "Reservar ahora",
                background=f"linear-gradient(135deg, {SUN}, #E08A10)",
                color=OCEAN,
                font_family="'DM Sans', sans-serif",
                font_size="0.92rem",
                font_weight="700",
                padding="14px 34px",
                border_radius="40px",
                border="none",
                cursor="pointer",
                gap="8px",
                box_shadow="0 6px 24px rgba(244,160,28,0.40)",
                _hover={
                    "transform": "translateY(-3px)",
                    "box_shadow": "0 12px 32px rgba(244,160,28,.55)",
                },
                transition="all .22s ease",
            ),
            href="/reservas",
        ),
        spacing="5",
        align="start",
        flex="1",
        min_width="280px",
    )

    children = [img_col, info_col] if not reverse else [info_col, img_col]

    return rx.flex(
        *children,
        gap="52px",
        flex_wrap="wrap",
        align="start",
        width="100%",
    )


# ── Data ──────────────────────────────────────────────────────────────────────

ITINERARIO_BASE = [
    ("07:00 AM", "Salida desde Santo Domingo"),
    ("09:00 AM", "Llegada al punto de encuentro"),
    ("10:00 AM", "Inicio de la actividad principal"),
    ("12:30 PM", "Almuerzo buffet incluido"),
    ("02:00 PM", "Tiempo libre y actividades"),
    ("04:00 PM", "Regreso al punto de salida"),
]


# ── Page ──────────────────────────────────────────────────────────────────────

@rx.page(route="/descripcion", on_load=SearchState.on_load)
def descripcion() -> rx.Component:
    return rx.box(

        rx.script(
            "var l=document.createElement('link');l.rel='stylesheet';"
            "l.href='https://fonts.googleapis.com/css2?family=Cormorant+Garamond"
            ":ital,wght@0,600;0,700;1,600&family=DM+Sans:wght@300;400;500;700&display=swap';"
            "document.head.appendChild(l);"
        ),

        navbar(),

        # ── HERO ──────────────────────────────────────────────────────────
        rx.box(
            rx.box(
                position="absolute", inset="0",
                background=(
                    "linear-gradient(160deg,"
                    "rgba(10,35,66,.92) 0%,"
                    "rgba(26,107,138,.50) 55%,"
                    "rgba(10,35,66,.94) 100%)"
                ),
                z_index="1",
            ),
            rx.vstack(
                rx.hstack(
                    rx.box(width="32px", height="1px", background=SUN, opacity="0.65"),
                    rx.text(
                        "República Dominicana",
                        font_size="0.68rem", font_weight="500",
                        letter_spacing="0.24em", text_transform="uppercase",
                        color=SUN, font_family="'DM Sans', sans-serif",
                    ),
                    rx.box(width="32px", height="1px", background=SUN, opacity="0.65"),
                    align="center", spacing="3",
                ),
                rx.heading(
                    "Nuestros ",
                    rx.text.span("Destinos", color=SUN),
                    font_family="'Cormorant Garamond', serif",
                    font_size="3.8rem",
                    font_weight="700",
                    color=WHITE,
                    text_align="center",
                    line_height="1.05",
                    as_="h1",
                ),
                rx.text(
                    "Conoce los detalles de nuestras principales experiencias turísticas.",
                    font_size="1rem",
                    font_weight="300",
                    color="rgba(255,255,255,0.72)",
                    text_align="center",
                    max_width="540px",
                    line_height="1.75",
                    font_family="'DM Sans', sans-serif",
                ),
                spacing="5",
                align="center",
                position="relative",
                z_index="2",
                padding="96px 20px 100px",
            ),
            background_image="url('/hero.png')",
            background_size="cover",
            background_position="center",
            position="relative",
            overflow="hidden",
            min_height="52vh",
            display="flex",
            align_items="center",
            justify_content="center",
        ),

        # ── DESTINOS (filtrados) ───────────────────────────────────────────
        rx.box(
            rx.vstack(

                # Isla Saona
                rx.cond(
                    (SearchState.destino == "") |
                    SearchState.destino.lower().contains("saona"),
                    rx.fragment(
                        lugar_descripcion(
                            "/saona.jpg",
                            "Isla Saona",
                            "Disfruta de aguas cristalinas, arena blanca y un ambiente tropical perfecto "
                            "para relajarte y vivir una experiencia inolvidable en el Caribe.",
                            "1 día completo", "Incluido",
                            "Almuerzo buffet, guía y catamarán",
                            "RD$3,500",
                            ITINERARIO_BASE,
                            reverse=False,
                        ),
                        dot_separator(),
                    ),
                    rx.box(),
                ),

                # Samaná
                rx.cond(
                    (SearchState.destino == "") |
                    SearchState.destino.lower().contains("samana") |
                    SearchState.destino.lower().contains("samaná"),
                    rx.fragment(
                        lugar_descripcion(
                            "/samana.jpg",
                            "Samaná",
                            "Vive una escapada natural entre playas, montañas, cascadas y paisajes verdes "
                            "que muestran la belleza auténtica y genuina del país.",
                            "1 día completo", "Incluido",
                            "Almuerzo, guía y puntos naturales",
                            "RD$4,200",
                            ITINERARIO_BASE,
                            reverse=True,
                        ),
                        dot_separator(),
                    ),
                    rx.box(),
                ),

                # Punta Cana
                rx.cond(
                    (SearchState.destino == "") |
                    SearchState.destino.lower().contains("punta"),
                    lugar_descripcion(
                        "/puntacana.jpg",
                        "Punta Cana",
                        "Relájate en uno de los destinos más famosos del Caribe, ideal para disfrutar "
                        "playas espectaculares, resorts y actividades de primer nivel.",
                        "1 día completo", "Incluido",
                        "Playa, almuerzo y actividades",
                        "RD$5,000",
                        ITINERARIO_BASE,
                        reverse=False,
                    ),
                    rx.box(),
                ),

                spacing="9",
                align="stretch",
                width="100%",
                max_width="1100px",
                margin="0 auto",
            ),
            background=LIGHT,
            padding="72px 32px 96px",
        ),

        footer(),

        background=LIGHT,
        font_family="'DM Sans', sans-serif",
        width="100%",
    )