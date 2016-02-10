"""
Arvore binária didática - 
Nós simples - permite a recuperação dos valores
com slices - 
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value > self.value:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.add(value)
        elif value < self.value:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.add(value)

    def __contains__(self, value):
        if value == self.value:
            return True
        if value < self.value and self.left:
            return value in self.left
        if value > self.value and self.right:
            return value in self.right
        return False

    def __getitem__(self, index):
        if not isinstance(index, slice):
            if index in self:
                return index
            raise KeyError
        left, right, middle = [], [], []
        if (index.start is None or index.start < self.value) and self.left:
            left = self.left[index.start: min(
                self.value,
                index.stop if index.stop is not None else self.value)]
        if (index.stop is None or index.stop > self.value) and self.right:
            right = self.right[max(self.value,
                                   index.start if index.start is not None else self.value)
                                   : index.stop]
        if ((index.start is None and index.stop is None) or
             (index.stop is not None and index.start is None and self.value < index.stop) or
             (index.start is not None and index.stop is None and self.value > index.start) or
             (index.start <= self.value < index.stop)
            ):
            middle = [self.value]
        return left + middle + right
    
    def __iter__(self):
        return iter(self[:])

    def __repr__(self):
        return "Node({}, {}, {})".format(self.left or "", self.value, self.right or "")
    
    def add_many(self, items):
        for i in items:
            self.add(i)

if __name__ == "__main__":
    from urllib.request import urlopen
    import string

    text = urlopen("http://www.gutenberg.org/cache/epub/3333/pg3333.txt").read().decode("utf-8")
    tokens = [palavra.strip(string.punctuation).lower() for palavra in text.split()]

    words = Node("mar")
    words.add_many(tokens)
    print(words["ba": "be"])
    