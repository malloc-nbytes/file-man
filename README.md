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

### Create a directory
When prompted, type `create <name> <absolute/relative or ambiguous path>`, where `name` is the name of the directory you want to create and `<absolute/relative or ambiguous path>` is where you want it located.

Examples:
```
> create example_dir ~/dev/python/
> create example_dir .
> create example_dir ../
> create example_dir python
```




