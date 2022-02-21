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
    parser.add_argument(
        "-w",
        "--wpm",
        metavar="n",
        help="Set initial WPM",
        type=int,
        default=250,
    )
    parser.add_argument(
        "-no",
        "--dont-optimize-delays",
        action="store_true",
        help="Change word display time based on word's length",
    )
    args = parser.parse_args()

    try:
        handle = open(args.filename)
        document = Document(
            handle,
            wpm=args.wpm,
            start_word=args.resume - 1,
            optimize_delays=not args.dont_optimize_delays,
        )

        curses_app = CursesApp(document)
        curses_app.run()
    finally:
        handle.close()
        print(
            f"To resume reading from this point run with argument -r {document.current_word + 1}"
        )
