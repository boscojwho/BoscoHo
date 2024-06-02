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
        accent_color="teal",
    )
)
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.add_page(coding, route="/coding")
app.add_page(projects, route="/projects")
