import argparse
from pathlib import Path
import itertools
import json
import time

# Create argument parser
parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('destination')
parser.add_argument('--create', '-c', action='store_true')
parser.add_argument('--verbose', '-v', action='store_true')

# Parse command line arguments
args = parser.parse_args()
print(f'Moving from {args.source} to {args.destination}')

start = time.time()
if args.create:
    Path(args.destination).mkdir()

# Find files matching glob
source = list(Path('.').glob(args.source))
dest = Path(args.destination).expanduser()
print(f'Found {len(source)} files')

session = []
# Loop over files
for i, a in enumerate(source):
    b = Path(str(dest))
    # Make path substitutions
    b = Path(str(b)
        .replace('@', str(a.parent))
        .replace('%', a.suffix)
        .replace('#', str(i)))
    # Handle implicit move to directory
    if b.is_dir(): b /= a.name
    #print(f'Attempting move from {a} to {b}')
    # Execute file move
    if not b.exists():
        Path(a).rename(b)
        if args.verbose: print(f'Moved {a} to {b}')
        # Record move operation in log
        session.append(json.dumps({'source': str(a), 'destination': str(b)}))
if args.verbose: print('Updating log file')
with open(Path('~/Desktop/utils/mv_log.json').expanduser(), 'a') as f:
    f.write('\n'.join(session))
end = time.time()
if args.verbose: print(f'Finished in {end - start} seconds')
