#!/bin/python3

import sys
import os
import stat
from datetime import datetime
import threading
import time

import itertools

DEEP = False

def get_next(parts, parts_iter):
    arg = parts[parts_iter[0]]
    parts_iter[0] += 1
    return arg

def prompt(message=None):
    if message is not None:
        print(message)
    print("> ", end="")
    return input()

def quit(parts=None, parts_iter=None):
    sys.exit()

def err(msg):
    print(f"(ERR) {msg}")

def spinning_wheel(stop_event):
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    while not stop_event.is_set():
        print(next(spinner), end='\r')
        time.sleep(0.1)

def top_ten_shortest(data):
    print("\n| Top 10 candidates:")
    print(" ∟")
    sorted_data = sorted(data, key=lambda x: len(x[1]))
    num_items_to_print = min(10, len(sorted_data))
    for i in range(num_items_to_print):
        id_value, string_value = sorted_data[i]
        print(f"  | ({id_value}) path: {string_value}")
    print()

def __walk_dirs(name, searchfor):
    global DEEP

    home_directory = os.path.expanduser("~")
    if DEEP:
        print("NOTE: Deepsearch is enabled. Searching times will be much longer.")
        home_directory = '/'

    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinning_wheel, args=(stop_event,))
    spinner_thread.start()

    print(f"Searching for {searchfor}: {name}")
    matching = []
    i = 0
    for root, dirs, files in os.walk(home_directory):
        if searchfor == 'directories':
            for directory in dirs:
                if directory == name:
                    new_path = os.path.join(root, directory)
                    matching.append((i, new_path))
                    i += 1
        elif searchfor == 'files':
            for file in files:
                if file == name:
                    new_path = os.path.join(root, file)
                    matching.append((i, new_path))
                    i += 1
    stop_event.set()
    spinner_thread.join()
    print("\rDONE")
    return matching

def __search_matching_item(name, search_type, modification=True):
    print("Searching filesystem (this may take a while)")
    matching_items = __walk_dirs(name, search_type)

    if len(matching_items) > 1:
        os.system("stty -echo")
        big = len(matching_items) > 50
        idx = None

        if big:
            print("NOTE: More than 50 candidates present")
            print("+-----------------------------------------+")
            print("|     [ENTER]           = next item       |")
            print("| a + [ENTER]           = list all        |")
            print("| any number + [ENTER]  = use this number |")
            print("+-----------------------------------------+")

        print("| All candidates:")
        print(" ∟")

        for item in matching_items:
            if big:
                advance = input()
                try:
                    idx = int(advance)
                    break
                except:
                    if 'a' in advance:
                        big = False
            print(f"  | ({item[0]}) {item[1]}")

        os.system("stty echo")
        top_ten_shortest(matching_items)

        if not modification:
            return None

        if idx is None:
            prompt_message = f"Multiple {search_type} with the same name found and needs to be resolved (enter a number)"
            idx = int(prompt(prompt_message))
        else:
            print(f"Using candidate: {matching_items[idx]}")

        if idx >= 0 and idx < len(matching_items):
            return matching_items[idx][1]
        elif len(matching_items) == 0:
            err(f"No {search_type} with the name {name} found.")
            return None
        else:
            return matching_items[0][1]

    elif len(matching_items) == 0:
        err(f"No {search_type} with the name {name} found.")
        return None
    else:
        return matching_items[0][1]

def __create_dir(path):
    print(f"Creating directory: {path}")
    try:
        os.makedirs(path)
        print(f"Directory created: {path}")
    except OSError as e:
        err(f"Failed to create directory: {path}")
        err(e)

def create_dir(parts, parts_iter):
    try:
        name = get_next(parts, parts_iter)
        path = get_next(parts, parts_iter)
    except:
        err("Not enough arguments provided")
        return

    if not os.path.isdir(path) and path != '.' and path != '~':
        path = __search_matching_item(path, "directories")

    if path is None:
        return

    path = os.path.expanduser(path)
    path = os.path.join(path, name)
    __create_dir(path)

