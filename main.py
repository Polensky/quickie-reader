from document import Document
import curses
import time
from curses import wrapper

def main(stdscr):
    stdscr.nodelay(True)
    stdscr.clear()
    wi = 4
    cnt = 0
    direction = 1
    document = Document('prep.md')
    words = document.read_document()

    while True:
        c = stdscr.getch()
        curses.flushinp()
        stdscr.clear()

        if c == ord('q'):
            break
        elif c == ord('k'):
            document.wpm += 50
        elif c == ord('j'):
            document.wpm -= 50

        stdscr.addstr(0, 0, f'WPM: {document.wpm}')
        word, orp_ind = next(words)
        x_mid = int(curses.COLS / 2)
        y_mid = int(curses.LINES / 2)

        stdscr.addstr(y_mid - 1, x_mid - 10, '-'*20)
        stdscr.addstr(y_mid, int(x_mid - orp_ind), word)
        stdscr.addstr(y_mid + 1, x_mid - 10, '-'*20)


if __name__ == '__main__':
    wrapper(main)
