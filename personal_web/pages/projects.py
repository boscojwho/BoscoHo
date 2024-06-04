import reflex as rx
from ..templates import template


@rx.page(
    route="/projects",
    title="Projects"
)
@template.page
def projects() -> rx.Component:
    return rx.text("Projects")