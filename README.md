# utils

Some utilities for Unix systems; main goals include convenience, safety, and
flexibility.

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
