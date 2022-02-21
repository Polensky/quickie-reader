import time


class Document:
    """Represent the document that is being read"""

    def __init__(self, handle, wpm=250, start_word=0, optimize_delays=True):
        self.handle = handle
        self.wpm = wpm
        self.optimize_delays = optimize_delays
        self.is_reading = True
        self.seek_performed = False
        self.words = []
        self.current_word = start_word

    @staticmethod
    def orp_index(word):
        """Figure out the optimal recognition point(orp)"""
        len_word = len(word)
        if len_word == 2:
            orp = 2
        elif len_word <= 5:
            orp = len_word // 2 + len_word % 2
        else:
            orp = len_word // 2

        return orp - 1

    def wait_time(self, word):
        """Figure out optimal delay based on word length"""
        delay = 60 / self.wpm
        if self.optimize_delays:
            len_word = len(word)
            if len_word <= 2:
                delay *= 0.75
            elif 6 <= len_word <= 9:
                delay *= 1.5
            elif len_word >= 10:
                delay *= 1.75
            elif len_word >= 13:
                delay *= 2

        return delay

    def word_runner(self):
        """Reads a file and yields it line by line"""
        text = self.handle.read()
        self.words = text.split()
        while self.current_word < len(self.words):
            yield self.words[self.current_word]
            self.current_word += 1


    def read_document(self):
        """Yield one word at a time with his orp index"""
        words = self.word_runner()
        try:
            while True:
                if self.is_reading:
                    word = next(words)
                    orp_ind = self.orp_index(word)
                elif self.seek_performed:
                    word = self.words[self.current_word]
                    orp_ind = self.orp_index(word)

                self.seek_performed = False
                yield (word, orp_ind)

                time.sleep(self.wait_time(word))
        except StopIteration:
            pass
        finally:
            del words

    def toggle_play_pause(self):
        self.is_reading = not self.is_reading

    def change_wpm(self, delta):
        self.wpm += delta
        if self.wpm <= 0:
            self.wpm = 50

    def seek(self, num_words):
        self.current_word += num_words
        if self.current_word < 0:
            self.current_word = 0
        elif self.current_word >= len(self.words):
            self.current_word = len(self.words) - 1
        self.seek_performed = True
