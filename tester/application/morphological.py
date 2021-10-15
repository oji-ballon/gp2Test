import MeCab
sepalater = MeCab.Tagger('-Owakati')

class Morphology(object):

    def __init__(self, texts):
        self.texts = texts

        pass

    def sepalate(self):
        import MeCab
        t = MeCab.Tagger('')
        words = t.parse(self.texts).split()

        sepalated = {}
        for i, e in enumerate(words):
            if i % 2 == 0 and i < len(words) - 1:
                sepalated[e] = words[i + 1]

        return print(sepalated)
