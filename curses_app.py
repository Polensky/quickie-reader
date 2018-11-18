from document import Document
import curses


class CursesApp:
    """Curses application of quickie reader"""
    def __init__(self, filename):
        self.document = Document(filename)

    def application(self, stdscr):
        """Main application"""
        stdscr.nodelay(True)
        stdscr.clear()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

        words = self.document.read_document()
        keybind_text = "[j] Decrease WPM [k] Increase WPM [Space] Play/Pause [q] Quit"

        for word, orp_ind in words:
            c = stdscr.getch()
            curses.flushinp()
            stdscr.clear()
            curses.update_lines_cols()

            if c == ord('q'):
                break
            elif c == ord('k'):
                document.wpm += 50
            elif c == ord('j'):
                document.wpm -= 50
            elif c == ord(' '):
               document.toggle_play_pause()

            stdscr.addstr(0, 0, f'WPM: {document.wpm}')
            stdscr.addstr(int(curses.LINES - 1), 0, keybind_text)
            x_mid = int(curses.COLS / 2)
            y_mid = int(curses.LINES / 2)

            stdscr.addstr(y_mid - 1, x_mid - 10, '-'*20)
            stdscr.addstr(y_mid - 1, x_mid, '|', curses.color_pair(1))
            stdscr.addstr(y_mid + 1, x_mid - 10, '-'*20)
            stdscr.addstr(y_mid + 1, x_mid, '|', curses.color_pair(1))

            stdscr.addstr(y_mid, int(x_mid - orp_ind), word[:orp_ind])
            stdscr.addstr(y_mid, x_mid, word[orp_ind], curses.color_pair(1))
            stdscr.addstr(y_mid, x_mid + 1, word[orp_ind + 1:])

            stdscr.addstr(int(curses.LINES-1), int(curses.COLS-1), '')

    def run(self):
        curses.wrapper(self.application)