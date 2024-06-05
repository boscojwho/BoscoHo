# import reflex as rx
#
# from personal_web.templates import template
#
#
# class BlogState(rx.State):
#     md: str
#     @rx.var
#     def blog_post_name(self) -> str:
#         # Access URL parameters directly
#         return self.router.page.params.get('blog_post_name', '')
#
#
# @template.page(
#     route="/coding/blog_post/[blog_post_name]",
#     title="Blog Post",
#     show_sidebar_right=False
# )
# def blog_post() -> rx.Component:
#     with open(f"../blog/_{BlogState.blog_post_name}.md", 'r') as file:
#         BlogState.md = file.read()
#     return rx.markdown(BlogState.md)
