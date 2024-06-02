import reflex as rx

@rx.page(
    route="/coding",
    title="Coding"
)
def coding() -> rx.Component:
    return rx.text("Coding")