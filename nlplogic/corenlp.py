from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search Wikipedia"""
    return wikipedia.search(name)


def get_text(topic):
    """Summarize Wikipedia"""

    result = wikipedia.summary(topic)
    return result


def get_textblob(text):
    """Gets text blob object and returns"""
    blob = TextBlob(text)
    return blob


def get_tags(name):
    """Find wikipedia name and return back tags"""

    text = get_text(name)
    blob = get_textblob(text)
    tags = blob.tags
    return tags


def get_phrases(name):
    """Find wikipedia name and return back noun phrases"""

    text = get_text(name)
    blob = get_textblob(text)
    phrases = blob.noun_phrases
    return phrases
