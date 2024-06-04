import reflex as rx
from ..templates import template


@template.page(
    route="/about",
    title="About",
)
def about() -> rx.Component:
    return rx.text("About")