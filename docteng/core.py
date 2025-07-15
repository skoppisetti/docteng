"""
Core document rendering functionality using Jinja2 templates.
"""

from jinja2 import Environment, FileSystemLoader


class DocumentRenderer:
    """
    A document renderer that uses Jinja2 templates to generate documents
    from structured data.
    
    Example:
        >>> renderer = DocumentRenderer(template_dir="my_templates")
        >>> context = {"title": "My Document", "content": "Hello World"}
        >>> html = renderer.render("document.html", context)
    """
    
    def __init__(self, template_dir="templates"):
        """
        Initialize the document renderer.
        
        Args:
            template_dir (str): Directory containing Jinja2 templates
        """
        self.env = Environment(loader=FileSystemLoader(template_dir))
    
    def render(self, template_name, context):
        """
        Render a template with the given context.
        
        Args:
            template_name (str): Name of the template file
            context (dict): Data to pass to the template
            
        Returns:
            str: Rendered template as string
            
        Raises:
            jinja2.TemplateNotFound: If template file doesn't exist
            jinja2.TemplateSyntaxError: If template has syntax errors
        """
        template = self.env.get_template(template_name)
        return template.render(context) 