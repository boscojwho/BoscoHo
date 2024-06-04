import reflex as rx

from ..templates import template
from ..examples import __columns_with_nav_bar

from personal_web import styles


@rx.page(
    route="/",
    title="Home"
)
@template.page
def index() -> rx.Component:
    return rx.vstack(
        rx.text("content"),
        height="100em"
    )
