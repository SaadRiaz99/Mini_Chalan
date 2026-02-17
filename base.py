import random

challan_pay = random.randint(250, 1500)

class vechile:
    def __init__(self, vech_name, speed):
        self.vech_name = vech_name
        self.speed = speed

    def check_Speed(self):
        if self.speed > 90:
            print(f"Your Speed is {self.speed} Km/h and Your Vechile Number is {self.vech_name}")
            self.challan()
        else:
            print(f"{self.vech_name} is driving safely at {self.speed} km/h")

    def challan(self):
        print(f"Your Vechile name is {self.vech_name}\nSpeed: {self.speed} \nChallan is PkR {challan_pay}")

class car(vechile):
    def check_speed(self):
        if self.speed > 90:
            print(f"Car {self.vech_name} exceeded speed limit! Speed: {self.speed} km/h")
            self.challan()
        else:
            print(f"Car {self.vech_name} is within speed limit.")

class Truck(vechile):
    def check_speed(self):
        if self.speed > 120:
            print(f"Truck {self.vech_name} exceeded speed limit! Speed: {self.speed} km/h")
            self.challan()
        else:
            print(f"Truck {self.vech_name} is within speed limit.")

class Bike(vechile):
    def check_speed(self):
        if self.speed > 80:
            print(f"Bike {self.vech_name} exceeded speed limit! Speed: {self.speed} km/h")
            self.challan()
        else:
            print(f"Bike {self.vech_name} is within speed limit.")

def Check_speed(vechile_obj):
    vechile_obj.check_Speed()

def main():
    vehicles = [
        car("Honda Civic", 100),
        Bike("Yamaha R15", 85),
        Truck("Volvo FH", 65),
        car("Toyota Corolla", 80)
    ]

    print("---- Traffic Speed Check ----")
    for v in vehicles:
        Check_speed(v)

if __name__ == "__main__":
    main()
