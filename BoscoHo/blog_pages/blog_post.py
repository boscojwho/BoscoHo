import reflex as rx
import re
import markdown

from BoscoHo.templates import template


# class BlogState(rx.State):
#     name: str
#     md: str
#
#     @rx.var
#     def blog_post_name(self):
#         # Access URL parameters directly
#         x = self.router.page.params.get('post_name', '')
#         print("blog_post_name", x)
#         self.name = x


# @template.page(
#     route="/coding/blog/[post_name]",
#     title="Blog Post",
#     show_sidebar_right=False
# )

component_map = {
    "blockquote": lambda text: rx.card(
        text,
        size="1",
        background_color="var(--blue-2)",
    )
}


def blog_post(post: str) -> rx.Component:
    with open(f"./blog/{post}", 'r') as file:
        md = file.read()
        # Manually strip metadata section:
        # Remove everything between the first and last "---" (inclusive)
        cleaned_content = re.sub(r"(^|\n)---(.*?)\n---", "", md, flags=re.DOTALL)

        # md_meta = markdown.Markdown(extensions=['meta'])
        # html = md_meta.convert(md)
        # print(html)

    return rx.markdown(
        cleaned_content,
        margin_left="20px",
        margin_right="20px",
        component_map=component_map
    )
