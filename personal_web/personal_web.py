import reflex as rx

from .pages.about import about
from .pages.coding import coding
from .pages.index import index
from .pages.projects import projects
from .blog_pages import blog_post

font_alfa_slab_one = "https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap"
font_luckiest_guy = "https://fonts.googleapis.com/css2?family=Luckiest+Guy&display=swap"
font_lilita_one = "https://fonts.googleapis.com/css2?family=Lilita+One&display=swap"
font_passion_one = "https://fonts.googleapis.com/css2?family=Passion+One:wght@400;700;900&display=swap"
font_gluten = "https://fonts.googleapis.com/css2?family=Gluten:slnt,wght@-13..13,100..900&display=swap"

class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        # accent_color="orange",
    ),
    stylesheets=[
        font_gluten,
    ],
)
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.add_page(coding, route="/coding")
app.add_page(projects, route="/projects")

from .blog_pages import blog_post_1
import os

path = "./blog"
dir_list = os.listdir(path)

from .templates import template

for post in dir_list:
    # See reflex-web/pcweb/pages/blog/blog.py
    # This is how we can pass props into a rx.component.
    template.page(route=f"/coding/blog/{post}", title="Blog Post", show_sidebar_right=False)(
        # Must pass `() -> rx.Component`, hence lambda function here.
        # Need to bind post to lambda function, otherwise value is incorrect (not sure why, some Python thing for sure).
        lambda p=post: blog_post.blog_post(p)
    )
    # app.add_page(blog_post.blog_post, route=f"/coding/blog/{post}")

app.add_page(blog_post_1.markdown, route="/coding/blog_pages/1")