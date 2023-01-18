from random_words import RandomWords
from quote import quote


class Text:
    def __init__(self):
        self.text = ""

    def get_text(self):
        r = RandomWords()
        w = r.random_word()
        res = quote(w, limit=1)

        self.text = res[0]['quote']

        return self.text
