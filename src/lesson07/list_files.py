import os
import time

path = '.' # working directory

def human_time(timestamp):
    print(time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime(timestamp)))

def human_size(bytes):
    print(bytes, 'bytes')

all_items = os.listdir(path)
for item_name in all_items:
    full_path = os.path.join(path, item_name)
    stats = os.stat(full_path)
    
    if os.path.isdir(full_path):
        pass
    elif os.path.isfile(full_path):
        print(item_name)
        human_size(stats.st_size)
        human_time(stats.st_mtime)
        print() #empty line
    
