# utils

Some utilities for Unix systems; main goals include convenience, safety, and
flexibility.

## Contents

[[toc]]

## Usage

### mv

`mv.py` is a replacement for the Unix built-in `mv`, including functionality
from `rsync` and `rename` such as recursive directory merging, checksums/data
integrity verification, and pattern-based renaming.

By default, `mv.py` includes some useful replacements that will be expanded
(textually) for each file:

- `#`: an integer representing how many files and directories were moved before the current one
- `@`: the parent directory of the source/origin file or directory (useful for recursively handling nested directory structures, or when operating on a long file path)
- `#`: the file extension/suffix, including the `.`

Some examples:

*rename a file*
```
python mv.py image.png test.png
```

*rename a file*
```
python mv.py ./image.png ./test.png
```

*move a file (test-dir exists)*
```
python mv.py image.png test-dir/image.png
```

*move a file (test-dir exists)*
```
python mv.py image.png test-dir
```

*move a file (test-dir does not exist)*
```
python mv.py -c image.png test-dir
```

*move files matching a pattern*
```
python mv.py -c '*.png' images
```

*move files matching a pattern and rename by index*
```
python mv.py -c '*.png' 'images/image-#.png'
```

*move files with multiple extensions*
```
python mv.py -c './source/*.*' 'images/image-#%'
```

*move files and print details to stdout*
```
python mv.py -c -v '*.png' 'images/image-#.png'
```

*move files recursively*
```
python mv.py -c './**/*.png' 'images/image-#.png'
```

*move files recursively, preserving directory structure*
```
python mv.py -c './**/*.png' 'images/@'
```

## Branches

- main: main branch into which others are merged once stable
- dev: development branch where new features can be implemented and tested before being merged into the stable `main` branch
- mv: script for easily moving files and directories in bulk

## Statistics

[[stats]]
