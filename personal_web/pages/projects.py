import reflex as rx
from ..templates import template


@template.page(
    route="/projects",
    title="Projects",
)
def projects() -> rx.Component:
    return rx.text("Projects")