"""
Arvore binária didática - 
Nós simples - permite a recuperação dos valores
com slices - 
"""

from itertools import zip_longest

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.depth = 1
        self._len = 1

    @classmethod
    def from_ordered_list(cls, items):
        if not items:
            return None
        middle = len(items) // 2
        root = cls(items[len(items) // 2])
        root.left = cls.from_ordered_list(items[:middle])
        root.right = cls.from_ordered_list(items[middle + 1:])
        root.depth = root._shallow_depth()
        root._len = len(root.right or []) + len(root.left or []) + 1
        return root

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
        self.depth = self._shallow_depth()
        self._len += 1

    def _shallow_depth(self):
        return max(self.left.depth if self.left else 0,
                   self.right.depth if self.right else 0) + 1

    def __contains__(self, value):
        if value == self.value:
            return True
        if value < self.value and self.left:
            return value in self.left
        if value > self.value and self.right:
            return value in self.right
        return False

    def __len__(self):
        return self._len

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

    def draw(self):
        lines = self._draw( center=80)
        print("\n".join(lines))

    def _draw(self, center):
        lines = []
        lines.append(str(self.value).center(center))
        lines_left = []
        lines_right = []
        if self.left:
            lines_left = self.left._draw(center // 2)
        if self.right:
            lines_right = self.right._draw(center // 2)
        for left, right in zip_longest(lines_left, lines_right):
            if not left:
                left = " " * (center // 2)
            if not right:
                right = " " * (center // 2)
            lines.append(left + right)
        return lines

    def recurse_depth(self):
        left = self.left.recurse_depth() if self.left else 0
        right = self.right.recurse_depth() if self.right else 0
        return max(left, right) + 1

if __name__ == "__main__":
    from urllib.request import urlopen
    import string

    text = urlopen("http://www.gutenberg.org/cache/epub/3333/pg3333.txt").read().decode("utf-8")
    tokens = [palavra.strip(string.punctuation).lower() for palavra in text.split()]

    words = Node("mar")
    words.add_many(tokens)
    print(words["ba": "be"])
    