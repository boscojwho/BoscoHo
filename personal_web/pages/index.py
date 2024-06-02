import reflex as rx

import personal_web.components.sidebar as sidebar

from personal_web import styles

@rx.page(
    route="/",
    title="Home"
)
def index() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.hstack(
                rx.text("navbar"),
            ),
            width="100%",
            height="80px",
            z_index="5",
            top="0px",
            position="fixed",
            align_items="center",
            direction="column",
            background_color="#AAAAAA",
        ),
        rx.flex(
            rx.box(
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
                margin_top="80px",
                width="24%",
                height="100%",
                display=["none", "none", "none", "none", "flex", "flex"],
                flex_shrink=0,
            ),
            rx.box(
                rx.vstack(
                    rx.text("content"),
                    height="1000em"
                ),
                margin_top="80px",
                width=["100%", "100%", "100%", "66%", "58%", "58%"],  # if right_sidebar else "100%",
                height="100%",
                background_color="#EEEEEE",
            ),
            rx.box(
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
                margin_top="80px",
                width="18%",
                height="100%",
                display=["none", "none", "none", "flex", "flex", "flex"],  # if right_sidebar else "none",
                flex_shrink=0,
            ),
            # max_width="110em",
            margin_left="20px",
            margin_right="20px",
            margin_top="8px",
            height="100%",
            min_height="100vh",
            width="100%",
            spacing="4",
        ),
        justify="center",
        spacing="2"
    )
    # Welcome Page (Index)
    # return rx.hstack(
    #     # Sidebar
    #     rx.box(
    #         sidebar.sidebar(),
    #         rx.box(
    #             rx.menu.root(
    #                 rx.menu.trigger(
    #                     rx.button(
    #                         rx.icon("menu"),
    #                         variant="soft",
    #                     )
    #                 ),
    #                 rx.menu.content(
    #                     menu_item_link("Coding", "/coding"),
    #                     menu_item_link("Projects", "/projects"),
    #                     menu_item_link("About", "/about")
    #                 )
    #             ),
    #             leading="2em",
    #             top="2em",
    #             z_index="500",
    #             display=["flex", "flex", "none", "none", "none"],
    #         )
    #     ),
    #     # Main content
    #     rx.text("Home")
    # )
def menu_item_link(text, href):
    return rx.menu.item(
        rx.link(
            text,
            href=href,
            width="100%",
            color="inherit",
        ),
        _hover={
            "color": styles.accent_color,
            "background_color": styles.accent_text_color,
        },
    )