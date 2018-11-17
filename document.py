import time
import math
from enum import Enum


class Document:
    """Represent the document that is being read"""

    def __init__(self, filename, wpm = 350):
        self.filename = filename
        self.wpm = wpm
        self.is_reading = True


    def orp_index(self, word):
        """Figure out the optimal recognition point(orp)"""
        len_word = len(word)
        if len_word == 2:
            orp = 2
        elif len_word <= 5:
            orp = math.ceil(len_word / 2)
        elif len_word % 2:
            orp = math.floor(len_word / 2)
        else:
            orp = len_word / 2

        return int(orp - 1)

    def word_runner(self):
        """Reads a file and yields it line by line"""
        with open(self.filename) as doc:
            text = doc.readlines()
        for line in text:
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

                if self.is_reading:
                    word = next(words)
                    orp_ind = int(self.orp_index(word))

                yield (word, orp_ind)
        except StopIteration:
            pass
        finally:
            del words

    def toggle_play_pause(self):
        self.is_reading = True if not self.is_reading else False
