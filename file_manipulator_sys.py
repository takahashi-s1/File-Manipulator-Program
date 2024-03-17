# using sys module 
import sys
import os

# command,inputpathだけ固定してあとは任意にする
if len(sys.argv) < 3:
    print("Usage: python3 file_manipulator.py command inputpath [outputpath] [n] [needle] [newstring]")
    sys.exit(1)

# 引数からcommand,inputpathを取得
command = sys.argv[1]
inputpath = sys.argv[2]

# commandによって処理を分岐
if command == 'reverse':
    if len(sys.argv) != 4:
        print("Usage: python3 file_manipulator.py reverse inputpath outputpath")
        sys.exit(1)
    outputpath = sys.argv[3]
    with open(inputpath, 'r') as f:
        content = f.read()
    with open(outputpath, 'w') as f:
        f.write(content[::-1])

elif command == 'copy':
    if len(sys.argv) != 4:
        print("Usage: python3 file_manipulator.py copy inputpath outputpath")
        sys.exit(1)
    outputpath = sys.argv[3]
    os.system(f'cp {inputpath} {outputpath}')

elif command == 'duplicate-contents':
    if len(sys.argv) != 4:
        print("Usage: python3 file_manipulator.py duplicate-contents inputpath n")
        sys.exit(1)
    n = int(sys.argv[3])
    with open(inputpath, 'r') as f:
        content = f.read()
    with open(inputpath, 'w') as f:
        f.write(content * n)

elif command == 'replace-string':
    if len(sys.argv) != 5:
        print("Usage: python3 file_manipulator.py replace-string inputpath needle newstring")
        sys.exit(1)
    needle = sys.argv[3]
    newstring = sys.argv[4]
    with open(inputpath, 'r') as f:
        content = f.read()
    with open(inputpath, 'w') as f:
        f.write(content.replace(needle, newstring))

else:
    print(f"Invalid command: {command}")
    sys.exit(1) # exit(1)はエラーを表す. 0は正常終了を表す
