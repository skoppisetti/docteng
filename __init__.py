# For backward compatibility, re-export the main classes
from docteng import DocumentRenderer, render_newsletter, render_from_context, generate_unique_name

__all__ = ["DocumentRenderer", "render_newsletter", "render_from_context", "generate_unique_name"]
