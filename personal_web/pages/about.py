import reflex as rx
from ..templates import template


@template.page(
    route="/about",
    title="About",
    show_sidebar_right=False
)
def about() -> rx.Component:
    return rx.flex(
        rx.text("mastodon: sideshow_boz[@]mastodon[.]social"),
        rx.text("github: boscojwho"),
        rx.divider(),
        rx.text(
            "built with ",
            rx.text.strong("python"),
            as_="p",
        ),
        direction="column",
        spacing="2"
    )