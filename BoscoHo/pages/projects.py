import reflex as rx
from ..templates import template


@template.page(
    route="/projects",
    title="Projects",
    show_sidebar_right=False
)
def projects() -> rx.Component:
    return rx.markdown(
        """
        ## HK Glyphs
        """
    )