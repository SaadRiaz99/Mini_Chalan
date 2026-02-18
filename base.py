import random

challan_pay = random.randint(250, 1500)

class vechile:
    def __init__(self, vech_name, speed, rgs_number, licence_number=True):

        self.vech_name = vech_name
        self.licence_number = licence_number
        self.rgs_number = rgs_number
        self.speed = speed

    def speed_limit(self):
        return 90 

    def calculate_fine(self):
        if self.speed > self.speed_limit() + 30:
            return 2000
        elif self.speed > self.speed_limit() + 10:
            return 1500
        else:
            return 800

    def check_Speed(self):
        if self.speed > self.speed_limit():

            fine = self.calculate_fine()

            if not self.licence_number:
                print("⚠ Licence Expired! Extra 1000 PKR added")
                fine += 1000

            print(f"\n🚔 Vehicle: {self.vech_name}")
            print(f"Registration No: {self.rgs_number}")
            print(f"Speed: {self.speed} Km/h")
            print(f"Speed Limit: {self.speed_limit()} Km/h")
            print(f"Total Fine: PKR {fine}\n")

        else:
            print(f"✅ {self.vech_name} is driving safely at {self.speed} km/h\n")


# ✅ Proper Polymorphism
class car(vechile):
    def speed_limit(self):
        return 100


class Truck(vechile):
    def speed_limit(self):
        return 120
        

class Bike(vechile):
    def speed_limit(self):
        return 80
        

def Check_speed(vechile_obj):
    vechile_obj.check_Speed()


def main():
    vehicles = [
        car("Honda Civic", 135, "LEA-1234", True),
        Bike("Yamaha R15", 95, "LHR-5678", False),
        Truck("Volvo FH", 110, "ISB-9999", True),
        car("Toyota Corolla", 85, "KHI-2222", True)
    ]

    print("---- Traffic Speed Check ----\n")

    for v in vehicles:
        Check_speed(v)


if __name__ == "__main__":
    main()
