# file-man
Just a simple exercise to create and move files around without knowing where exactly certain directories are located.

## Usage

### Terminology

#### `absolute path`
Examples of an absolute path:
1. `~/dev/python/`
2. `~/Documents/papers/research/`

#### `relative path`
Examples of a relative path:
1. `.`
2. `../`
3. `../../`

#### `ambigous path`
Ambigous paths consist of a single word, the name of the folder that you want it stored in. As an example, if I want to store the new directory in `~/dev/python/` but I don't know where the `/python/` folder is, I would just type `python`. It will then search the computer for directories that match the name `python` and will list the paths of those directories. It is then up to the user to choose which one should be used. If only one is found, it will just use it without needing the user to resolve matching directory names.

Examples of an ambigous paths:
1. `dev`
2. `Documents`
3. `papers`

An example output of creating a directory in `python` is as follows:
```
> create example_dir python
Searching filesystem (this may take a while)
Searching for directories: python
DONE
| All candidates:
 ∟
  | (0) /home/user/.local/share/nvim/mason/packages/python-lsp-server/venv/lib/python3.10/site-packages/parso/python
  | (1) /home/user/.local/share/nvim/lazy/nvim-treesitter/tests/query/highlights/python
  | (2) /home/user/.local/share/nvim/lazy/nvim-treesitter/tests/indent/python
  | (3) /home/user/.local/share/nvim/lazy/nvim-treesitter/queries/python
  | (4) /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/tests/select/python
  | (5) /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/tests/repeatable_move/python
  | (6) /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/queries/python
  | (7) /home/user/.local/share/nvim/lazy/friendly-snippets/snippets/python
  | (8) /home/user/dev/python
  | (9) /home/user/.steam/debian-installation/steamapps/common/SteamLinuxRuntime_sniper/var/tmp-AQSI71/usr/share/gcc/python
  | (10) /home/user/.steam/debian-installation/steamapps/common/SteamLinuxRuntime_sniper/sniper_platform_0.20230509.49493/files/share/gcc/python
  | (11) /home/user/.steam/debian-installation/steamapps/common/SteamLinuxRuntime_soldier/var/tmp-EZJW31/usr/share/gcc-8/python
  | (12) /home/user/.steam/debian-installation/steamapps/common/SteamLinuxRuntime_soldier/soldier_platform_0.20230509.49491/files/share/gcc-8/python
  | (13) /home/user/.steam/debian-installation/ubuntu12_64/steam-runtime-heavy/usr/share/gcc-5/python
  | (14) /home/user/.steam/debian-installation/ubuntu12_32/steam-runtime/usr/share/gcc-5/python
  | (15) /home/user/.steam/debian-installation/ubuntu12_32/steam-runtime.old/usr/share/gcc-5/python

| Top 10 candidates:
 ∟
  | (8) path: /home/user/dev/python
  | (3) path: /home/user/.local/share/nvim/lazy/nvim-treesitter/queries/python
  | (7) path: /home/user/.local/share/nvim/lazy/friendly-snippets/snippets/python
  | (2) path: /home/user/.local/share/nvim/lazy/nvim-treesitter/tests/indent/python
  | (6) path: /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/queries/python
  | (1) path: /home/user/.local/share/nvim/lazy/nvim-treesitter/tests/query/highlights/python
  | (4) path: /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/tests/select/python
  | (14) path: /home/user/.steam/debian-installation/ubuntu12_32/steam-runtime/usr/share/gcc-5/python
  | (5) path: /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/tests/repeatable_move/python
  | (15) path: /home/user/.steam/debian-installation/ubuntu12_32/steam-runtime.old/usr/share/gcc-5/python

Multiple directories with the same name found and needs to be resolved (enter a number)
```

If there are more than 50 candidates, it will go through a "slow mode", and displays this:
```
> finddir Documents
Searching filesystem (this may take a while)
Searching for directories: Documents
DONE
NOTE: More than 50 candidates present
+-----------------------------------------+
|     [ENTER]           = next item       |
| a + [ENTER]           = list all        |
| any number + [ENTER]  = use this number |
+-----------------------------------------+
```

Just as it's stated, `[ENTER]` will show the next item, `a + [ENTER]` will show the rest, and typing a number and pressing `[ENTER]` will use that item. If the rest is shown, you can still look through everything that was printed and choose the number that way as well.

### Create a directory
When prompted, type `create <name> <absolute/relative or ambiguous path>`, where `<name>` is the name of the directory you want to create and `<absolute/relative or ambiguous path>` is where you want it located.

