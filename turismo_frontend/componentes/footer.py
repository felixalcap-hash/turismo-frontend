
import reflex as rx
 
OCEAN = "#0A2342"
SKY   = "#1A6B8A"
SUN   = "#F4A01C"
WHITE = "#FFFFFF"
 
 
def footer_link(label: str, href: str) -> rx.Component:
    return rx.link(
        label,
        href=href,
        font_size="0.82rem",
        color="rgba(255,255,255,0.55)",
        text_decoration="none",
        letter_spacing="0.04em",
        _hover={"color": SUN},
        transition="color .2s ease",
    )
 
 
def social_icon(icon: str, href: str, label: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.icon(icon, size=16, color="rgba(255,255,255,0.7)"),
            width="38px",
            height="38px",
            border_radius="50%",
            border="1px solid rgba(255,255,255,0.15)",
            display="flex",
            align_items="center",
            justify_content="center",
            background="rgba(255,255,255,0.06)",
            _hover={"background": SUN, "border_color": SUN},
            transition="all .2s ease",
        ),
        href=href,
        aria_label=label,
    )
 
 
def footer() -> rx.Component:
    return rx.box(
 
        rx.box(
            height="3px",
            width="100%",
            background=f"linear-gradient(90deg, transparent, {SUN}, transparent)",
            opacity="0.6",
        ),
 
        rx.box(
            rx.flex(
 
                # Columna 1 — Marca
                rx.vstack(
                    rx.hstack(
                        rx.image(src="/logo.png", width="36px", height="36px"),
                        rx.text(
                            "Caribe",
                            rx.text.span("Go", color=SUN),
                            font_family="'Cormorant Garamond', serif",
                            font_size="1.5rem",
                            font_weight="700",
                            color=WHITE,
                            line_height="1",
                        ),
                        align="center",
                        spacing="2",
                    ),
                    rx.text(
                        "Descubre experiencias inolvidables en los destinos "
                        "más paradisíacos del Caribe.",
                        font_size="0.85rem",
                        color="rgba(255,255,255,0.52)",
                        line_height="1.7",
                        max_width="240px",
                    ),
                    rx.hstack(
                        social_icon("facebook", "#", "Facebook"),
                        social_icon("instagram", "#", "Instagram"),
                        social_icon("message-circle", "#", "WhatsApp"),
                        spacing="3",
                        margin_top="4px",
                    ),
                    align="start",
                    spacing="4",
                    flex="1.4",
                    min_width="200px",
                ),
 
                # Columna 2 — Destinos
                rx.vstack(
                    rx.text(
                        "Destinos",
                        font_size="0.7rem",
                        font_weight="600",
                        letter_spacing="0.18em",
                        text_transform="uppercase",
                        color=SUN,
                        margin_bottom="4px",
                    ),
                    footer_link("Isla Saona", "/descripcion"),
                    footer_link("Samaná", "/descripcion"),
                    footer_link("Punta Cana", "/descripcion"),
                    align="start",
                    spacing="3",
                    flex="1",
                    min_width="140px",
                ),
 
                # Columna 3 — Navegación
                rx.vstack(
                    rx.text(
                        "Navegación",
                        font_size="0.7rem",
                        font_weight="600",
                        letter_spacing="0.18em",
                        text_transform="uppercase",
                        color=SUN,
                        margin_bottom="4px",
                    ),
                    footer_link("Inicio", "/"),
                    footer_link("Descripción", "/descripcion"),
                    footer_link("Reservas", "/reservas"),
                    align="start",
                    spacing="3",
                    flex="1",
                    min_width="140px",
                ),
 
                # Columna 4 — Contacto
                rx.vstack(
                    rx.text(
                        "Contacto",
                        font_size="0.7rem",
                        font_weight="600",
                        letter_spacing="0.18em",
                        text_transform="uppercase",
                        color=SUN,
                        margin_bottom="4px",
                    ),
                    rx.hstack(
                        rx.icon("mail", size=14, color="rgba(255,255,255,0.45)"),
                        rx.text("hola@caribego.com", font_size="0.82rem", color="rgba(255,255,255,0.55)"),
                        align="center", spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("phone", size=14, color="rgba(255,255,255,0.45)"),
                        rx.text("+1 (809) 555-0199", font_size="0.82rem", color="rgba(255,255,255,0.55)"),
                        align="center", spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("map-pin", size=14, color="rgba(255,255,255,0.45)"),
                        rx.text("Santo Domingo, RD", font_size="0.82rem", color="rgba(255,255,255,0.55)"),
                        align="center", spacing="2",
                    ),
                    align="start",
                    spacing="3",
                    flex="1.2",
                    min_width="170px",
                ),
 
                gap="48px",
                flex_wrap="wrap",
                width="100%",
                align="start",
            ),
            max_width="1200px",
            margin="0 auto",
            padding="56px 32px 40px",
        ),
 
        rx.box(
            rx.box(height="1px", background="rgba(255,255,255,0.08)", width="100%"),
            rx.flex(
                rx.text(
                    "© 2026 CaribeGo. Todos los derechos reservados.",
                    font_size="0.78rem",
                    color="rgba(255,255,255,0.32)",
                    letter_spacing="0.03em",
                ),
                rx.hstack(
                    footer_link("Términos", "#"),
                    rx.box(width="1px", height="12px", background="rgba(255,255,255,0.15)"),
                    footer_link("Privacidad", "#"),
                    spacing="3",
                    align="center",
                ),
                justify="between",
                align="center",
                flex_wrap="wrap",
                gap="12px",
                padding="20px 32px",
                max_width="1200px",
                margin="0 auto",
                width="100%",
            ),
        ),
 
        background=f"linear-gradient(160deg, {OCEAN} 0%, #0D3558 50%, {SKY} 100%)",
        width="100%",
        margin_top="0",
    )
 