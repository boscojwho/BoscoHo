from BoscoHo import styles
from ..components import layout_metrics as layout
import reflex as rx


def sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            sidebar_home(),
            # Adds space between nav bar home icon and first sidebar item.
            rx.box(
              height="32px"
            ),
            sidebar_item("Coding", "/coding"),
            rx.chakra.wrap(
                rx.chakra.wrap_item(
                    sidebar_item_small("Swift/Apple"),
                ),
                rx.chakra.wrap_item(
                    sidebar_item_small("Python"),
                ),
                rx.chakra.wrap_item(
                    sidebar_item_small("Web"),
                ),
                rx.chakra.wrap_item(
                    sidebar_item_small("Blog/RSS"),
                ),
                spacing_x="0.85em",
                align="center",
            ),
            sidebar_item("Projects", "/projects"),
            rx.chakra.wrap(
                rx.chakra.wrap_item(
                    sidebar_item_small("HK Glyph"),
                ),
                rx.chakra.wrap_item(
                    sidebar_item_small("Chinotto"),
                ),
                rx.chakra.wrap_item(
                    sidebar_item_small("Castro"),
                ),
                rx.chakra.wrap_item(
                    sidebar_item_small("Open Source"),
                ),
                rx.chakra.wrap_item(
                    sidebar_item_small("Past Projects"),
                ),
                spacing_x="0.85em",
                align="center",
            ),
            sidebar_item("About", "/about"),
            rx.hstack(
                sidebar_icon_small("mail"),
                sidebar_icon_small("message-circle-heart"),
                sidebar_icon_small("rss"),
            ),
            direction="column",
            position="fixed",
            spacing="2",
            width=layout.width_sidebar,
        ),
        margin_top=layout.margin_top_sidebar,
        width=layout.width_sidebar,
        height="100%",
        display=layout.display_sidebar,
        flex_shrink=0,
    )


def sidebar_home() -> rx.Component:
    # Whether the item is active.
    url = "/"
    active = False
    # (
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
        font_size="80px",
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
        font_size="60px",
        font_variation_settings="'slnt' 0",
        letter_spacing="-2px",
        color=styles.accent_text_color,
        line_height="0.8",
        width="100%",
        _hover={"color": "red"},
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
    active = False
    # active = (
    #         (rx.State.router.page.path == url.lower())
    #         # | (rx.State.router.page.path.find(url.lower()) != -1)
    #         | ((rx.State.router.page.path == "/") & text == "Home")
    # )

    return rx.link(
        rx.hstack(
            rx.text(
                text.upper(),
                font_family=styles.FONT_FAMILY,
                font_weight="600",
                font_size="2em",
                font_variation_settings="'slnt' 0",
                border_radius="4px",
                line_height="0.8",
                _hover={"color": "red"},
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
        width=layout.width_sidebar,
        underline="none",
        margin_top="4px",
        margin_bottom="-6px",
    )


def sidebar_item_small(text: str) -> rx.Component:
    return rx.text(
        text.lower(),
        font_family=styles.FONT_FAMILY,
        font_weight="300",
        font_size="1.1em",
        font_variation_settings="'slnt' 0",
        line_height="0.9",
    )


def sidebar_icon_small(icon: str) -> rx.Component:
    return rx.flex(
        rx.icon(icon, size=15)
    )