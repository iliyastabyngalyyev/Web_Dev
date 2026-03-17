"""
main.py - Demonstrates usage of the Animal class hierarchy.
"""

from Models import Animal, Dog, Cat


def main():
    # Instantiate objects from each class
    generic_animal = Animal(name="Generic", age=5, color="brown")
    dog = Dog(name="Buddy", age=3, color="golden", breed="Labrador")
    cat = Cat(name="Whiskers", age=4, color="white", is_indoor=True)

    # Store objects in a list
    animals = [generic_animal, dog, cat]

    print("=== All Animals ===")
    for animal in animals:
        print(animal)

    print("\n=== Descriptions ===")
    for animal in animals:
        print(animal.describe())

    # Demonstrate polymorphism - calling overridden speak() method
    print("\n=== Polymorphism: speak() ===")
    for animal in animals:
        print(f"{animal.name} says: {animal.speak()}")

    # Call unique methods
    print("\n=== Unique Methods ===")
    print(dog.fetch())
    print(cat.purr())


if __name__ == "__main__":
    main()