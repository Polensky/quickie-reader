from document import Document
import curses


class CursesApp:
    """Curses application of quickie reader"""

    KEYBIND_TEXT = "[j] Decrease WPM [k] Increase WPM [Space] Play/Pause [q] Quit"
    HORIZONAL_SEP_LENGTH = 21
    HORIZONTAL_SEP = "⎯" * HORIZONAL_SEP_LENGTH
    ORP_INDICATOR_TOP = "▼"
    ORP_INDICATOR_BOT = "▲"

    def __init__(self, filename):
        self.document = Document(filename)
        self.words = self.document.read_document()

    def application(self, stdscr):
        """Main application"""

        stdscr.nodelay(True)
        stdscr.clear()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

        def draw_keybind_text():
            middle_keybind = x_mid - len(self.KEYBIND_TEXT) // 2
            stdscr.addstr(curses.LINES - 1, middle_keybind, self.KEYBIND_TEXT)

        def draw_wpm():
            info_text = f"WPM: {self.document.wpm}"
            stdscr.addstr(curses.LINES - 3, x_mid - len(info_text) // 2, info_text)

        def draw_borders():
            stdscr.addstr(y_mid - 1, x_mid - 10, self.HORIZONTAL_SEP)
            stdscr.addstr(
                y_mid - 1, x_mid, self.ORP_INDICATOR_TOP, curses.color_pair(1)
            )
            stdscr.addstr(y_mid + 1, x_mid - 10, self.HORIZONTAL_SEP)
            stdscr.addstr(
                y_mid + 1, x_mid, self.ORP_INDICATOR_BOT, curses.color_pair(1)
            )

        def draw_word():
            stdscr.move(y_mid, 0)
            stdscr.clrtoeol()
            stdscr.addstr(y_mid, x_mid - orp_ind, word[:orp_ind])
            stdscr.addstr(y_mid, x_mid, word[orp_ind], curses.color_pair(1))
            stdscr.addstr(y_mid, x_mid + 1, word[orp_ind + 1 :])

        def move_cursor():
            stdscr.move(curses.LINES - 1, curses.COLS - 1)

        def redraw():
            if redraw_needed:
                stdscr.clear()
                draw_borders()
                draw_keybind_text()
            if redraw_needed or wpm_redraw_needed:
                draw_wpm()
            draw_word()
            move_cursor()

        rows = cols = 0
        first_iteration = True

        for word, orp_ind in self.words:
            c = stdscr.getch()
            curses.flushinp()
            curses.update_lines_cols()

            x_mid = curses.COLS // 2
            y_mid = curses.LINES // 2
            redraw_needed = (
                rows != curses.COLS or cols != curses.LINES or first_iteration
            )
            rows = curses.COLS
            cols = curses.LINES

            wpm_redraw_needed = False
            if c == ord("q"):
                break
            elif c == ord("k"):
                self.document.wpm += 50
                wpm_redraw_needed = True
            elif c == ord("j"):
                self.document.wpm -= 50
                wpm_redraw_needed = True
            elif c == ord(" "):
                self.document.toggle_play_pause()

            redraw()

            redraw_needed = False
            wpm_redraw_needed = False
            first_iteration = False

    def run(self):
        curses.wrapper(self.application)
