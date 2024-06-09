import reflex as rx

from typing import Callable

from ..components import nav_bar
from ..components import sidebar
from ..components import sidebar_right
from ..components import layout_metrics as layout


def page(
        route: str,
        title: str,
        show_sidebar_right=True
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    print("@page", route)
    """ Decorator for defining a page.

    This decorator embeds content in the middle column of a three-column layout with a navigation bar (adapts to display breakpoints).

    Apply this decorator to any `Reflex.Component` function that represents the content in the middle column (i.e. main content).
    """

    # Python decorator with parameters pattern.
    # Need to move @rx.page decorator to the innermost function,
    # instead of applying it on each page,
    # otherwise decorator can't find passed-in content component.
    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        @rx.page(
            route=route,
            title=title,
        )
        def templated_page():
            return rx.flex(
                nav_bar.navbar(),
                rx.flex(
                    sidebar.sidebar(),
                    rx.box(
                        page_content(),
                        margin_top=layout.margin_top_content,
                        margin_bottom=layout.margin_bottom_content,
                        width=layout.width_content,
                        height="100%",
                    ),
                    sidebar_right.sidebar_right() if show_sidebar_right is True else rx.fragment(),
                    margin_left="20px",
                    margin_right="20px",
                    height="100%",
                    min_height="100vh",
                    width="100%",
                    spacing="4",
                ),
                justify="center",
                spacing="2",
                background_color=rx.color_mode_cond(light="#FAF9F6", dark="#0D0D0D")
            )

        return templated_page

    return decorator
