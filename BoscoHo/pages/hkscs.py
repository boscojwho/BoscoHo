import reflex as rx
from ..templates import template


@template.page(
    route="/projects/hk_characters",
    title="HK Characters",
    show_sidebar_right=False
)
def index() -> rx.Component:
    return rx.flex(
        rx.card(
            rx.flex(
                rx.chakra.image(src="/hkscs_icon.png", width="120px", height="auto", borderRadius="26.844"),
                rx.vstack(
                    rx.text("HK Characters", size="8", weight="bold", trim="both",),
                    rx.text("Explore Hong Kong words.", size="5", weight="medium", trim="both",)
                ),
                spacing="4",
                align_items="flex-start",
                flex_wrap="wrap",
            ),
            variant="classic",
        ),
        rx.chakra.image(src="/hkscs_landscape.png", height="auto", borderRadius="24"),
        rx.divider(),
        rx.vstack(
            rx.text("Feature List"),
            rx.text("Feature 1"),
            rx.text("Feature 2"),
            rx.text("Feature 3"),
        ),
        rx.divider(),
        rx.link(
            rx.text("Privacy Policy"),
            href="/privacy/file/hkscs.md"
        ),
        spacing = "4",
        align_items = "flex-start",
        flex_wrap = "wrap",
    )