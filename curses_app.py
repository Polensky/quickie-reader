from document import Document
import curses


class CursesApp:
    """Curses application of quickie reader"""

    KEYBIND_TEXT = "[j] Decrease WPM [k] Increase WPM [Space] Play/Pause [q] Quit"
    HORIZONTAL_SEP = '⎯'*20
    ORP_INDICATOR_TOP = '▼'
    ORP_INDICATOR_BOT = '▲'

    def __init__(self, filename):
        self.document = Document(filename)

    def application(self, stdscr):
        """Main application"""
        stdscr.nodelay(True)
        stdscr.clear()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

        words = self.document.read_document()

        for word, orp_ind in words:
            c = stdscr.getch()
            curses.flushinp()
            stdscr.clear()
            curses.update_lines_cols()

            if c == ord('q'):
                break
            elif c == ord('k'):
                self.document.wpm += 50
            elif c == ord('j'):
                self.document.wpm -= 50
            elif c == ord(' '):
                self.document.toggle_play_pause()

            x_mid = int(curses.COLS / 2)
            y_mid = int(curses.LINES / 2)

            info_text = f'WPM: {self.document.wpm}'
            stdscr.addstr(curses.LINES - 3, x_mid - int(len(info_text)/2), info_text)

            middle_keybind = x_mid - int((len(self.KEYBIND_TEXT)/2))
            stdscr.addstr(int(curses.LINES - 1), middle_keybind, self.KEYBIND_TEXT)

            stdscr.addstr(y_mid - 1, x_mid - 10, self.HORIZONTAL_SEP)
            stdscr.addstr(y_mid - 1, x_mid, self.ORP_INDICATOR_TOP, \
                          curses.color_pair(1))
            stdscr.addstr(y_mid + 1, x_mid - 10, self.HORIZONTAL_SEP)
            stdscr.addstr(y_mid + 1, x_mid, self.ORP_INDICATOR_BOT, \
                          curses.color_pair(1))

            stdscr.addstr(y_mid, int(x_mid - orp_ind), word[:orp_ind])
            stdscr.addstr(y_mid, x_mid, word[orp_ind], curses.color_pair(1))
            stdscr.addstr(y_mid, x_mid + 1, word[orp_ind + 1:])

            stdscr.addstr(int(curses.LINES-1), int(curses.COLS-1), '')

    def run(self):
        curses.wrapper(self.application)
