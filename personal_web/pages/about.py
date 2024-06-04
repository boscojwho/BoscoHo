import reflex as rx
from ..templates import template


@template.page(
    route="/",
    title="Home",
)
def about() -> rx.Component:
    return rx.text("About")