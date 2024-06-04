import reflex as rx

from ..components import layout_metrics as layout


def navbar() -> rx.Component:
    return rx.flex(
        rx.hstack(
            home()
        ),
        width="100%",
        height=layout.height_navbar,
        display=layout.display_navbar,
        z_index="5",
        top="0px",
        position="fixed",
        align_items="center",
        direction="column",
        # background_color="#AAAAAA",
    )


def home() -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.text(
                "Home",
            ),
            bg="transparent",
            align="center",
            # border_radius=styles.border_radius,
            width="100%",
            # padding="1em",
        ),
        href="/",
        width="100%",
    )