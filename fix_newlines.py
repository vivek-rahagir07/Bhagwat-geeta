import os
import json
import re

def clean_text(text):
    if isinstance(text, str):
        # Replace escaped newlines and actual newlines with space
        return text.replace('\\n', ' ').replace('\n', ' ')
    return text

def clean_json_file(filepath):
    print(f"Processing {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        def recursive_clean(obj):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, str):
                        obj[k] = clean_text(v)
                    elif isinstance(v, (dict, list)):
                        recursive_clean(v)
            elif isinstance(obj, list):
                for i in range(len(obj)):
                    item = obj[i]
                    if isinstance(item, str):
                        obj[i] = clean_text(item)
                    elif isinstance(item, (dict, list)):
                        recursive_clean(item)
        
        recursive_clean(data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def clean_html_file(filepath):
    print(f"Processing {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Specific replacement for shlokaBank content in index.html
        # We look for the shlokaBank array and replace \\n inside it
        # But simpler approach: replace \\n globally if we are sure
        
        # Let's be a bit more targeted. 
        # The user wants to remove /n in shloks.
        # In index.html, they appear as \\n in the source code string.
        
        new_content = content.replace('\\\\n', ' ')
        
        # Also check for single \n if any (though in JS source string it would be a literal newline)
        # We don't want to remove actual newlines in the HTML structure
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    base_dir = '/Users/vivek/Documents/GitHub/Bhagwat-geeta'
    data_dir = os.path.join(base_dir, 'data')
    
    # Process JSON files
    if os.path.exists(data_dir):
        for filename in os.listdir(data_dir):
            if filename.startswith('chapter_') and filename.endswith('.json'):
                clean_json_file(os.path.join(data_dir, filename))
    
    # Process index.html
    clean_html_file(os.path.join(base_dir, 'index.html'))

if __name__ == "__main__":
    main()
