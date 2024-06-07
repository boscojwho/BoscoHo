import reflex as rx

from reflex.style import toggle_color_mode
from ..components import layout_metrics as layout
from ..components import sidebar

def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            # home(),
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
        home_text(),
        href="/",
        width="100%",
    )

def home_text() -> rx.Component:
    return rx.hstack(
        rx.text(
            "bOSCO hO",
            font_family="Gluten",
            font_weight="800",
            font_size="80px",
            color="#000000"
        )
    )

def home_icon() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="/home_logo.png",
            height="120px",
            margin_top="8px",
            margin_left="8px"
        ),
        flex_direction="row",
        bg="transparent",
        align="start",
        # border_radius=styles.border_radius,
        width="100%",
        # padding="1em",
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
                color(),
                rx.popover.close(
                    rx.button("Close"),
                ),
                direction="column",
                spacing="3",
                width="240px"
            ),
            background=rx.color_mode_cond(light="#FEFCFB", dark="#1E160F")
        ),
        modal=True,
    )


button_style = {
    "border_radius": "50px",
    "border": f"1px solid {rx.color('mauve', 4)}",
    "background": rx.color('mauve', 2),
    "box_shadow": "0px 3px 7px -4px rgba(21, 18, 44, 0.15)",
    "padding": "7px 12px 7px 12px",
    "align_items": "center",
}


def color() -> rx.Component:
    return rx.flex(
            rx.color_mode.icon(
                light_component=rx.icon("sun", color=rx.color("mauve", 9)),
                dark_component=rx.icon("moon", color=rx.color("mauve", 9)),
            ),
            on_click=toggle_color_mode,
            _hover = {
                "cursor" : "pointer"
            },
            padding="7px",
            style=button_style,
            border_radius="8px",
        )