import reflex as rx

from personal_web.templates import template


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
def blog_post(post: str) -> rx.Component:
    # return rx.text(f"Title: {post}")
    print("render ", post)
    with open(f"./blog/{post}", 'r') as file:
        md = file.read()
    return rx.markdown(md)
