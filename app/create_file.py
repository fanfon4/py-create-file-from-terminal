import sys
import os
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    dirs = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    dir_path = ""
    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        filepath = os.path.join(dir_path, file_name) if dir_path else file_name

        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_is_not_empty = (os.path.exists(filepath)
                             and os.path.getsize(filepath) > 0)

        with open(filepath, "a") as f:
            if file_is_not_empty:
                f.write("\n")

            f.write(f"{timestamp}\n")
            for index, line_content in enumerate(lines, 1):
                f.write(f"{index} {line_content}\n")


create_file()
