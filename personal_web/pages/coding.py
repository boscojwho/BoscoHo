import reflex as rx
from ..templates import template


@template.page(
    route="/coding",
    title="Coding",
    show_sidebar_right=False
)
def coding() -> rx.Component:
    return rx.text("Coding")