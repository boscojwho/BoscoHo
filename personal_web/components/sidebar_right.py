import reflex as rx

from ..components import layout_metrics as layout


def sidebar_right() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.text("Item 1"),
            rx.text("Item 2"),
            rx.text("Item 3"),
            direction="column",
            width="100%",
            position="fixed",
            spacing="2",
            justify="start",
            # overflow="hidden",
            background_color="#87CEFA",
        ),
        margin_top=layout.margin_top_right_sidebar,
        width=layout.width_right_sidebar,
        height="100%",
        display=layout.display_right_sidebar,
        flex_shrink=0,
    )