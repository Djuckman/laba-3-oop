class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц задается значением типа int")
        self.pages = pages
        super().__init__(name, author)

    def __str__(self):
        return super().__str__() + f". Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}), author={self.pages!r})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Продолжительность задается значением типа float")
        self.duration = duration
        super().__init__(name, author)

    def __str__(self):
        return super().__str__() + f". Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}), duration={self.duration!r})"
