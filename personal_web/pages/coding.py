import reflex as rx

from ..templates import template
from ..blog import _2024_navigation_split_view

@template.page(
    route="/coding",
    title="Coding",
    show_sidebar_right=False
)
def coding() -> rx.Component:
    return rx.vstack(
        rx.section(
            rx.heading("2024"),
            rx.link(
                "Navigation Split View - 3 Columns",
                href="/"
            ),
            size="1",
            # padding_left="12px",
            # padding_right="12px",
            # background_color="var(--gray-2)",
        ),
    )
    # return rx.markdown(
    #     _2024_navigation_split_view.md,
    #     padding="12px"
    # )