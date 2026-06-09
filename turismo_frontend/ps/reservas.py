import reflex as rx
from turismo_frontend.componentes.navbar import navbar
from turismo_frontend.componentes.footer import footer


def info_row(icon: str, text: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(icon, font_size="18px"),
            background="rgba(255,183,3,0.15)",
            border_radius="10px",
            padding="8px 10px",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        rx.text(text, color="#444", font_size="15px", font_family="'Georgia', serif"),
        spacing="3",
        align="center",
    )


def section_label(text: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            width="4px",
            height="20px",
            background="linear-gradient(180deg, #FFB703, #FB8500)",
            border_radius="4px",
        ),
        rx.text(
            text,
            font_size="16px",
            font_weight="700",
            color="#023047",
            letter_spacing="0.04em",
            text_transform="uppercase",
            font_family="'Georgia', serif",
        ),
        spacing="3",
        align="center",
        margin_bottom="4px",
    )


def styled_input(placeholder: str, input_type: str = "text") -> rx.Component:
    return rx.input(
        placeholder=placeholder,
        type=input_type,
        width="100%",
        height="48px",
        padding="0 16px",
        border="1.5px solid #E2E8F0",
        border_radius="12px",
        font_size="15px",
        font_family="'Georgia', serif",
        color="#1a1a2e",
        background="white",
        _focus={
            "outline": "none",
            "border_color": "#FFB703",
            "box_shadow": "0 0 0 3px rgba(255,183,3,0.18)",
        },
        _placeholder={"color": "#A0AEC0"},
    )

def enviar_reserva():
    return rx.toast.success(
        "¡Reserva enviada con éxito! Un asesor de CaribeGo se pondrá en contacto contigo pronto para confirmar los detalles de tu viaje."
    )

