from nlplogic.corenlp import *

def test_get_phrase():
    assert 'carolina' in get_phrases("North Carolina")