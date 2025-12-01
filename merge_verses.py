import json
import os
import glob

def merge_chapters():
    all_verses = []
    
    # Iterate through chapter 1 to 18
    for i in range(1, 19):
        filename = f"data/chapter_{i}.json"
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    chapter_data = json.load(f)
                    if isinstance(chapter_data, list):
                        all_verses.extend(chapter_data)
                    else:
                        print(f"Warning: {filename} does not contain a list.")
            except Exception as e:
                print(f"Error reading {filename}: {e}")
        else:
            print(f"Warning: {filename} not found.")

    # Create the JS content
    js_content = f"window.gitaVerses = {json.dumps(all_verses, ensure_ascii=False, indent=2)};"
    
    # Write to verses.js
    with open("data/verses.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    
    print(f"Successfully created data/verses.js with {len(all_verses)} verses.")

if __name__ == "__main__":
    merge_chapters()
