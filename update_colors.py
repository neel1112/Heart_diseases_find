import os
import re
from pathlib import Path

# Define the color mappings
color_mappings = {
    # Old colors to new colors
    '#2ca4b6': '#5E936C',  # Primary blue to green
    '#1d8a9b': '#3E5F44',  # Darker blue to darker green
    '#ff6b6b': '#93DA97',  # Red accent to light green
    '#f8f9fa': '#E8FFD7',  # Light gray to lightest green
    '#343a40': '#3E5F44',  # Dark gray to dark green
    '#495057': '#5E936C',  # Medium gray to medium green
    '#dee2e6': '#93DA97',  # Light gray to light green
    '#007bff': '#5E936C',  # Bootstrap primary blue to green
    '#0056b3': '#3E5F44',  # Bootstrap dark blue to dark green
    '#28a745': '#5E936C',  # Bootstrap success green to our green
    '#218838': '#3E5F44',  # Bootstrap dark success green to our dark green
    '#17a2b8': '#5E936C',  # Bootstrap info blue to green
    '#138496': '#3E5F44',  # Bootstrap dark info blue to dark green
    '#1e3a2a': '#3E5F44',  # Dark text to dark green
    '#4a6450': '#5E936C',  # Medium text to medium green
    '#3a4a42': '#5E936C',  # Another medium text to medium green
}

def update_file_colors(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Update color variables in style tags
        style_pattern = r'<style[^>]*>([\s\S]*?)<\/style>'
        def update_style(match):
            style_content = match.group(1)
            for old_color, new_color in color_mappings.items():
                # Match color as whole word to avoid partial replacements
                style_content = re.sub(rf'(?<!\w){re.escape(old_color)}(?!\w)', new_color, style_content, flags=re.IGNORECASE)
            return f'<style>{style_content}</style>'
        
        content = re.sub(style_pattern, update_style, content, flags=re.IGNORECASE)
        
        # Update inline styles
        style_attr_pattern = r'style="([^"]*)"'
        def update_inline_style(match):
            style = match.group(1)
            for old_color, new_color in color_mappings.items():
                style = re.sub(rf'(?<!\w){re.escape(old_color)}(?!\w)', new_color, style, flags=re.IGNORECASE)
            return f'style="{style}"'
        
        content = re.sub(style_attr_pattern, update_inline_style, content)
        
        # Update background-clip properties for better compatibility
        content = content.replace('-webkit-background-clip: text;', '-webkit-background-clip: text; background-clip: text;')
        
        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            
        print(f"Updated: {file_path}")
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return False

def main():
    templates_dir = Path('e:/Heart-Disease-Prediction-System-main - Copy - Copy - Copy/health/templates')
    html_files = list(templates_dir.glob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to process...")
    
    success_count = 0
    for html_file in html_files:
        if update_file_colors(html_file):
            success_count += 1
    
    print(f"\nUpdate complete! Processed {success_count} out of {len(html_files)} files successfully.")

if __name__ == "__main__":
    main()
