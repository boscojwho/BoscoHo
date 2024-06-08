from personal_web import styles
from ..components import layout_metrics as layout
import reflex as rx


def sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.vstack(
                rx.text(
                    "bOSCO",
                    text_align="right",
                    # text_shadow="2px 2px #ff0000",
                    font_family="Gluten",
                    font_weight="800",
                    font_size="80px",
                    letter_spacing="-2px",
                    color=styles.accent_text_color,
                    line_height="0.8",
                    width="100%",
                ),
                rx.text(
                    "hO",
                    text_align="right",
                    # text_shadow="2px 2px #ff0000",
                    font_family="Gluten",
                    font_weight="800",
                    font_size="60px",
                    letter_spacing="-2px",
                    color=styles.accent_text_color,
                    line_height="0.8",
                    width="100%",
                ),
                spacing="0",
                margin_top="24px",
            ),
            # Adds space between nav bar home icon and first sidebar item.
            rx.box(
              height="32px"
            ),
            sidebar_item("Coding", "/coding"),
            rx.hstack(
                sidebar_item_small("Swift"),
                sidebar_item_small("Python"),
                sidebar_item_small("Web"),
            ),
            sidebar_item("Projects", "/projects"),
            rx.hstack(
                sidebar_item_small("HK Glyph"),
            ),
            sidebar_item("About", "/about"),
            rx.hstack(
                sidebar_item_small("Contact"),
            ),
            direction="column",
            position="fixed",
            spacing="1",
            # width="34%",
        ),
        margin_top=layout.margin_top_sidebar,
        width=layout.width_sidebar,
        height="100%",
        display=layout.display_sidebar,
        flex_shrink=0,
    )


def sidebar_item(text: str, url: str) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (
            (rx.State.router.page.path == url.lower())
            # | (rx.State.router.page.path.find(url.lower()) != -1)
            | ((rx.State.router.page.path == "/") & text == "Home")
    )

    return rx.link(
        rx.hstack(
            rx.text(
                text.upper(),
                font_family=styles.FONT_FAMILY,
                font_weight="600",
                font_size="2em",
                border_radius="4px",
                line_height="0.8",
                _hover={"color": "red"}
            ),

            color=rx.cond(
                active,
                rx.color("ruby", 10),
                styles.text_color,
            ),
            align="center",
            width="100%",
        ),
        # weight=rx.cond(
        #     active,
        #     "bold",
        #     "medium"
        # ),
        href=url,
        width="100%",
        underline="none"
    )


def sidebar_item_small(text: str) -> rx.Component:
    return rx.text(
        text.lower(),
        font_family=styles.FONT_FAMILY,
        font_weight="300",
        font_size="1em",
        line_height="0.9",
    )