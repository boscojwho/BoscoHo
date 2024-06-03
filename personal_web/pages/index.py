import reflex as rx

from ..examples import __columns_with_nav_bar

from personal_web import styles

@rx.page(
    route="/",
    title="Home"
)
def index() -> rx.Component:
    return __columns_with_nav_bar.index()