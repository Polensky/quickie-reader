import pytest
from document import Document


def test_document_constructor():
    filename = "A file name"
    wpm = 1000
    document = Document(filename=filename, wpm=wpm)
    assert document.filename == filename
    assert document.wpm == wpm
    assert document.is_reading == True

def test_document_orp_index():
    document = Document(filename="")
    words = {1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 3, }
    for length, index in words.items():
        assert document.orp_index("a" * length) == index

def test_document_word_runner(tmpdir):
    filecontent = "This text\nspans\nmultiple\nlines\nand has spaces\n"
    f = tmpdir.join("file.txt")
    f.write(filecontent)

    document = Document(filename=f)
    assert all(word1 == word2 for word1, word2 in zip(document.word_runner(), filecontent.split()))

def test_document_read_document(tmpdir):
    filecontent = "This text\nspans\nmultiple\nlines\nand has spaces\n"
    f = tmpdir.join("file.txt")
    f.write(filecontent)

    document = Document(filename=f)
    print(list(document.read_document()))
    assert all(word1 == (word2, document.orp_index(word2)) for word1, word2 in zip(document.read_document(), filecontent.split()))

def test_document_toggle_play_payse():
    document = Document("")
    assert document.is_reading == True
    document.toggle_play_pause()
    assert document.is_reading == False
    document.toggle_play_pause()
    assert document.is_reading == True

