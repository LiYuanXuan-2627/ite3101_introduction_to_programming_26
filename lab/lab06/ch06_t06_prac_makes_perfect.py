from abc import ABC, abstractmethod


class Number(ABC):
    """Abstract numeric API for arithmetic operations."""

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def subtract(self, other):
        pass

    @abstractmethod
    def multiply(self, other):
        pass

    @abstractmethod
    def divide(self, other):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def cube(self):
        pass

    @abstractmethod
    def is_even(self):
        pass

    @abstractmethod
    def is_odd(self):
        pass


class IntNumber(Number):
    """Concrete integer implementation with useful arithmetic behavior."""

    def add(self, other):
        other_value = other.value if isinstance(other, IntNumber) else other
        return IntNumber(self.value + other_value)

    def subtract(self, other):
        other_value = other.value if isinstance(other, IntNumber) else other
        return IntNumber(self.value - other_value)

    def multiply(self, other):
        other_value = other.value if isinstance(other, IntNumber) else other
        return IntNumber(self.value * other_value)

    def divide(self, other):
        other_value = other.value if isinstance(other, IntNumber) else other
        if other_value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return IntNumber(self.value / other_value)

    def square(self):
        return IntNumber(self.value ** 2)

    def cube(self):
        return IntNumber(self.value ** 3)

    def is_even(self):
        return self.value % 2 == 0

    def is_odd(self):
        return self.value % 2 != 0

    def __str__(self):
        return str(self.value)
