import reflex as rx
from turismo_frontend.componentes.navbar import navbar
from turismo_frontend.componentes.footer import footer
from turismo_frontend.state.search_state import SearchState


OCEAN = "#0A2342"
SKY   = "#1A6B8A"
SUN   = "#F4A01C"
WHITE = "#FFFFFF"
FOAM  = "#EEF5F9"
MUTED = "#6B7B8D"

INPUT_STYLE = {
    "border": "1.5px solid #DDE6EE",
    "border_radius": "10px",
    "padding": "11px 14px",
    "font_size": "0.88rem",
    "background": FOAM,
    "outline": "none",
    "width": "100%",
    "font_family": "'DM Sans', sans-serif",
    "color": "#1A1A2E",
}


def eyebrow(text: str) -> rx.Component:
    return rx.hstack(
        rx.box(width="28px", height="1px", background=SUN, opacity="0.7"),
        rx.text(
            text,
            font_size="0.72rem",
            font_weight="500",
            letter_spacing="0.2em",
            text_transform="uppercase",
            color=SKY,
        ),
        rx.box(width="28px", height="1px", background=SUN, opacity="0.7"),
        align="center",
        spacing="3",
        margin_bottom="8px",
    )


def stat_item(number: str, label: str) -> rx.Component:
    return rx.vstack(
        rx.text(
            number,
            font_family="'Cormorant Garamond', serif",
            font_size="1.9rem",
            font_weight="700",
            color=SUN,
            line_height="1",
        ),
        rx.text(
            label,
            font_size="0.68rem",
            letter_spacing="0.12em",
            text_transform="uppercase",
            color="rgba(255,255,255,0.5)",
        ),
        align="center",
        spacing="1",
    )


def oferta_card(
    img_src: str,
    titulo: str,
    descripcion: str,
    precio: str,
) -> rx.Component:
    return rx.box(
        rx.image(
            src=img_src,
            width="100%",
            height="190px",
            object_fit="cover",
            display="block",
        ),
        rx.vstack(
            rx.text(
                titulo,
                font_family="'Cormorant Garamond', serif",
                font_size="1.25rem",
                font_weight="700",
                color=OCEAN,
            ),
            rx.text(
                descripcion,
                font_size="0.83rem",
                color=MUTED,
                line_height="1.6",
            ),
            rx.hstack(
                rx.text(precio, font_size="0.85rem", font_weight="500", color=SKY),
                rx.button(
                    "Reservar",
                    background=SUN,
                    color=OCEAN,
                    font_family="'DM Sans', sans-serif",
                    font_size="0.78rem",
                    font_weight="600",
                    padding="6px 18px",
                    border_radius="40px",
                    border="none",
                    cursor="pointer",
                    on_click=rx.redirect("/reservas"), 
                    _hover={"opacity": "0.85"},
                    transition="opacity .2s",
                ),
                justify="between",
                width="100%",
                align="center",
                margin_top="6px",
            ),
            padding="16px 18px",
            spacing="2",
            align="start",
        ),
        border_radius="16px",
        overflow="hidden",
        border="1px solid #DDE6EE",
        background=WHITE,
        box_shadow="0 4px 20px rgba(10,35,66,0.08)",
        _hover={
            "box_shadow": "0 10px 36px rgba(10,35,66,0.16)",
            "transform": "translateY(-4px)",
        },
        transition="all .24s ease",
    )


def about_chip(label: str) -> rx.Component:
    return rx.hstack(
        rx.box(width="7px", height="7px", border_radius="50%", background=SUN, flex_shrink="0"),
        rx.text(label, font_size="0.82rem", color="rgba(255,255,255,0.88)"),
        align="center",
        spacing="2",
        background="rgba(255,255,255,0.09)",
        border="1px solid rgba(255,255,255,0.18)",
        border_radius="40px",
        padding="8px 18px",
    )


