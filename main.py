#!/usr/bin/env python3

from curses_app import CursesApp
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read documents one word at a time')
    parser.add_argument('filename', metavar='filename', type=str)
    args = parser.parse_args()


    try:
        handle = open(args.filename)
        curses_app = CursesApp(handle)
        curses_app.run()
    finally:
        handle.close()
