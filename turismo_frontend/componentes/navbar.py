import reflex as rx

OCEAN = "#0A2342"
SKY   = "#1A6B8A"
SUN   = "#F4A01C"
WHITE = "#FFFFFF"


def nav_link(label: str, href: str) -> rx.Component:
    return rx.link(
        label,
        href=href,
        font_size="0.85rem",
        font_weight="500",
        letter_spacing="0.04em",
        color="rgba(10,35,66,0.65)",
        text_decoration="none",
        padding="6px 2px",
        border_bottom="2px solid transparent",
        _hover={
            "color": OCEAN,
            "border_bottom_color": SUN,
        },
        transition="all .2s ease",
    )


def navbar() -> rx.Component:
    return rx.box(

        # Línea dorada decorativa en el tope
        rx.box(
            height="3px",
            width="100%",
            background=f"linear-gradient(90deg, transparent, {SUN} 40%, {SUN} 60%, transparent)",
            opacity="0.7",
        ),

        # Contenido de la navbar
        rx.flex(

            # ── Logo + nombre ──────────────────────────────────────────
            rx.hstack(
                rx.image(
                    src="/logo.png",
                    width="38px",
                    height="38px",
                    border_radius="50%",
                    border=f"2px solid {SUN}",
                ),
                rx.text(
                    "Caribe",
                    rx.text.span("Go", color=SUN),
                    font_family="'Cormorant Garamond', serif",
                    font_size="1.5rem",
                    font_weight="700",
                    color=OCEAN,
                    line_height="1",
                ),
                align="center",
                spacing="2",
            ),

            # ── Links de navegación ────────────────────────────────────
            rx.hstack(
                nav_link("Inicio", "/"),
                nav_link("Descripción", "/descripcion"),
                nav_link("Reservas", "/reservas"),
                spacing="7",
                align="center",
            ),

            # ── CTA ────────────────────────────────────────────────────
            rx.button(
                rx.icon("log-in", size=15),
                "Reservar ahora",
                background=OCEAN,
                color=WHITE,
                font_family="'DM Sans', sans-serif",
                font_size="0.82rem",
                font_weight="600",
                letter_spacing="0.03em",
                padding="9px 20px",
                border_radius="40px",
                border="none",
                cursor="pointer",
                on_click=rx.redirect("/reservas"), 
                gap="7px",
                _hover={
                    "background": SKY,
                    "transform": "translateY(-1px)",
                    "box_shadow": f"0 6px 20px rgba(10,35,66,0.25)",
                },
                transition="all .2s ease",
            ),

            justify="between",
            align="center",
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding="14px 32px",
        ),

        width="100%",
        background="rgba(255,255,255,0.97)",
        box_shadow="0 1px 0 rgba(10,35,66,0.06), 0 4px 24px rgba(10,35,66,0.05)",
        position="sticky",
        top="0",
        z_index="100",
        backdrop_filter="blur(12px)",
    )