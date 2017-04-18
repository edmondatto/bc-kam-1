class Animal(object):
    animal_type = ''
    num_of_legs = 4
    sound = 'roar'
    num_of_horns = 0

    def __str__(self):
        return "A {}  with {} legs and makes a {} sound.".format(self.__class__.__name__, self.num_of_legs, self.sound)

    def make_sound(self):
        return self.sound.upper() * 3

    def has_horns(self):
        if self.num_of_horns > 0:
            return True
        else:
            return False

    def has_legs(self):
        if self.num_of_legs > 0:
            return True
        else:
            return False

    def move(self):
        return "It is walking"


class Dog(Animal):
    animal_type = 'Dog'
    sound = 'woof woof '


class Snake(Animal):
    animal_type = 'Snake'
    sound = 'Hiss '
    num_of_legs = 0

    def move(self):
        return "It s gliding"


class Cow(Animal):
    animal_type = 'Cow'
    sound = 'Mow '


class PetDog(Dog):
    def __init__(self):
        self.name = input("> Enter your pet's name: ")