def move_file(parts, parts_iter):
    try:
        filename = get_next(parts, parts_iter)
        path = get_next(parts, parts_iter)
    except:
        err("Not enough arguments provided")
        return

    filepath = None
    destination = None

    if filename.startswith('~/'):
        expanded_filename = os.path.expanduser(filename)
        if os.path.isfile(expanded_filename):
            filepath = os.path.abspath(expanded_filename)

    if filepath is None:
        filepath = __search_matching_item(filename, "files")

    if os.path.isdir(path) or '~' in path or '.' in path:
        destination = os.path.abspath(os.path.expanduser(path))
    else:
        destination = __search_matching_item(path, "directories")

    if filepath is None or destination is None:
        err(f"Exiting as filepath is None or destination is None")
        return

    try:
        filename = os.path.basename(filepath)
        destination_path = os.path.join(destination, filename)

        if os.path.isfile(destination_path):
            err(f"A file with the name '{filename}' already exists in the destination directory")
            return

        os.rename(filepath, destination_path)
        print(f"Moved file '{filename}' to '{destination_path}'")
    except OSError as e:
        err(f"Failed to move file '{filename}': {str(e)}")

def find_dir(parts, parts_iter):
    try:
        dirname = get_next(parts, parts_iter)
    except:
        err("Not enough arguments provided")
        return
    __search_matching_item(dirname, "directories", False)

def find_file(parts, parts_iter):
    try:
        filename = get_next(parts, parts_iter)
    except:
        err("Not enough arguments provided")
        return
    __search_matching_item(filename, "files", False)

def clear_terminal(parts, parts_iter):
    # Clear terminal screen command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear terminal screen command for Linux/Mac
    else:
        os.system('clear')

def list_dir(parts, parts_iter):
    filepath = get_next(parts, parts_iter)
    if os.path.isdir(filepath) or '~' in filepath or '.' in filepath:
        filepath = os.path.abspath(os.path.expanduser(filepath))
    else:
        filepath = __search_matching_item(filepath, "directories")

    if filepath is None or filepath is None:
        err(f"Exiting as filepath is None or filepath is None")
        return

    items = os.listdir(filepath)
    max_permissions_width = 10
    max_size_width = 10

    for item in items:
        item_path = os.path.join(filepath, item)
        item_stat = os.stat(item_path)
        
        item_size = item_stat.st_size
        item_permissions = stat.filemode(item_stat.st_mode)
        item_last_modified = datetime.fromtimestamp(item_stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")

        output = "{:<{}} {:>{}} {:<19} {}".format(item_permissions, max_permissions_width,
                                                  item_size, max_size_width,
                                                  item_last_modified,
                                                  item)
        print(output)

def usage():
    print("Run with `deep` to enable deep search (search times is greatly affected)\n")
    print(". = Current directory")
    print("../ = Back a single directory")
    print("~ = Home directory\n")
    print("Create a directory")
    print("  create <name> <absolute/relative or ambiguous path>")
    print("Move a file")
    print("  move <filename> <absolute/relative or ambiguous path>")
    print("Find a directory")
    print("  finddir <name>")
    print("Find a file")
    print("  findfile <name>")
    print("List items in a directory")
    print("  ls <absolute/relative or ambiguous path>")
    print("Clear the screen")
    print("  clear")
    print("Quit the program")
    print("  quit")
    print("  exit")

def set_deep():
    global DEEP
    print("Deepsearch enabled")
    DEEP = True

functions = {
    "quit": quit,
    "exit": quit,
    "clear": clear_terminal,
    "ls": list_dir,
    "create": create_dir,
    "move": move_file,
    "finddir": find_dir,
    "findfile": find_file,
}

arg_functions = {
    "deep": set_deep,
}

argv = sys.argv[1:]

for arg in argv:
    try:
        arg_functions[arg]()
    except:
        err(f"Invalid arg: {arg}")

print("Type `help` for more information")
while True:
    user_input = prompt()

    if user_input == "help":
        usage()
        continue

    parts_iter = [0]
    parts = user_input.split(' ')

    command = get_next(parts, parts_iter)
    if command == "":
        continue

    if command in functions:
        functions[command](parts, parts_iter)
    else:
        err(f"Invalid command {command}")

