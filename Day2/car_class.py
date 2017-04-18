"""
A Car class that can be used to instantiate various vehicles.

It takes in arguments that depict the type, model, and name of the vehicle, 
provided they are set.
"""


class Car(object):
    num_of_doors = 4
    num_of_wheels = 4
    speed = 0

    def __init__(self, name=None, model=None, car_type=None):
        if model is None:
            self.model = 'GM'
        if name is None:
            self.name = 'General'
        else:
            self.car_type = car_type
            self.model = model
            self.name = name
        if name == 'Koenigsegg' or name == "Porshe":
            self.num_of_doors = 2
        if car_type == 'trailer':
            self.num_of_wheels = 8

    def is_saloon(self):
        if self.car_type != 'trailer':
            return True

    def drive(self, speed):
        if self.is_saloon():
            self.speed = speed * (1000 / 3)
        else:
            self.speed = speed * 11
        return self
