from utils.set_interval import set_interval
from utils.set_interval_2 import Set_Interval
from threading import Timer


class Vehicle:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self) -> int:
        return f"{self.color} car with {self.mileage} milage"

    def get_color(self):
        print(f"color of {self} is {self.color}")


class SpeedGage:
    def __init__(self) -> None:
        self.speed = 0

    def inc_speed(self, amount):
        print(f"speed increasing by {amount} speed is {self.speed}")
        self.speed += amount

    def dec_speed(self, amount):
        print(f"speed decreasing by {amount} speed is {self.speed}")
        self.speed += amount

    def start_acceleration(self, acceleation):
        acc = Set_Interval(1, self.inc_speed, [acceleation])
        self.acc = acc

    def stop_acceleration(self):
        print(f"STOPPING {self} at speed {self.speed}")
        self.acc.cancel()


class Car(Vehicle, SpeedGage):
    def __init__(self, color, mileage, model, seats) -> None:
        Vehicle.__init__(self, color, mileage)
        SpeedGage.__init__(self)
        self.model = model
        self.seats = seats


benz_wagon = Car("Black", 1000, "Mercedece", 4)
print(benz_wagon)
print("car speed", benz_wagon.speed)
benz_wagon.inc_speed(10)
benz_wagon.inc_speed(10)
benz_wagon.inc_speed(10)
print("car speed", benz_wagon.speed)
benz_wagon.start_acceleration(15)


def print_speed():
    print("car speed ___", benz_wagon.speed)


stop_benz_timer = Timer(3, benz_wagon.stop_acceleration)
stop_benz_timer.start()

show_speed_timer = Timer(3, print_speed)
show_speed_timer.start()
