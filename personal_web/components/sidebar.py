from personal_web import styles
from ..components import layout_metrics as layout
import reflex as rx


def sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            # sidebar_header_item("Home", "/"),
            sidebar_item("Coding", "/coding"),
            sidebar_item("Projects", "/projects"),
            sidebar_item("About", "/about"),
            direction="column",
            position="fixed",
            # spacing="2",
            width="24%",
        ),
        margin_top=layout.margin_top_sidebar,
        width=layout.width_sidebar,
        height="100%",
        display=layout.display_sidebar,
        flex_shrink=0,
    )


def sidebar_header_item(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.text(
                text,
            ),
            bg="transparent",
            align="center",
            # border_radius=styles.border_radius,
            width="100%",
            # padding="1em",
        ),
        href=url,
        width="100%",
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
    active = (rx.State.router.page.path == url.lower()) | (
            (rx.State.router.page.path == "/") & text == "Home"
    )

    return rx.link(
        rx.hstack(
            rx.text(
                text,
                bg=rx.cond(
                    active,
                    rx.color("accent", 2),
                    "transparent",
                ),
                padding="8px",
                border_radius="4px"
            ),

            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            # size="8",
            align="center",
            # border_radius=styles.border_radius,
            width="100%",
            # padding="1em",
        ),
        weight=rx.cond(
            active,
            "bold",
            "medium"
        ),
        href=url,
        width="100%",
    )
