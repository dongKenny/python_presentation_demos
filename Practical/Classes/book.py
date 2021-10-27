class Book:
    def __init__(self, title: str, word_count: int):
        self.__title: str = title
        self.__word_count: int = word_count

    @property
    def title(self):
        return self.title

    @property
    def word_count(self):
        return self.word_count

    def __repr__(self):
        return f'Book({self.title}, {self.word_count})'

    def __hash__(self):
        return hash((self.title, self.word_count))

    def __eq__(self, other):
        if other.__class is self.__class__:
            return (self.title, self.word_count) == (other.title, other.word_count)
        else:
            return NotImplemented

    def __lt__(self, other):
        if other.__class is self.__class__:
            return (self.title, self.word_count) < (other.title, other.word_count)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class is self.__class__:
            return (self.title, self.word_count) <= (other.title, other.word_count)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class is self.__class__:
            return (self.title, self.word_count) > (other.title, other.word_count)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class is self.__class__:
            return (self.title, self.word_count) >= (other.title, other.word_count)
        else:
            return NotImplemented



