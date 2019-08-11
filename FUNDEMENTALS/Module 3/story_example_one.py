"""
Retrieve and print words from a URL.

Usage:

    python3 story_example_one.py <URL>
"""
import sys
from urllib.request import urlopen


# a function that gets words from web and stores in list
def fetch_words(url):
    """Fetch a list of words from URL

    Args:
        url: The URL of an UTF-8 text document.
    Returns:
        A list of strings containing words
        of a story.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for words in line_words:
                story_words.append(words)
    return story_words


def print_words(items):
    """
    Print items one per line.

    Args:
        An iterable series of printable items
    """
    for item in items:
        print(item)


def main(url):
    """
    Print each word from a text document.

    Args:
        url: The URL of an UTF-8 text document.
    """
    words = fetch_words(url)
    print_words(words)


# used to run fetch_words as a script
if __name__ == "__main__":
    main(sys.argv[1])  # The 0th arg is the module filename
