import curses


class CursesApp:
    """Curses application of quickie reader"""

    HORIZONAL_SEP_LENGTH = 21
    HORIZONTAL_SEP = "⎯" * HORIZONAL_SEP_LENGTH
    ORP_INDICATOR_TOP = "▼"
    ORP_INDICATOR_BOT = "▲"
    WPM_DELTA_MINOR = 50
    WPM_DELTA_MAJOR = 250
    SEEK_MINOR = 10
    SEEK_MAJOR = 100
    KEYBIND_TEXT = f"[j/J/k/K] Decrease/Increase WPM by {WPM_DELTA_MINOR}/{WPM_DELTA_MAJOR} [Space] Play/Pause [q] Quit"
    KEYBIND_TEXT_SEEK = f"[h/H/l/L] Seek {SEEK_MINOR}/{SEEK_MAJOR} words backward/forward"

    def __init__(self, document):
        self.document = document
        self.words = self.document.read_document()

    def application(self, stdscr):
        """Main application"""

        stdscr.nodelay(True)
        stdscr.clear()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

        def clear_line(y):
            stdscr.move(y, 0)
            stdscr.clrtoeol()

        def draw_keybind_text():
            stdscr.addstr(
                curses.LINES - 2, x_mid - len(self.KEYBIND_TEXT) // 2, self.KEYBIND_TEXT
            )
            stdscr.addstr(
                curses.LINES - 1,
                x_mid - len(self.KEYBIND_TEXT_SEEK) // 2,
                self.KEYBIND_TEXT_SEEK,
            )

        def draw_info():
            info_text = f"WPM: {self.document.wpm} Word: {self.document.current_word + 1}"
            y_info = curses.LINES - 4
            clear_line(y_info)
            stdscr.addstr(y_info, x_mid - len(info_text) // 2, info_text)

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
            clear_line(y_mid)
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
            draw_word()
            draw_info()
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

            if c == ord("q"):
                break
            elif c == ord("k"):
                self.document.change_wpm(self.WPM_DELTA_MINOR)
            elif c == ord("K"):
                self.document.change_wpm(self.WPM_DELTA_MAJOR)
            elif c == ord("j"):
                self.document.change_wpm(-self.WPM_DELTA_MINOR)
            elif c == ord("J"):
                self.document.change_wpm(-self.WPM_DELTA_MAJOR)
            elif c == ord(" "):
                self.document.toggle_play_pause()
            elif c == ord("l"):
                self.document.seek(self.SEEK_MINOR)
            elif c == ord("L"):
                self.document.seek(self.SEEK_MAJOR)
            elif c == ord("h"):
                self.document.seek(-self.SEEK_MINOR)
            elif c == ord("H"):
                self.document.seek(-self.SEEK_MAJOR)

            redraw()

            redraw_needed = False
            wpm_redraw_needed = False
            first_iteration = False

    def run(self):
        curses.wrapper(self.application)
