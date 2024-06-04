import reflex as rx

from .pages.about import about
from .pages.coding import coding
from .pages.index import index
from .pages.projects import projects


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


app = rx.App(
    theme=rx.theme(
        appearance="inherit",
        has_background=True,
        radius="large",
        accent_color="orange",
    ),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap",
    ],
)
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.add_page(coding, route="/coding")
app.add_page(projects, route="/projects")
