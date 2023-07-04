#!/bin/python3

import sys
import os

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

def __search_matching_item(name, search_type):
    print("Searching filesystem (this may take a while)")
    matching_items = __walk_dirs(name, search_type)

    if len(matching_items) > 1:
        prompt_message = f"Multiple {search_type} with the same name found and needs to be resolved (enter a number)"
        idx = int(prompt(prompt_message))
        if idx >= 0 and idx < len(matching_items):
            return matching_items[idx]
        elif len(matching_items) == 0:
            err(f"No {search_type} with the name {name} found.")
            return None
        else:
            return matching_items[0]
    elif len(matching_items) == 0:
        err(f"No {search_type} with the name {name} found.")
        return None
    else:
        return matching_items[0]

def __walk_dirs(name, searchfor):
    global DEEP

    home_directory = os.path.expanduser("~")
    if DEEP:
        print("NOTE: Deepsearch is enabled. Searching times will be much longer.")
        home_directory = '/'

    print(f"Searching for {searchfor}: {name}")
    matching = []
    i = 0
    for root, dirs, files in os.walk(home_directory):
        if searchfor == 'directories':
            for directory in dirs:
                if directory == name:
                    new_path = os.path.join(root, directory)
                    print(f"{i}: {new_path}")
                    matching.append(new_path)
                    i += 1
        elif searchfor == 'files':
            for file in files:
                if file == name:
                    new_path = os.path.join(root, file)
                    print(f"{i}: {new_path}")
                    matching.append(new_path)
                    i += 1
    return matching

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

def usage():
    print("Run with `deep` to enable deep search (search times is greatly affected)\n")
    print(". = Current directory")
    print("../ = Back a single directory")
    print("~ = Home directory\n")
    print("Create a directory")
    print("  create <name> <absolute or relative path>")
    print("Move a file/directory")
    print("  move <filename> <absolute or relative path>")

def set_deep():
    global DEEP
    print("Deepsearch enabled")
    DEEP = True

functions = {
    "quit": quit,
    "create": create_dir,
    "move": move_file,
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

    if command in functions:
        functions[command](parts, parts_iter)
    else:
        err(f"Invalid command {command}")

