import argparse
from pathlib import Path
import itertools

parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('destination')

args = parser.parse_args()
print(f'Moving from {args.source} to {args.destination}')

source = list(Path('.').glob(args.source))
#dest = list(Path('.').glob(args.destination))
dest = Path(args.destination)
print(f'Found {len(source)} files')

i = 0
#for i, (a, b) in enumerate(zip(source, dest)):
#for a, b in itertools.zip_longest(source, dest):
for i, a in enumerate(source):
    b = Path(str(dest))
    if b.is_dir(): b /= a.name
    b = Path(str(b)
        .replace('@', str(a.parent))
        .replace('%', a.suffix)
        .replace('#', str(i)))
    if not b.exists():
        Path(a).rename(b)
        print(f'Moved {a} to {b}')
    #i += 1
