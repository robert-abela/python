import os

def search_dir(path, ext):
    filtered = []
    all_items = os.listdir(path)
    for item_name in all_items:
        full_path = os.path.join(path, item_name)
        if os.path.isfile(full_path) and item_name.endswith(ext):
            filtered.append(item_name)
    
    filtered.sort(reverse=True)
    for item in filtered:
        print(item)


path = '.' # working directory
ext = '.py'
search_dir(path, ext)
