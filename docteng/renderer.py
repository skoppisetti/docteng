"""
High-level rendering functions for document generation.
"""

import json
import os
import uuid
from pathlib import Path

from .core import DocumentRenderer


def generate_unique_name():
    """
    Generate a unique name using last 6 characters of UUID4.
    
    Returns:
        str: A 6-character unique identifier
    """
    return str(uuid.uuid4()).replace('-', '')[-6:]


def render_newsletter(template_file, json_file, output_name=None, output_dir="output", template_dir="templates"):
    """
    Render a newsletter with specified template and content.
    
    Args:
        template_file (str): Path to the template file (relative to template_dir)
        json_file (str): Path to the JSON content file
        output_name (str, optional): Name for the output file (without extension)
        output_dir (str): Directory to store the output file (default: "output")
        template_dir (str): Directory containing templates (default: "templates")
    
    Returns:
        str: Path to the generated output file
        
    Raises:
        FileNotFoundError: If JSON file or template is not found
        ValueError: If JSON is invalid or template rendering fails
        
    Example:
        >>> output_path = render_newsletter(
        ...     "newsletter.html", 
        ...     "content.json", 
        ...     output_name="weekly_update"
        ... )
        >>> print(f"Newsletter saved to: {output_path}")
    """
    # Initialize renderer
    renderer = DocumentRenderer(template_dir=template_dir)
    
    # Load JSON content
    try:
        with open(json_file, 'r') as f:
            content = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {json_file}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in file {json_file}: {e}")
    
    # Render the template
    try:
        html_output = renderer.render(template_file, content)
    except Exception as e:
        raise ValueError(f"Error rendering template {template_file}: {e}")
    
    # Generate output filename
    if output_name is None:
        output_name = f"newsletter_{generate_unique_name()}"
    
    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Generate output path
    output_path = os.path.join(output_dir, f"{output_name}.html")
    
    # Write output file
    with open(output_path, 'w') as f:
        f.write(html_output)
    
    return output_path


def render_from_context(template_file, context, output_name=None, output_dir="output", template_dir="templates"):
    """
    Render a document directly from a Python dictionary context.
    
    Args:
        template_file (str): Path to the template file (relative to template_dir)
        context (dict): Data to pass to the template
        output_name (str, optional): Name for the output file (without extension)
        output_dir (str): Directory to store the output file (default: "output")
        template_dir (str): Directory containing templates (default: "templates")
    
    Returns:
        str: Path to the generated output file
        
    Example:
        >>> context = {
        ...     "title": "My Newsletter",
        ...     "sections": [{"title": "News", "content": "Latest updates"}]
        ... }
        >>> output_path = render_from_context("newsletter.html", context)
    """
    # Initialize renderer
    renderer = DocumentRenderer(template_dir=template_dir)
    
    # Render the template
    try:
        html_output = renderer.render(template_file, context)
    except Exception as e:
        raise ValueError(f"Error rendering template {template_file}: {e}")
    
    # Generate output filename
    if output_name is None:
        output_name = f"document_{generate_unique_name()}"
    
    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Generate output path
    output_path = os.path.join(output_dir, f"{output_name}.html")
    
    # Write output file
    with open(output_path, 'w') as f:
        f.write(html_output)
    
    return output_path 