import reflex as rx
from ..templates import template


@template.page(
    route="/about",
    title="About",
    show_sidebar_right=False
)
def about() -> rx.Component:
    return rx.flex(
        rx.spacer(height="20px"),
        rx.hstack(
            rx.text("mastodon:"),
            rx.link(
                "sideshow_boz",
                href="https://mastodon.social/@sideshow_boz")
        ),
        rx.hstack(
            rx.text("github:"),
            rx.link(
                "boscojwho",
                href="https://github.com/boscojwho")
        ),
        rx.divider(),
        rx.text(
            "built with ",
            rx.text.strong("python"),
            as_="p",
        ),
        direction="column",
        spacing="2"
    )