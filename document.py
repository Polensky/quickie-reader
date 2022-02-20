import time


class Document:
    """Represent the document that is being read"""

    def __init__(self, filename, wpm=350):
        self.filename = filename
        self.wpm = wpm
        self.is_reading = True
        self.words = []
        self.current_word = 0

    def orp_index(self, word):
        """Figure out the optimal recognition point(orp)"""
        len_word = len(word)
        if len_word == 2:
            orp = 2
        elif len_word <= 5:
            orp = len_word // 2 + len_word % 2
        else:
            orp = len_word // 2

        return orp - 1

    def word_runner(self):
        """Reads a file and yields it line by line"""
        with open(self.filename) as doc:
            text = doc.read()
        self.words = text.split()
        while self.current_word < len(self.words):
            yield self.words[self.current_word]
            self.current_word += 1


    def read_document(self):
        """Yield one word at a time with his orp index"""
        words = self.word_runner()
        try:
            while True:
                time.sleep(60 / self.wpm)

                if self.is_reading:
                    word = next(words)
                    orp_ind = self.orp_index(word)

                yield (word, orp_ind)
        except StopIteration:
            pass
        finally:
            del words

    def toggle_play_pause(self):
        self.is_reading = not self.is_reading

    def seek(self, num_words):
        self.current_word += num_words
        if self.current_word < 0:
            self.current_word = 0
        elif self.current_word >= len(self.words):
            self.current_word = len(self.words) - 1
