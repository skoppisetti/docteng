"""
DocTeng - Document Templating Engine

A flexible Jinja2-based document and newsletter renderer that supports
dynamic templating with JSON content.
"""

from .core import DocumentRenderer
from .renderer import render_newsletter, render_from_context, generate_unique_name

__version__ = "0.1.0"
__all__ = ["DocumentRenderer", "render_newsletter", "render_from_context", "generate_unique_name"] 