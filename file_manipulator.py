# using argparse module
import argparse
import os

def reverse(inputpath, outputpath):
    with open(inputpath, 'r') as f:
        data = f.read()
    with open(outputpath, 'w') as f:
        f.write(data[::-1])

def copy(inputpath, outputpath):
    with open(inputpath, 'r') as f:
        data = f.read()
    with open(outputpath, 'w') as f:
        f.write(data)

def duplicate_contents(inputpath, n):
    with open(inputpath, 'r') as f:
        data = f.read()
    with open(inputpath, 'w') as f:
        for _ in range(n):
            f.write(data)

def replace_string(inputpath, needle, newstring):
    with open(inputpath, 'r') as f:
        data = f.read()
    with open(inputpath, 'w') as f:
        f.write(data.replace(needle, newstring))

def validate_file_path(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"{path} does not exist")
    return path

parser = argparse.ArgumentParser(
    prog="file-manipulator",
    description="file manipulator programを作ってみたよ！うまく作動してるかな？",
    epilog="以上です！"
)
subparsers = parser.add_subparsers(dest='command')

reverse_parser = subparsers.add_parser('reverse')
reverse_parser.add_argument('inputpath', type=validate_file_path)
reverse_parser.add_argument('outputpath')

copy_parser = subparsers.add_parser('copy')
copy_parser.add_argument('inputpath', type=validate_file_path)
copy_parser.add_argument('outputpath')

duplicate_parser = subparsers.add_parser('duplicate-contents')
duplicate_parser.add_argument('inputpath', type=validate_file_path)
duplicate_parser.add_argument('n', type=int)

replace_parser = subparsers.add_parser('replace-string')
replace_parser.add_argument('inputpath', type=validate_file_path)
replace_parser.add_argument('needle')
replace_parser.add_argument('newstring')

args = parser.parse_args()

if args.command == 'reverse':
    reverse(args.inputpath, args.outputpath)
elif args.command == 'copy':
    copy(args.inputpath, args.outputpath)
elif args.command == 'duplicate-contents':
    duplicate_contents(args.inputpath, args.n)
elif args.command == 'replace-string':
    replace_string(args.inputpath, args.needle, args.newstring)
