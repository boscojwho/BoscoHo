import reflex as rx

from typing import Callable

from ..components import nav_bar
from ..components import sidebar
from ..components import sidebar_right
from ..components import layout_metrics as layout


def page(content: Callable[[], rx.Component]) -> rx.Component:
    """ Decorator for defining a page.

    This decorator embeds content in the middle column of a three-column layout with a navigation bar (adapts to display breakpoints).

    Apply this decorator to any `Reflex.Component` function that represents the content in the middle column (i.e. main content).
    """
    return rx.flex(
        nav_bar.navbar(),
        rx.flex(
            sidebar.sidebar(),
            rx.box(
                content(),
                margin_top=layout.margin_top_content,
                width=layout.width_content,
                height="100%",
            ),
            sidebar_right.sidebar_right(),
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
