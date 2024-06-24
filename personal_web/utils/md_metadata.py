import markdown
from typing import Dict
def md_metadata(md: str) -> Dict:
    """
    Returns Markdown metadata defined at top of .md file as a dictionary.
    """
    md_meta = markdown.Markdown(extensions=['meta'])
    md_meta.convert(md)
    return md_meta.Meta