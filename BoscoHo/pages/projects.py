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
                    rx.chakra.image(src="", width="120px", height="auto", borderRadius="26.844"),
                    rx.text('Chinotto', weight="bold"),
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
        rx.chakra.responsive_grid(
            rx.link(
                rx.vstack(
                    rx.chakra.image(src="/fencathon_2_logo.png", width="44px", height="auto", borderRadius="9.8428"),
                    # rx.text('Fencathon', weight="bold"),
                    align="center"
                ),
                href="/"
            ),
            rx.link(
                rx.vstack(
                    rx.chakra.image(src="/fencathon_1_logo.png", width="44px", height="auto", borderRadius="9.8428"),
                    # rx.text('Fencathon', weight="bold"),
                    align="center"
                ),
                href="/"
            ),
            rx.link(
                rx.vstack(
                    rx.chakra.image(src="/atp_logo.png", width="44px", height="auto", borderRadius="9.8428"),
                    # rx.text('Fencathon', weight="bold"),
                    align="center"
                ),
                href="/"
            ),
            columns=[4],
            spacing="4",
        ),
        rx.text("Fencing", weight="bold"),
        rx.divider(),
        rx.chakra.responsive_grid(
            rx.link(
                rx.vstack(
                    rx.chakra.image(src="/rungo_icon_old.png", width="44px", height="auto", borderRadius="9.8428"),
                    rx.chakra.image(src="/rungo_icon_new.png", width="44px", height="auto"),
                    # rx.text('Fencathon', weight="bold"),
                    align="center"
                ),
                href="/"
            ),
            columns=[4],
            spacing="4",
        ),
    )
    # return rx.vstack(
    #     rx.chakra.card(
    #         rx.chakra.image(
    #             src="/hkscs_icon.png", width="100px", height="auto"
    #         )
    #     )
    # )