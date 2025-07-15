#!/usr/bin/env python3
"""
Example usage of the DocTeng library.

This script demonstrates different ways to use the DocTeng library
for document and newsletter generation.
"""

from docteng import DocumentRenderer, render_newsletter, render_from_context

def example_basic_rendering():
    """Example of basic document rendering using DocumentRenderer class."""
    print("=== Basic Document Rendering ===")
    
    # Initialize renderer
    renderer = DocumentRenderer(template_dir="templates")
    
    # Create context data
    context = {
        "title": "My Custom Newsletter",
        "hero": {
            "headline": "Welcome to Basic Rendering!",
            "subheadline": "This is generated programmatically."
        },
        "sections": [
            {
                "title": "Programming News",
                "layout": "row",
                "content": [
                    {"title": "Python 3.12 Released", "body": "New features and improvements"},
                    {"title": "DocTeng Library", "body": "A new templating engine for documents"}
                ]
            },
            {
                "title": "Resources",
                "layout": "two_column",
                "content": [
                    {"title": "Documentation", "body": "Read the docs for more info"},
                    {"title": "Examples", "body": "Check out usage examples"}
                ]
            }
        ]
    }
    
    # Render the template
    html_output = renderer.render("newsletter_layout.html", context)
    
    # Save to file
    with open("output/basic_example.html", "w") as f:
        f.write(html_output)
    
    print("✓ Basic rendering complete: output/basic_example.html")


def example_json_rendering():
    """Example of rendering from JSON file."""
    print("\n=== JSON File Rendering ===")
    
    # Render from existing JSON file
    output_path = render_newsletter(
        template_file="newsletter_layout.html",
        json_file="content_samples/newsletter3.json",
        output_name="json_example",
        output_dir="output"
    )
    
    print(f"✓ JSON rendering complete: {output_path}")


def example_context_rendering():
    """Example of rendering from Python dictionary context."""
    print("\n=== Context Dictionary Rendering ===")
    
    # Create context directly in Python
    context = {
        "title": "Developer Weekly",
        "hero": {
            "headline": "Latest in Software Development",
            "subheadline": "Weekly roundup of programming news and tutorials"
        },
        "sections": [
            {
                "title": "Featured Articles",
                "layout": "two_column",
                "content": [
                    {
                        "title": "Best Practices in Python",
                        "body": "Learn advanced Python patterns and techniques for cleaner code"
                    },
                    {
                        "title": "Database Optimization",
                        "body": "Tips for improving database query performance"
                    }
                ]
            },
            {
                "title": "Quick Tips",
                "layout": "row",
                "content": [
                    {"title": "Git Workflow", "body": "Streamline your version control"},
                    {"title": "Code Review", "body": "Effective code review practices"},
                    {"title": "Testing", "body": "Writing better unit tests"}
                ]
            }
        ]
    }
    
    output_path = render_from_context(
        template_file="newsletter_layout.html",
        context=context,
        output_name="context_example"
    )
    
    print(f"✓ Context rendering complete: {output_path}")


def example_custom_template_dir():
    """Example using custom template directory."""
    print("\n=== Custom Template Directory ===")
    
    context = {
        "title": "Custom Template Example",
        "sections": [
            {
                "title": "Custom Layout",
                "layout": "row",
                "content": [{"title": "Test", "body": "Using templates directory"}]
            }
        ]
    }
    
    output_path = render_from_context(
        template_file="newsletter_layout.html",
        context=context,
        template_dir="templates",  # Explicitly specify template directory
        output_name="custom_template_example"
    )
    
    print(f"✓ Custom template rendering complete: {output_path}")


if __name__ == "__main__":
    print("DocTeng Library Usage Examples")
    print("==============================")
    
    try:
        example_basic_rendering()
        example_json_rendering()
        example_context_rendering()
        example_custom_template_dir()
        
        print("\n🎉 All examples completed successfully!")
        print("\nGenerated files:")
        print("- output/basic_example.html")
        print("- output/json_example.html") 
        print("- output/context_example.html")
        print("- output/custom_template_example.html")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Make sure you have the templates and content_samples directories set up correctly.") 