def inicio() -> rx.Component:
    return rx.box(

        rx.script(
            "var l=document.createElement('link');l.rel='stylesheet';"
            "l.href='https://fonts.googleapis.com/css2?family=Cormorant+Garamond"
            ":wght@600;700&family=DM+Sans:wght@300;400;500&display=swap';"
            "document.head.appendChild(l);"
        ),

        navbar(),

        # ── HERO ──────────────────────────────────────────────────────────
        rx.box(
            rx.box(
                position="absolute", inset="0",
                background=(
                    "linear-gradient(160deg,"
                    "rgba(10,35,66,.85) 0%,"
                    "rgba(26,107,138,.46) 52%,"
                    "rgba(10,35,66,.88) 100%)"
                ),
                z_index="1",
            ),
            rx.vstack(
                rx.hstack(
                    rx.box(width="36px", height="1px", background=SUN, opacity="0.75"),
                    rx.text(
                        "República Dominicana",
                        font_size="0.72rem",
                        font_weight="500",
                        letter_spacing="0.22em",
                        text_transform="uppercase",
                        color=SUN,
                    ),
                    rx.box(width="36px", height="1px", background=SUN, opacity="0.75"),
                    align="center",
                    spacing="3",
                ),
                rx.heading(
                    "Tu próxima aventura comienza ",
                    rx.text.span("aquí", color=SUN),
                    font_family="'Cormorant Garamond', serif",
                    font_size="3.6rem",
                    font_weight="700",
                    color=WHITE,
                    line_height="1.08",
                    text_align="center",
                    max_width="780px",
                    as_="h1",
                ),
                rx.text(
                    "Encuentra destinos increíbles, ofertas exclusivas y actividades "
                    "para crear recuerdos que duran toda la vida.",
                    font_family="'DM Sans', sans-serif",
                    font_size="1.05rem",
                    font_weight="300",
                    color="rgba(255,255,255,0.8)",
                    text_align="center",
                    max_width="560px",
                    line_height="1.75",
                ),
                rx.button(
                    rx.icon("map-pin", size=16),
                    "Explorar destinos",
                    background=SUN,
                    color=OCEAN,
                    font_family="'DM Sans', sans-serif",
                    font_size="0.95rem",
                    font_weight="600",
                    padding="14px 34px",
                    border_radius="40px",
                    border="none",
                    cursor="pointer",
                    on_click=rx.redirect("/descripcion"), 
                    gap="8px",
                    _hover={
                        "transform": "translateY(-3px)",
                        "box_shadow": "0 14px 40px rgba(244,160,28,.5)",
                    },
                    transition="all .22s ease",
                ),
                spacing="6",
                align="center",
                position="relative",
                z_index="2",
                padding="80px 20px 100px",
            ),
            background_image="url('/hero.png')",
            background_size="cover",
            background_position="center",
            position="relative",
            overflow="hidden",
            min_height="88vh",
            display="flex",
            align_items="center",
            justify_content="center",
        ),

        # ── STATS ─────────────────────────────────────────────────────────
        rx.flex(
            stat_item("120+", "Destinos"),
            rx.divider(
                orientation="vertical", height="40px",
                border_color="rgba(255,255,255,0.12)",
            ),
            stat_item("15K+", "Viajeros felices"),
            rx.divider(
                orientation="vertical", height="40px",
                border_color="rgba(255,255,255,0.12)",
            ),
            stat_item("98%", "Satisfacción"),
            rx.divider(
                orientation="vertical", height="40px",
                border_color="rgba(255,255,255,0.12)",
            ),
            stat_item("5 ★", "Calificación media"),
            background=OCEAN,
            padding="28px 48px",
            justify="center",
            gap="32px",
            flex_wrap="wrap",
            width="100%",
            align="center",
        ),

        # ── BUSCADOR ──────────────────────────────────────────────────────
      

rx.box(
    rx.box(
        rx.text(
            "¿A dónde quieres ir?",
            font_size="0.7rem",
            font_weight="500",
            letter_spacing="0.15em",
            text_transform="uppercase",
            color=SKY,
            margin_bottom="14px",
            font_family="'DM Sans', sans-serif",
        ),
        rx.flex(
            rx.box(
                rx.el.input(
                    placeholder="Destino o actividad",
                    type="text",
                    value=SearchState.destino,
                    on_change=SearchState.set_destino,
                    style=INPUT_STYLE,
                ),
                flex="2",
                min_width="150px",
            ),
            rx.box(
                rx.el.input(
                    type="date",
                    value=SearchState.fecha,
                    on_change=SearchState.set_fecha,
                    style=INPUT_STYLE,
                ),
                flex="1",
                min_width="140px",
            ),
            rx.box(
                rx.el.input(
                    placeholder="Personas",
                    type="number",
                    min="1",
                    value=SearchState.personas,
                    on_change=SearchState.set_personas,
                    style=INPUT_STYLE,
                ),
                flex="0.8",
                min_width="110px",
            ),
            rx.el.button(
                "Buscar →",
                on_click=SearchState.buscar,
                style={
                    "background": OCEAN,
                    "color": WHITE,
                    "font_family": "'DM Sans', sans-serif",
                    "font_size": "0.92rem",
                    "font_weight": "600",
                    "padding": "11px 30px",
                    "border_radius": "10px",
                    "border": "none",
                    "cursor": "pointer",
                    "white_space": "nowrap",
                    "flex_shrink": "0",
                },
            ),
            gap="12px",
            width="100%",
            flex_wrap="wrap",
            align="end",
        ),
        max_width="960px",
        margin="0 auto",
        background=WHITE,
        padding="28px 32px",
        border_radius="18px",
        box_shadow="0 16px 56px rgba(10,35,66,0.13)",
    ),
    background="#F0F6FA",
    padding="40px 24px",
    width="100%",
),

        # ── OFERTAS ───────────────────────────────────────────────────────
        rx.vstack(
            eyebrow("Experiencias seleccionadas"),
            rx.heading(
                "Ofertas turísticas destacadas",
                font_family="'Cormorant Garamond', serif",
                font_size="2.8rem",
                font_weight="700",
                color=OCEAN,
                line_height="1.1",
                text_align="center",
                as_="h2",
            ),
            rx.text(
                "Elige una experiencia y reserva tu próxima aventura.",
                font_size="0.95rem",
                color=MUTED,
                margin_bottom="12px",
            ),
            rx.grid(
                oferta_card(
                    "/saona.jpg",
                    "Isla Saona",
                    "Disfruta aguas cristalinas, arena blanca y un día completo en el paraíso.",
                    "Desde RD$3,500",
                ),
                oferta_card(
                    "/samana.jpg",
                    "Samaná",
                    "Vive una escapada natural entre playas, montañas y paisajes impresionantes.",
                    "Desde RD$4,200",
                ),
                oferta_card(
                    "/puntacana.jpg",
                    "Punta Cana",
                    "Relájate en uno de los destinos más famosos del Caribe dominicano.",
                    "Desde RD$5,000",
                ),
                columns=rx.breakpoints(initial="1", sm="2", md="3"),
                spacing="5",
                width="100%",
            ),
            max_width="1200px",
            margin="0 auto",
            padding="72px 32px 80px",
            spacing="4",
            align="center",
            width="100%",
        ),

        # ── SOBRE NOSOTROS ────────────────────────────────────────────────
        rx.box(
            rx.text(
                "\u201C",
                position="absolute",
                top="-60px",
                left="4%",
                font_family="'Cormorant Garamond', serif",
                font_size="18rem",
                color="rgba(255,255,255,0.04)",
                line_height="1",
                pointer_events="none",
                user_select="none",
            ),
            rx.vstack(
                eyebrow("Nuestra misión"),
                rx.heading(
                    "Sobre nuestra plataforma",
                    font_family="'Cormorant Garamond', serif",
                    font_size="2.6rem",
                    font_weight="700",
                    color=WHITE,
                    text_align="center",
                    as_="h2",
                ),
                rx.text(
                    "Somos una plataforma turística creada para facilitar la búsqueda, "
                    "comparación y reserva de ofertas en República Dominicana. Nuestro objetivo "
                    "es conectar a los usuarios con experiencias seguras, accesibles y memorables.",
                    font_family="'DM Sans', sans-serif",
                    font_size="1rem",
                    font_weight="300",
                    color="rgba(255,255,255,0.78)",
                    line_height="1.85",
                    text_align="center",
                    max_width="680px",
                ),
                rx.flex(
                    about_chip("Reservas seguras"),
                    about_chip("Precios transparentes"),
                    about_chip("Atención 24/7"),
                    about_chip("100% local"),
                    flex_wrap="wrap",
                    justify="center",
                    gap="12px",
                ),
                spacing="5",
                align="center",
                position="relative",
                z_index="1",
                max_width="780px",
                margin="0 auto",
            ),
            background=f"linear-gradient(135deg, {OCEAN} 0%, {SKY} 100%)",
            padding="90px 48px",
            position="relative",
            overflow="hidden",
            width="100%",
        ),

        footer(),

        background="#F8FAFC",
        font_family="'DM Sans', sans-serif",
        width="100%",
    )