Examples:
```
> create example_dir ~/dev/python/
> create example_dir .
> create example_dir ../
> create example_dir python
```

### Move a file
Similar to above, when prompted, type `create <name> <absolute/relative or ambiguous path>`, where `<name>` is the name of the file you want to move and `<absolute/relative or ambiguous path>` is where you want it located. `<name>` can also be absolute, relative, or ambiguous.

Example:
```
> move ../file.py ~/dev/python/
> move ~/dev/c/file.c .
> move ./file.py ../
> move file.py python
```

### Find a directory
When prompted, type `finddir <name>` where `<name>` is an ambiguous name. It will then list the location(s) of the directory.

Example:
```
finddir tmp
finddir python
finddir dev
```

### Find a file
When prompted, type `findfile <name>` where `<name>` is an ambiguous name. It will then list the location(s) of the file.

Example:
```
findfile main.c
findfile paper.docx
findfile backup.txt
```

### List a directory
This works the same as the command `ls` does, except you provide it an ambiguous path. It will then list out everything in that directory with permissions, size, date last modified, and the name.

Example:
```
ls python
```
Output:
```
> ls python
Searching filesystem (this may take a while)
Searching for directories: python
DONE
| All candidates:
 ∟
  | (0) /home/user/.local/share/nvim/mason/packages/python-lsp-server/venv/lib/python3.10/site-packages/parso/python
  | (1) /home/user/.local/share/nvim/lazy/nvim-treesitter/tests/query/highlights/python
  | (2) /home/user/.local/share/nvim/lazy/nvim-treesitter/tests/indent/python
  | (3) /home/user/.local/share/nvim/lazy/nvim-treesitter/queries/python
  | (4) /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/tests/select/python
  | (5) /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/tests/repeatable_move/python
  | (6) /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/queries/python
  | (7) /home/user/.local/share/nvim/lazy/friendly-snippets/snippets/python
  | (8) /home/user/dev/python
  | (9) /home/user/.steam/debian-installation/steamapps/common/SteamLinuxRuntime_sniper/var/tmp-AQSI71/usr/share/gcc/python
  | (10) /home/user/.steam/debian-installation/steamapps/common/SteamLinuxRuntime_sniper/sniper_platform_0.20230509.49493/files/share/gcc/python
  | (11) /home/user/.steam/debian-installation/steamapps/common/SteamLinuxRuntime_soldier/var/tmp-EZJW31/usr/share/gcc-8/python
  | (12) /home/user/.steam/debian-installation/steamapps/common/SteamLinuxRuntime_soldier/soldier_platform_0.20230509.49491/files/share/gcc-8/python
  | (13) /home/user/.steam/debian-installation/ubuntu12_64/steam-runtime-heavy/usr/share/gcc-5/python
  | (14) /home/user/.steam/debian-installation/ubuntu12_32/steam-runtime/usr/share/gcc-5/python
  | (15) /home/user/.steam/debian-installation/ubuntu12_32/steam-runtime.old/usr/share/gcc-5/python

| Top 10 candidates:
 ∟
  | (8) path: /home/user/dev/python
  | (3) path: /home/user/.local/share/nvim/lazy/nvim-treesitter/queries/python
  | (7) path: /home/user/.local/share/nvim/lazy/friendly-snippets/snippets/python
  | (2) path: /home/user/.local/share/nvim/lazy/nvim-treesitter/tests/indent/python
  | (6) path: /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/queries/python
  | (1) path: /home/user/.local/share/nvim/lazy/nvim-treesitter/tests/query/highlights/python
  | (4) path: /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/tests/select/python
  | (14) path: /home/user/.steam/debian-installation/ubuntu12_32/steam-runtime/usr/share/gcc-5/python
  | (5) path: /home/user/.local/share/nvim/lazy/nvim-treesitter-textobjects/tests/repeatable_move/python
  | (15) path: /home/user/.steam/debian-installation/ubuntu12_32/steam-runtime.old/usr/share/gcc-5/python

Multiple directories with the same name found and needs to be resolved (enter a number)
> 8
8
drwxrwxr-x       4096 2023-07-04 16:39:33 file_man
drwxrwxr-x       4096 2023-06-28 16:42:38 playground
```

### Clear the screen
When prompted, type `clear` to clear the screen.

### Quit the program
When prompted, type `quit` or `exit` to quit the program.

### Deepsearch
By default, when walking through the directories, it starts at `~`. However, by running the program with `deep`, it will being its search at `/`. This will slow down the search time dramatically.

Example:
```
python3 file-man deep
```

Output:
```
$ python3 file_man.py deep
Deepsearch enabled
Type `help` for more information
>
```
