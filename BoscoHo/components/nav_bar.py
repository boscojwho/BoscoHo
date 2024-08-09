import reflex as rx

from reflex.style import toggle_color_mode
from ..components import layout_metrics as layout
from ..components import sidebar

from BoscoHo import styles

def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            home(),
            rx.spacer(),
            menu(),
            width="100%",
            align="center",
            margin_left="20px",
            margin_right="20px",
            margin_bottom="20px",
        ),
        width="100%",
        height=layout.height_navbar,
        display=layout.display_navbar,
        z_index="5",
        top="0px",
        position="fixed",
        align_items="center",
        direction="column",
        style={
            "backgroundColor": rx.color_mode_cond(light="rgba(250, 249, 246, 1)", dark="rgba(13, 13, 13, 0.8)"),
            "backdropFilter": "blur(4px)"
        }
    )

def home() -> rx.Component:
    # Whether the item is active.
    url = "/"
    active = False
    # active = (
    #         (rx.State.router.page.path == url.lower())
    #         | (rx.State.router.page.path == "/")
    # )
    return rx.link(
        rx.vstack(
            sidebar_home_first_name("bOSCO"),
            sidebar_home_last_name("hO"),
            spacing="0",
            margin_top="24px",
            color=rx.cond(
                active,
                rx.color("ruby", 10),
                styles.text_color,
            ),
        ),
        href="/",
        underline="none",
    )


def sidebar_home_first_name(text: str) -> rx.Component:
    return rx.text(
        text,
        text_align="right",
        # text_shadow="2px 2px #ff0000",
        font_family="Gluten",
        font_weight="800",
        font_size="36px",
        font_variation_settings="'slnt' 0",
        letter_spacing="-2px",
        color=styles.accent_text_color,
        line_height="0.8",
        width="100%",
        _hover={"color": "red"},
    )


def sidebar_home_last_name(text: str) -> rx.Component:
    return rx.text(
        text,
        text_align="right",
        # text_shadow="2px 2px #ff0000",
        font_family="Gluten",
        font_weight="800",
        font_size="36px",
        font_variation_settings="'slnt' 0",
        letter_spacing="-2px",
        color=styles.accent_text_color,
        line_height="0.8",
        width="100%",
        _hover={"color": "red"},
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
                # color(),
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