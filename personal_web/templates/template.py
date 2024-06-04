from typing import Callable
from ..examples import __columns_with_nav_bar
from ..components import sidebar
import reflex as rx


margin_top_content = ["80px", "80px", "80px", "80px", "0px", "0px"]
width_content = ["100%", "100%", "100%", "75%", "58%", "58%"]


def page(content: Callable[[], rx.Component]) -> rx.Component:
    """ Decorator for defining a page.

    This decorator embeds content in the middle column of a three-column layout with a navigation bar (adapts to display breakpoints).

    Apply this decorator to any `Reflex.Component` function that represents the content in the middle column (i.e. main content).
    """
    return rx.flex(
        __columns_with_nav_bar.navbar(),
        rx.flex(
            sidebar.sidebar(),
            rx.box(
                content(),
                margin_top=margin_top_content,
                width=width_content,
                height="100%",
                background_color="#EEEEEE",
            ),
            __columns_with_nav_bar.right_sidebar(),
            margin_left="20px",
            margin_right="20px",
            margin_top="8px",
            height="100%",
            min_height="100vh",
            width="100%",
            spacing="4",
        ),
        justify="center",
        spacing="2"
    )
