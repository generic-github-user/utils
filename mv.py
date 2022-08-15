import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('destination')

args = parser.parse_args()
source = Path(args.source)
dest = Path(args.destination)

if dest.is_dir(): dest /= source.name
Path(source).rename(dest)
print(f'Moved {source} to {dest}')
