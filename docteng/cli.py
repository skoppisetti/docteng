"""
Command-line interface for DocTeng.
"""

import argparse
import sys

from .renderer import render_newsletter


def main():
    """
    Main CLI entry point for DocTeng.
    """
    parser = argparse.ArgumentParser(
        description='DocTeng - Render newsletters and documents from templates and JSON content',
        prog='docteng'
    )
    parser.add_argument(
        'template', 
        help='Template file name (relative to templates/ directory)'
    )
    parser.add_argument(
        'json_file', 
        help='Path to JSON content file'
    )
    parser.add_argument(
        '-n', '--name', 
        help='Name for the output file (without extension)'
    )
    parser.add_argument(
        '-o', '--output-dir', 
        default='output', 
        help='Output directory (default: output)'
    )
    parser.add_argument(
        '-t', '--template-dir',
        default='templates',
        help='Template directory (default: templates)'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='DocTeng 0.1.0'
    )
    
    args = parser.parse_args()
    
    try:
        output_path = render_newsletter(
            template_file=args.template,
            json_file=args.json_file,
            output_name=args.name,
            output_dir=args.output_dir,
            template_dir=args.template_dir
        )
        print(f"Newsletter generated successfully: {output_path}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main() 