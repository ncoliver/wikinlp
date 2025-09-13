from nlplogic.corenlp import get_phrases

def test_get_phrase():
    assert 'carolina' in get_phrases("North Carolina")
