import reflex as rx

from typing import List, Dict


class BlogData(rx.State):
    blog_year: [str] = [
        "2024",
        "2023",
        "2022"
    ]
    blog_data: Dict[str, List[Dict[str, str]]] = {
        "2024": [
            {"title": "Navigation Split View - 3 Columns", "href": "/"},
            {"title": "Untitled 2", "href": "/"},
            {"title": "Untitled 3", "href": "/"},
        ],
        "2023": [
            {"title": "Untitled 1", "href": "/"},
            {"title": "Untitled 2", "href": "/"},
            {"title": "Untitled 3", "href": "/"},
        ],
        "2022": [
            {"title": "Untitled 1", "href": "/"},
            {"title": "Untitled 2", "href": "/"},
            {"title": "Untitled 3", "href": "/"},
        ],
    }
