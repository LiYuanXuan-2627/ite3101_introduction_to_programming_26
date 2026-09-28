from abc import ABC, abstractmethod


class NumberBase(ABC):
    @abstractmethod
    def square(self):
        """Return the square of the value."""

    @abstractmethod
    def cube(self):
        """Return the cube of the value."""

    @abstractmethod
    def add(self, other):
        """Return the sum of this number and another number."""

    @abstractmethod
    def __str__(self):
        """Return the number as a string."""


class number(NumberBase):
    def __init__(self, value=0):
        self.value = value

    def square(self):
        return self.value ** 2

    def cube(self):
        return self.value ** 3

    def add(self, other):
        if isinstance(other, number):
            return number(self.value + other.value)
        return number(self.value + other)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"number({self.value!r})"

    def __add__(self, other):
        return self.add(other)


Number = number


def cube(value):
    if isinstance(value, number):
        return value.cube()
    if isinstance(value, (int, float)):
        return value ** 3
    return value * value * value