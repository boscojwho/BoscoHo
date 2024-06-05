import reflex as rx
from ..templates import template


@template.page(
    route="/blog/1",
    title="Navigation Split View - 3 Columns",
    show_sidebar_right=False
)
def markdown() -> rx.Component:
    return rx.markdown(
        r"""
        # Navigation Split View - 3 Columns

        For some reason, using split view’s three column API doesn’t work as expected on iPhone (compact size) when using non-List views. There is a workaround. [2024.04]

        ```swift
        /// This works
        NavigationSplitView {
            sidebar
        } content: {
            List(selection...) {
                ...
            }
        } detail: {
            detail...
        }

        /// This doesn't
        NavigationSplitView {
            sidebar
        } content: {
            CustomView... (e.g. LazyVGrid)
        } detail: {
            detail...
        }
        ```

        Turns out, you can just use `NavigationLink` and `NavigationStack` in a two-column setup, and still have it show in three columns in regular size. The system will collapse the views into a `NavigationStack` in compact size.

        ```swift
        /// Workaround
        NavigationSplitView {
            sidebar
        } content: {
            NavigationStack {
                CustomNonListView... (e.g. LazyVGrid) {
                    NavigationLink...
                }
            }
            .navigationDestination(...) {
                DetailView...
            }
        } detail: {
            if selection == nil {
                ContentUnavailableView...
            }
        }
        ```

        For this to work, you still need to use the three-column API, otherwise the system will complain that there is no next column on which to present a detail view.
        """,
        padding="12px"
    )