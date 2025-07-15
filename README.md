# docteng - Document Templating Engine

A flexible Jinja2-based document and newsletter renderer that supports dynamic templating with JSON content.

## Installation

### Install from PyPI (when published)
```bash
pip install docteng
```

### Install for development
```bash
git clone <repository-url>
cd docteng
poetry install
```

## Usage

### As a Library

#### Basic Document Rendering
```python
from docteng import DocumentRenderer

# Initialize renderer with template directory
renderer = DocumentRenderer(template_dir="my_templates")

# Render with context data
context = {
    "title": "My Newsletter",
    "sections": [
        {"title": "News", "content": "Latest updates"},
        {"title": "Events", "content": "Upcoming events"}
    ]
}

html_output = renderer.render("newsletter.html", context)
print(html_output)
```

#### High-Level Newsletter Rendering
```python
from docteng import render_newsletter

# Render from JSON file
output_path = render_newsletter(
    template_file="newsletter_layout.html",
    json_file="content_samples/newsletter3.json",
    output_name="weekly_update",
    output_dir="output"
)
print(f"Newsletter saved to: {output_path}")
```

#### Render from Python Dictionary
```python
from docteng import render_from_context

context = {
    "title": "Weekly Newsletter",
    "hero": {
        "headline": "Welcome to Our Weekly Update!",
        "subheadline": "Stay informed with the latest news."
    },
    "sections": [
        {
            "title": "Top Stories",
            "layout": "row",
            "content": [
                {"title": "Story 1", "body": "Details of story 1"},
                {"title": "Story 2", "body": "Details of story 2"}
            ]
        }
    ]
}

output_path = render_from_context(
    template_file="newsletter_layout.html",
    context=context,
    output_name="custom_newsletter"
)
```

### Command Line Interface

After installation, you can use the `docteng` command:

```bash
# Basic usage
docteng newsletter_layout.html content_samples/newsletter3.json

# With custom output name
docteng newsletter_layout.html content_samples/newsletter3.json --name DailyBrewAt9

# With custom output directory
docteng newsletter_layout.html content_samples/newsletter3.json --output-dir my_output

# With custom template directory
docteng newsletter_layout.html content_samples/newsletter3.json --template-dir my_templates

# Show help
docteng --help
```

## Project Structure

```
docteng/
├── docteng/
│   ├── __init__.py          # Main package exports
│   ├── core.py              # Core DocumentRenderer class
│   ├── renderer.py          # High-level rendering functions
│   └── cli.py               # Command-line interface
├── templates/               # Jinja2 templates
│   ├── base.html
│   ├── newsletter_layout.html
│   └── partials/
├── content_samples/         # Example JSON content
├── output/                  # Generated output files
├── pyproject.toml          # Package configuration
└── README.md
```

## Template Structure

Templates use Jinja2 syntax and support nested includes:

```html
<!-- newsletter_layout.html -->
{% extends "base.html" %}

{% block content %}
    {% for section in sections %}
        <h2>{{ section.title }}</h2>
        
        {% if section.layout == "row" %}
            {% include "partials/row_section.html" %}
        {% elif section.layout == "two_column" %}
            {% include "partials/two_column_section.html" %}
        {% endif %}
    {% endfor %}
{% endblock %}
```

## JSON Content Format

```json
{
    "title": "Weekly Newsletter",
    "hero": {
        "headline": "Welcome to Our Weekly Update!",
        "subheadline": "Stay informed with the latest news."
    },
    "sections": [
        {
            "title": "Top Stories",
            "layout": "row",
            "content": [
                {"title": "Story 1", "body": "Details of story 1"}
            ]
        }
    ]
}
```

## Development

### Running Tests
```bash
poetry run pytest
```

### Code Formatting
```bash
poetry run black .
poetry run flake8 .
```

### Building Package
```bash
poetry build
```

## License

MIT License
