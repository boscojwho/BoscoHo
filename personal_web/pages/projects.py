import reflex as rx
from ..templates import template


@template.page(
    route="/",
    title="Home",
)
def projects() -> rx.Component:
    return rx.text("Projects")