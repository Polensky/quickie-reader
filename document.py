import time
import math
from enum import Enum


class Document:
    """Represent the document that is being read"""

    class State(Enum):
        reading = 1
        paused = 2

    def __init__(self, filename, wpm = 350):
        self.filename = filename
        self.wpm = wpm
        self.state = self.State.reading


    def orp_index(self, word):
        """Figure out the optimal recognition point"""
        len_word = len(word)
        if len_word == 2:
            orp = 2
        elif len_word <= 5:
            orp = math.ceil(len_word / 2)
        elif len_word % 2:
            orp = math.floor(len_word / 2)
        else:
            orp = len_word / 2

        return orp - 1

    def word_runner(self):
        with open(self.filename) as doc:
            for line in doc:
                for word in line.split():
                    yield word

    def read_document(self):
        """Yield one word at a time with his orp index"""
        words = self.word_runner()
        word = "press space to start"
        orp_ind = 13
        try:
            while True:
                time.sleep(60 / self.wpm)

                if self.state == self.State.reading:
                    word = next(words)
                    orp_ind = int(self.orp_index(word))

                yield (word, orp_ind)
        except StopIteration:
            pass
        finally:
            del words

    def toggle_play_pause(self):
        if self.state == self.State.paused:
            self.state = self.State.reading
        else:
            self.state = self.State.paused