def reservas() -> rx.Component:
    return rx.box(
        navbar(),

        # ── HERO ──────────────────────────────────────────────
        rx.box(
            rx.box(
                rx.vstack(
                    rx.box(
                        rx.text(
                            "✦  RESERVA TU AVENTURA  ✦",
                            color="#FFB703",
                            font_size="12px",
                            font_weight="700",
                            letter_spacing="0.2em",
                            font_family="'Georgia', serif",
                        ),
                        margin_bottom="16px",
                    ),
                    rx.heading(
                        "Vive República",
                        rx.text(" Dominicana", as_="span", color="#FFB703"),
                        size="9",
                        color="white",
                        text_align="center",
                        line_height="1.1",
                        font_family="'Georgia', serif",
                    ),
                    rx.text(
                        "Completa tus datos y asegura tu próxima experiencia caribeña.",
                        color="rgba(255,255,255,0.75)",
                        text_align="center",
                        max_width="560px",
                        font_size="17px",
                        line_height="1.7",
                        font_family="'Georgia', serif",
                    ),
                    spacing="4",
                    align="center",
                ),
                max_width="800px",
                margin="0 auto",
                padding="0 20px",
            ),
            background="linear-gradient(135deg, #011F2E 0%, #023047 55%, #014E6A 100%)",
            padding="100px 20px 90px",
            position="relative",
            overflow="hidden",
            _before={
                "content": '""',
                "position": "absolute",
                "top": "-80px",
                "right": "-80px",
                "width": "380px",
                "height": "380px",
                "border_radius": "50%",
                "background": "radial-gradient(circle, rgba(255,183,3,0.12), transparent 70%)",
                "pointer_events": "none",
            },
        ),

        # ── MAIN CONTENT ──────────────────────────────────────
        rx.box(
            rx.flex(

                # LEFT — FORMULARIO
                rx.box(
                    rx.vstack(

                        # Datos personales
                        section_label("Datos de contacto"),
                        styled_input("Nombre completo"),
                        styled_input("Correo electrónico", "email"),
                        styled_input("Teléfono", "tel"),

                        rx.box(height="8px"),

                        # Detalles actividad
                        section_label("Detalles de la actividad"),

                        rx.select(
                            ["Isla Saona", "Samaná", "Punta Cana"],
                            placeholder="Selecciona un destino",
                            width="100%",
                            height="48px",
                            border="1.5px solid #E2E8F0",
                            border_radius="12px",
                            font_size="15px",
                            font_family="'Georgia', serif",
                            color="#1a1a2e",
                            background="white",
                            padding_left="16px",
                            _focus={
                                "outline": "none",
                                "border_color": "#FFB703",
                                "box_shadow": "0 0 0 3px rgba(255,183,3,0.18)",
                            },
                        ),

                        rx.hstack(
                            styled_input("Fecha de llegada", "date"),
                            styled_input("Personas", "number"),
                            spacing="4",
                            width="100%",
                        ),

                        rx.text_area(
                            placeholder="Comentario adicional (opcional)…",
                            width="100%",
                            min_height="110px",
                            padding="14px 16px",
                            border="1.5px solid #E2E8F0",
                            border_radius="12px",
                            font_size="15px",
                            font_family="'Georgia', serif",
                            resize="vertical",
                            _focus={
                                "outline": "none",
                                "border_color": "#FFB703",
                                "box_shadow": "0 0 0 3px rgba(255,183,3,0.18)",
                            },
                            _placeholder={"color": "#A0AEC0"},
                        ),

                        # Submit button
                        rx.button(
                            rx.hstack(
                                rx.text("Enviar Reserva", font_weight="700", font_size="16px"),
                                rx.text("→", font_size="20px"),
                                spacing="3",
                                align="center",
                            ),
                            background="linear-gradient(135deg, #FFB703, #FB8500)",
                            color="#023047",
                            border_radius="14px",
                            padding="0 32px",
                            height="54px",
                            width="100%",
                            cursor="pointer",
                            on_click=enviar_reserva,
                            box_shadow="0 4px 20px rgba(255,183,3,0.40)",
                            _hover={
                                "background": "linear-gradient(135deg, #FFC933, #FF9A00)",
                                "box_shadow": "0 6px 28px rgba(255,183,3,0.55)",
                                "transform": "translateY(-2px)",
                            },
                            transition="all 0.2s ease",
                            font_family="'Georgia', serif",
                        ),

                        spacing="3",
                        align="start",
                        width="100%",
                    ),
                    background="white",
                    padding="40px",
                    border_radius="24px",
                    box_shadow="0 12px 48px rgba(2,48,71,0.10)",
                    flex="1.35",
                    min_width="0",
                ),

                # RIGHT — INFO & PAGO
                rx.box(
                    rx.vstack(

                        # Payment info
                        rx.box(
                            rx.vstack(
                                section_label("Información de pago"),
                                rx.text(
                                    "Luego de enviar tu solicitud, nuestro equipo confirmará la disponibilidad y te contactará para finalizar el pago.",
                                    color="#555",
                                    font_size="14px",
                                    line_height="1.7",
                                    font_family="'Georgia', serif",
                                ),
                                rx.box(height="4px"),
                                section_label("Métodos aceptados"),
                                info_row("💳", "Tarjeta de crédito o débito"),
                                info_row("🏦", "Transferencia bancaria"),
                                info_row("💵", "Efectivo al confirmar"),
                                spacing="3",
                                align="start",
                            ),
                        ),

                        rx.divider(border_color="#E2E8F0", margin_y="4px"),

                        # Important note
                        rx.box(
                            rx.hstack(
                                rx.text("⚠️", font_size="20px"),
                                rx.text(
                                    "La reserva se confirma tras validar disponibilidad y método de pago.",
                                    font_size="13px",
                                    color="#666",
                                    line_height="1.6",
                                    font_family="'Georgia', serif",
                                ),
                                spacing="3",
                                align="start",
                            ),
                            background="#FFFBEB",
                            border="1px solid #FFE082",
                            border_radius="12px",
                            padding="14px 16px",
                            width="100%",
                        ),

                        # Contact card
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.box(
                                        rx.text("🌴", font_size="22px"),
                                        background="rgba(2,48,71,0.08)",
                                        border_radius="10px",
                                        padding="8px",
                                    ),
                                    rx.vstack(
                                        rx.text(
                                            "Soporte CaribeGo",
                                            font_weight="700",
                                            color="#023047",
                                            font_size="15px",
                                            font_family="'Georgia', serif",
                                        ),
                                        rx.text(
                                            "Estamos para ayudarte",
                                            font_size="12px",
                                            color="#888",
                                            font_family="'Georgia', serif",
                                        ),
                                        spacing="0",
                                        align="start",
                                    ),
                                    spacing="3",
                                    align="center",
                                ),
                                rx.divider(border_color="#E2E8F0"),
                                rx.hstack(
                                    rx.text("📧", font_size="15px"),
                                    rx.text(
                                        "reservas@caribego.com",
                                        font_size="14px",
                                        color="#023047",
                                        font_family="'Georgia', serif",
                                    ),
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.text("📞", font_size="15px"),
                                    rx.text(
                                        "809-000-0000",
                                        font_size="14px",
                                        color="#023047",
                                        font_family="'Georgia', serif",
                                    ),
                                    spacing="2",
                                ),
                                spacing="3",
                                align="start",
                                width="100%",
                            ),
                            background="white",
                            border="1.5px solid #E2E8F0",
                            border_radius="16px",
                            padding="20px",
                            width="100%",
                        ),

                        spacing="4",
                        align="start",
                        width="100%",
                    ),
                    background="white",
                    padding="40px",
                    border_radius="24px",
                    box_shadow="0 12px 48px rgba(2,48,71,0.10)",
                    flex="1",
                    min_width="0",
                ),

                gap="28px",
                align="start",
                flex_wrap="wrap",
                max_width="1200px",
                margin="70px auto",
                padding="0 24px",
            ),
            background="#F0F6FA",
            padding_bottom="70px",
        ),

        footer(),
        background="#F0F6FA",
    )