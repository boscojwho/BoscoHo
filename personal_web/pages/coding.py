import reflex as rx
from ..templates import template


@rx.page(
    route="/coding",
    title="Coding"
)
@template.page
def coding() -> rx.Component:
    return rx.text("Coding")