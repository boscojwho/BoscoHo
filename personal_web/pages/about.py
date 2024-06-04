import reflex as rx
from ..templates import template


@rx.page(
    route="/about",
    title="About"
)
@template.page
def about() -> rx.Component:
    return rx.text("About")