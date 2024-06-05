import reflex as rx

from .pages.about import about
from .pages.coding import coding
from .pages.index import index
from .pages.projects import projects

font_alfa_slab_one = "https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap"
font_luckiest_guy = "https://fonts.googleapis.com/css2?family=Luckiest+Guy&display=swap"
font_lilita_one = "https://fonts.googleapis.com/css2?family=Lilita+One&display=swap"
font_passion_one = "https://fonts.googleapis.com/css2?family=Passion+One:wght@400;700;900&display=swap"

class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="orange",
    ),
    stylesheets=[
        font_luckiest_guy,
    ],
)
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.add_page(coding, route="/coding")
app.add_page(projects, route="/projects")

from .blog import blog_post_1

app.add_page(blog_post_1.markdown, route="/blog/1")