import reflex as rx

from ..components import layout_metrics as layout
from ..components import sidebar

def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            home(),
            rx.spacer(),
            menu(),
            width="100%",
            align="center",
            margin_right="20px"
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
            rx.image(
                src="/home_logo.png",
                height="80px",
            ),
            flex_direction="row",
            bg="transparent",
            align="start",
            # border_radius=styles.border_radius,
            width="100%",
            # padding="1em",
        ),
        href="/",
        width="100%",
    )

def menu() -> rx.Component:
    return rx.popover.root(
        rx.popover.trigger(
            rx.button(
                rx.icon(tag="menu")
            ),
        ),
        rx.popover.content(
            rx.flex(
                sidebar.sidebar_item("Coding", "/coding"),
                sidebar.sidebar_item("Projects", "/projects"),
                sidebar.sidebar_item("About", "/about"),
                rx.popover.close(
                    rx.button("Close"),
                ),
                direction="column",
                spacing="3",
                width="240px"
            ),
        ),
        modal=True,
    )