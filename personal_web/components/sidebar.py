from personal_web import styles

import reflex as rx

def sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            sidebar_item("Coding", "/coding"),
            sidebar_item("Projects", "/projects"),
            sidebar_item("About", "/about"),
        ),
        display=["none", "none", "flex", "flex", "flex"],
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
            ),
            bg=rx.cond(
                active,
                rx.color("accent", 2),
                "transparent",
            ),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            align="center",
            # border_radius=styles.border_radius,
            width="100%",
            # padding="1em",
        ),
        href=url,
        width="100%",
    )