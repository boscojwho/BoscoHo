import reflex as rx

from ..components import layout_metrics as layout


def navbar() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.text("navbar"),
        ),
        width="100%",
        height=layout.height_navbar,
        display=layout.display_navbar,
        z_index="5",
        top="0px",
        position="fixed",
        align_items="center",
        direction="column",
        background_color="#AAAAAA",
    )