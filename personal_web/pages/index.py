import reflex as rx

from ..templates import template
from ..examples import __columns_with_nav_bar

from personal_web import styles


@template.page(
    route="/",
    title="Home",
    show_sidebar_right=False
)
def index() -> rx.Component:
    return rx.vstack(
        rx.text("🍁", size="9")
    )
