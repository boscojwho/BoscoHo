import reflex as rx
from ..templates import template


@template.page(
    route="/projects",
    title="Projects",
    show_sidebar_right=False
)
def projects() -> rx.Component:
    return rx.vstack(
        rx.chakra.responsive_grid(
            rx.link(
                rx.vstack(
                    # width * 0.2237
                    rx.chakra.image(src="/hkscs_icon.png", width="120px", height="auto", borderRadius="26.844"),
                    rx.text('HK Characters', weight="bold"),
                    align="center"
                ),
                href="/"
            ),
            rx.link(
                rx.vstack(
                    rx.chakra.image(src="/castro_icon.png", width="120px", height="auto", borderRadius="26.844"),
                    rx.text('Castro', weight="bold"),
                    align="center"
                ),
                href="/"
            ),
            columns=[2, 3, 4],
            spacing="6",
        ),
        rx.divider(),
        rx.vstack(
            rx.text("Open Source Contributor", weight="medium"),
            rx.link(
                rx.vstack(
                    rx.chakra.image(src="/mlem_logo.png", width="60px", height="auto", borderRadius="13.422"),
                    rx.text('Mlem', weight="bold"),
                    align="center"
                )
            )
        ),
        rx.divider(),
        rx.text("Fencing"),
        rx.text("RunGo"),
    )
    # return rx.vstack(
    #     rx.chakra.card(
    #         rx.chakra.image(
    #             src="/hkscs_icon.png", width="100px", height="auto"
    #         )
    #     )
    # )