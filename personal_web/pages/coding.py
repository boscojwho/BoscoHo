import reflex as rx
from ..templates import template


@template.page(
    route="/coding",
    title="Coding",
)
def coding() -> rx.Component:
    return rx.text("Coding")