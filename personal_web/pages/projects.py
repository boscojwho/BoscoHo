import reflex as rx

@rx.page(
    route="/projects",
    title="Projects"
)
def projects() -> rx.Component:
    return rx.text("Projects")