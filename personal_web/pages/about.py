import reflex as rx

@rx.page(
    route="/about",
    title="About"
)
def about() -> rx.Component:
    return rx.text("About")