"""
models.py - Animal class hierarchy demonstrating OOP concepts.
"""


class Animal:
    """Base class representing a generic animal."""

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        """Return the sound the animal makes."""
        return "..."

    def describe(self):
        """Return a description of the animal."""
        return f"{self.name} is {self.age} years old and is {self.color}."

    def __str__(self):
        return f"Animal(name={self.name}, age={self.age}, color={self.color})"


class Dog(Animal):
    """Child class representing a dog."""

    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def speak(self):
        """Override speak to return a dog sound."""
        return "Woof!"

    def fetch(self):
        """Unique method for Dog."""
        return f"{self.name} fetches the ball!"

    def __str__(self):
        return (
            f"Dog(name={self.name}, age={self.age}, "
            f"color={self.color}, breed={self.breed})"
        )


class Cat(Animal):
    """Child class representing a cat."""

    def __init__(self, name, age, color, is_indoor):
        super().__init__(name, age, color)
        self.is_indoor = is_indoor

    def speak(self):
        """Override speak to return a cat sound."""
        return "Meow!"

    def purr(self):
        """Unique method for Cat."""
        return f"{self.name} is purring..."

    def __str__(self):
        indoor_status = "indoor" if self.is_indoor else "outdoor"
        return (
            f"Cat(name={self.name}, age={self.age}, "
            f"color={self.color}, type={indoor_status})"
        )