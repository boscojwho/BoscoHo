import reflex as rx

from typing import Dict, List
from ..templates import template

# import OS module
import os


class BlogData(rx.State):
    blog_year: List[str] = [
        "2024",
    ]
    blog_data: Dict[str, List[Dict[str, str]]] = {
        "2024": [
            {
                "title": "Navigation Split View - 3 Columns",
                "href": "coding/blog_pages/1",
                "tags": [
                    "swift"
                ]
            },
        ],
    }


@template.page(
    route="/coding",
    title="Coding",
    show_sidebar_right=False
)
def coding() -> rx.Component:
    return blog_posts()


def display_year(year):
    return rx.section(
        rx.heading(year),
        rx.spacer(height="4px"),
        rx.vstack(
            rx.foreach(
                BlogData.blog_data[year],
                lambda x: rx.hstack(
                    rx.link(
                        x["title"],
                        href=x["href"]
                    ),
                    rx.foreach(
                        x["tags"],
                        lambda tag: rx.badge(tag),
                    )
                ),
            )
        ),
        size="1",
    )


def blog_year():
    return rx.vstack(
        blog_posts(),
        rx.foreach(
            BlogData.blog_year,
            display_year,
        ),
    )


import markdown

from ..blog_pages import blog_post


def blog_posts():
    # Get the list of all files and directories
    path = "./blog"
    dir_list = os.listdir(path)
    blogs = {}
    for post in dir_list:
        with open(f"./blog/{post}", 'r') as file:
            md = file.read()
            md_meta = markdown.Markdown(extensions=['meta'])
            md_meta.convert(md)

            if 'title' in md_meta.Meta:
                print("title", md_meta.Meta['title'])
                blogs[post] = md_meta.Meta["title"]
            else:
                print("Key 'title' not found in md_meta.Meta")
                blogs[post] = post
            # print("title", md_meta.Meta['title'])

    return rx.section(
        rx.heading("2024"),
        rx.spacer(height="8px"),
        rx.vstack(
            rx.foreach(
                blogs,
                post_link,
            )
        ),
        size="1",
    )

from typing import List, Dict


def post_link(post: List) -> rx.Component:
    return rx.link(
        rx.text(post[1]),
        href=f"/coding/blog/{post[0]}"
    )