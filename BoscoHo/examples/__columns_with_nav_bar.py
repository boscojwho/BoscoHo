import reflex as rx

height_navbar = ["80px", "80px", "80px", "80px", "0px", "0px"]

display_navbar = ["flex", "flex", "flex", "flex", "none", "none"]
display_sidebar = ["none", "none", "none", "none", "flex", "flex"]
display_right_sidebar = ["none", "none", "none", "flex", "flex", "flex"]

margin_top_sidebar = ["80px", "80px", "80px", "80px", "0px", "0px"]
margin_top_content = ["80px", "80px", "80px", "80px", "0px", "0px"]
margin_top_right_sidebar = ["80px", "80px", "80px", "80px", "0px", "0px"]

width_sidebar = ["0%", "0%", "0%", "0%", "24%", "24%"]
width_content = ["100%", "100%", "100%", "75%", "58%", "58%"]
width_right_sidebar = ["0%", "0%", "0%", "25%", "18%", "18%"]


@rx.page(
    route="/",
    title="Home"
)
def index() -> rx.Component:
    return rx.flex(
        navbar(),
        columns(),
        justify="center",
        spacing="2"
    )


def columns() -> rx.Component:
    return rx.flex(
        sidebar(),
        main_content(),
        right_sidebar(),
        # max_width="110em",
        margin_left="20px",
        margin_right="20px",
        margin_top="8px",
        height="100%",
        min_height="100vh",
        width="100%",
        spacing="4",
    )


def main_content() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("content"),
            height="1000em"
        ),
        margin_top=margin_top_content,
        width=width_content,
        height="100%",
        background_color="#EEEEEE",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.hstack(
                rx.spacer(),
                rx.text("Sidebar item 1"),
                width="100%",
            ),
            rx.hstack(
                rx.spacer(),
                rx.text("Sidebar item 2"),
                width="100%",
            ),
            rx.hstack(
                rx.spacer(),
                rx.text("Sidebar item 3"),
                width="100%",
            ),
            direction="column",
            position="fixed",
            spacing="2",
            # overflow="hidden",
            background_color="#87CEFA",
            width="24%"
        ),
        margin_top=margin_top_sidebar,
        width=width_sidebar,
        height="100%",
        display=display_sidebar,
        flex_shrink=0,
    )


def right_sidebar() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.text("Item 1"),
            rx.text("Item 2"),
            rx.text("Item 3"),
            direction="column",
            width="100%",
            position="fixed",
            spacing="2",
            justify="start",
            # overflow="hidden",
            background_color="#87CEFA",
        ),
        margin_top=margin_top_right_sidebar,
        width=width_right_sidebar,
        height="100%",
        display=display_right_sidebar,
        flex_shrink=0,
    )


def navbar() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.text("navbar"),
        ),
        width="100%",
        height=height_navbar,
        display=display_navbar,
        z_index="5",
        top="0px",
        position="fixed",
        align_items="center",
        direction="column",
        background_color="#AAAAAA",
    )
