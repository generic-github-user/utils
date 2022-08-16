import argparse
from pathlib import Path
import itertools
import json
import time
import shutil

# Create argument parser
parser = argparse.ArgumentParser()
parser.add_argument('source', help='Origin (where to move from); globs/wildcards are allowed')
parser.add_argument('destination', help='Target (where to move to)')
parser.add_argument('--create', '-c', action='store_true', help='Create the target directory if it does not already exist')
parser.add_argument('--verbose', '-v', action='store_true', help='Print additional information about what the script is doing to your terminal (useful for debugging)')
parser.add_argument('--duplicate', '-d', action='store_true', help='Copy/duplicate files and directories instead of moving them')

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
        if args.duplicate: shutil.copy(a, b)
        else: Path(a).rename(b)

        if args.verbose: print(f'Moved {a} to {b}')
        # Record move operation in log
        session.append(json.dumps({'source': str(a), 'destination': str(b)}))
if args.verbose: print('Updating log file')
with open(Path('~/Desktop/utils/mv_log.json').expanduser(), 'a') as f:
    f.write('\n'.join(session))
end = time.time()
if args.verbose: print(f'Finished in {end - start} seconds')
