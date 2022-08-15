import argparse
from pathlib import Path
import itertools
import json
import time

parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('destination')
parser.add_argument('--create', '-c', action='store_true')
parser.add_argument('--verbose', '-v', action='store_true')

args = parser.parse_args()
print(f'Moving from {args.source} to {args.destination}')

start = time.time()
if args.create:
    Path(args.destination).mkdir()

source = list(Path('.').glob(args.source))
#dest = list(Path('.').glob(args.destination))
dest = Path(args.destination).expanduser()
print(f'Found {len(source)} files')

i = 0
#for i, (a, b) in enumerate(zip(source, dest)):
#for a, b in itertools.zip_longest(source, dest):
session = []
for i, a in enumerate(source):
    b = Path(str(dest))
    b = Path(str(b)
        .replace('@', str(a.parent))
        .replace('%', a.suffix)
        .replace('#', str(i)))
    if b.is_dir(): b /= a.name
    #breakpoint()
    #print(f'Attempting move from {a} to {b}')
    if not b.exists():
        Path(a).rename(b)
        if args.verbose: print(f'Moved {a} to {b}')
        session.append(json.dumps({'source': str(a), 'destination': str(b)}))
    #i += 1
if args.verbose: print('Updating log file')
with open(Path('~/Desktop/utils/mv_log.json').expanduser(), 'a') as f:
    f.write('\n'.join(session))
end = time.time()
if args.verbose: print(f'Finished in {end - start} seconds')
