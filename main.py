#!/usr/bin/env python3

from curses_app import CursesApp
from document import Document
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read documents one word at a time")
    parser.add_argument("filename", metavar="filename", type=str)
    parser.add_argument(
        "-r",
        "--resume",
        metavar="n",
        help="Start from n-th word",
        type=int,
        default=0,
    )
    args = parser.parse_args()

    try:
        handle = open(args.filename)
        document = Document(handle, start_word=args.resume)

        curses_app = CursesApp(document)
        curses_app.run()
    finally:
        handle.close()
        print(
            f"To resume reading from this point run with argument -r {document.current_word}"
        )
