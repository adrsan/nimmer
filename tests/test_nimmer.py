from nimmer.nimmer import nim


def test_empty_string():
    assert nim("") == ""


def test_single_word():
    assert nim("Hello") == "H"


def test_sentence_with_stop_words():
    assert nim("The quick brown fox") == "QBF"


def test_only_stop_words():
    assert nim("of the and") == ""
