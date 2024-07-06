import reflex as rx
from ..templates import template


@template.page(
    route="/projects/hk_characters",
    title="HK Characters",
    show_sidebar_right=False
)
def index() -> rx.Component:
    return rx.flex(
        rx.card(
            rx.flex(
                rx.chakra.image(src="/hkscs_icon.png", width="120px", height="auto", borderRadius="26.844"),
                rx.vstack(
                    rx.text("HK Characters", size="8", weight="bold", trim="both",),
                    rx.text("Explore Hong Kong words.", size="5", weight="medium", trim="both",)
                ),
                margin="2px",
                spacing="4",
                align_items="flex-start",
                flex_wrap="wrap",
            ),
            variant="classic",
        ),
        rx.chakra.image(src="/hkscs_landscape.png", width="320px", height="auto", borderRadius="24"),
        hkscs_metadata(),
        collections(),
        glyph_variants(),
        voice_to_speech(),
        search(),
        unihan_metadata(),
        rx.divider(),
        rx.link(
            rx.text("Privacy Policy"),
            href="/privacy/file/hkscs.md"
        ),
        margin="8px",
        spacing="4",
        align_items = "flex-start",
        flex_wrap = "wrap",
    )


def collections():
    return rx.card(
        rx.flex(
            rx.vstack(
                rx.text("Collections", size="6", weight="bold"),
                rx.text(
                    "Browse and discover characters in conveniently grouped collections, including \'Tang\' (characters with Tang-era pronunciations available), \'Commonly Used\', and \'Vietnamese\'."
                ),
                rx.text(
                    "View characters by the year added to the Hong Kong Supplementary Character Set."
                ),
                rx.chakra.image(src="/hkscs/hkscs_collections_canto.png",
                                height="auto",
                                borderRadius="8"),
                width=["100%", "100%", "48%", "48%", "48%"],
            ),
            rx.chakra.image(src="/hkscs/hkscs_collections.png",
                            width="48%",
                            height="auto",
                            borderRadius="8"),
            spacing="4",
            align_items="flex-start",
            flex_wrap="wrap",
        ),
        size="1"
    )


def glyph_variants():
    return rx.card(
        rx.flex(
            rx.vstack(
                rx.text("Glyph Variants", size="6", weight="bold"),
                rx.text(
                    "See how a single character can be written in various glyph variants, some of which may commonly used in a specific country."
                ),
                rx.chakra.image(src="/hkscs/hkscs_glyph_variants_font.png",
                                height="auto",
                                borderRadius="8"),
                width=["100%", "100%", "48%", "48%", "48%"],
            ),
            rx.chakra.image(src="/hkscs/hkscs_glyph_variants.png",
                            width="48%",
                            height="auto",
                            borderRadius="8"),
            spacing="4",
            align_items="flex-start",
            flex_wrap="wrap",
        ),
        size="1"
    )

def voice_to_speech():
    return rx.card(
        rx.flex(
            rx.vstack(
                rx.text("Voice to Speech", size="6", weight="bold"),
                rx.text(
                    "Hear and compare how the same character can be read in Cantonese, Korean, Japanese, Taiwanese, and Mandarin."
                ),
                rx.chakra.image(src="/hkscs/hkscs_metadata_canto.png",
                                height="auto",
                                borderRadius="8"),
                width=["100%", "100%", "48%", "48%", "48%"],
            ),
            rx.chakra.image(src="/hkscs/hkscs_speech_view.png",
                            width="48%",
                            height="auto",
                            borderRadius="8"),
            spacing="4",
            align_items="flex-start",
            flex_wrap="wrap",
        ),
        size="1"
    )

def search():
    return rx.card(
        rx.flex(
            rx.vstack(
                rx.text("Search", size="6", weight="bold"),
                rx.text(
                    "Look for words by definition, Jyutping, Unicode codepoint."
                ),
                rx.chakra.image(src="/hkscs/hkscs_search_definition.png",
                                height="auto",
                                borderRadius="8"),
                width=["100%", "100%", "48%", "48%", "48%"]
            ),
            rx.vstack(
                rx.chakra.image(src="/hkscs/hkscs_search_jyutping.png",
                                height="auto",
                                borderRadius="8"),
                rx.chakra.image(src="/hkscs/hkscs_search_codepoint.png",
                                height="auto",
                                borderRadius="8"),
                align="center",
                width=["100%", "100%", "48%", "48%", "48%"],
            ),
            spacing="4",
            align_items="flex-start",
            flex_wrap="wrap",
        ),
        size="1"
    )


def unihan_metadata():
    return rx.card(
        rx.flex(
            rx.vstack(
                rx.text("Unihan Metadata", size="6", weight="bold"),
                rx.text(
                    "View a character’s associated Unihan database metadata, if available."
                ),
                rx.text(
                    "Unihan metadata is provided by Unicode."
                ),
                width=["100%", "100%", "48%", "48%", "48%"]
            ),
            rx.chakra.image(src="/hkscs/hkscs_unihan_metadata.png", width="48%",
                            height="auto",
                            borderRadius="8"),
            spacing="4",
            align_items="flex-start",
            flex_wrap="wrap",
        ),
        size="1"
    )


def hkscs_metadata():
    return rx.card(
        rx.flex(
            rx.vstack(
                rx.text("Hong Kong Supplementary Character Set (HKSCS)", size="6", weight="bold"),
                rx.text(
                    "Realizing the inherent differences between written Chinese and written Cantonese, the Government of Hong Kong initially created the Hong Kong Supplementary Character Set in 1995 to streamline electronic communications in Hong Kong. New characters have been added to the character set in subsequent years."
                ),
                rx.markdown(
                    "[Learn more...](https://www.ccli.gov.hk/en/hkscs/what_is_hkscs.html)"
                ),
                width=["100%", "100%", "48%", "48%", "48%"]
            ),
            rx.chakra.image(src="/hkscs/hkscs_metadata.png", width="48%", height="auto",
                            borderRadius="8"),
            spacing="4",
            align_items="flex-start",
            flex_wrap="wrap",
        ),
        size="1"
    )
