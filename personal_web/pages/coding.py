import reflex as rx
from ..templates import template


@template.page(
    route="/",
    title="Home",
)
def coding() -> rx.Component:
    return rx.text("Coding")