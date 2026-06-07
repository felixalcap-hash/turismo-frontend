import reflex as rx

config = rx.Config(
    app_name="turismo_frontend",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)