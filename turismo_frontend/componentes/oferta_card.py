import reflex as rx


def oferta_card(imagen: str, titulo: str, descripcion: str, precio: str) -> rx.Component:
    return rx.box(
        rx.image(
            src=imagen,
            width="100%",
            height="220px",
            object_fit="cover",
            border_radius="18px 18px 0 0",
        ),

        rx.vstack(
            rx.heading(
                titulo,
                size="5",
                color="#023047",
            ),

            rx.text(
                descripcion,
                color="#555",
                font_size="0.95rem",
            ),

            rx.hstack(
                rx.text(
                    precio,
                    color="#FB8500",
                    font_weight="bold",
                    font_size="1.1rem",
                ),
                rx.button(
                    "Ver más",
                    background="#023047",
                    color="white",
                    border_radius="10px",
                    cursor="pointer",
                ),
                justify="between",
                align="center",
                width="100%",
            ),

            spacing="4",
            padding="20px",
        ),

        background="white",
        border_radius="18px",
        box_shadow="0 8px 25px rgba(0,0,0,0.10)",
        overflow="hidden",
        transition="0.3s",
        _hover={
            "transform": "translateY(-6px)",
            "box_shadow": "0 12px 35px rgba(0,0,0,0.16)",
        },
    )