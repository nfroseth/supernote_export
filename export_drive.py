import argparse
import os
from typing import Iterable, Optional
from supernotelib.cmds.supernote_tool import main as supernote_tool


def main(argv: Optional[Iterable[str]] = None) -> None:
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("input", type=str, default="./drive", help="Top Directory")
    parser.add_argument(
        "output", type=str, default="./convert", help="Output Directory"
    )
    args = parser.parse_args(argv)

    note = "note"
    for root, dirs, files in os.walk(args.input):
        for file in [file for file in files if file.split(".")[-1] == note]:
            added_path = os.path.join(args.output, root, file.split(".")[0])
            os.makedirs(added_path, exist_ok=True)

            print(f"File at {root}, Dirs found {dirs}, File name {file}, Processing...")

            supernote_tool(
                [
                    "convert",
                    "-a",
                    f"{os.path.join(root, file)}",
                    os.path.join(added_path, f"{file}.png"),
                ]
            )

if __name__ == "__main__":
    exit(main())
