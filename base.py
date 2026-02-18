import random

challan_pay = random.randint(250, 1500)

class vechile:
    def __init__(self, vech_name, speed , rgs_number , licence_number = True):

        self.vech_name = vech_name
        self.licence_number = licence_number
        self.rgs_number = rgs_number
        self.speed = speed


    def speed_limit(self):
        return 90 
    

    def calculate_fine(self):
        if self.speed > speed_limit() + 30 :
            return 2000
        elif self.speed > speed_limit() + 10 :
            return 1500
        else:
            return 800

    def check_Speed(self):
        if self.speed > 90:
            print(f"Your Speed is {self.speed} Km/h and Your Vechile Number is {self.vech_name} and Your Registration number is this {self.rgs_number} \nYour licence-number is {self.licence_number}")
            self.challan()
        else:
            print(f"{self.vech_name} is driving safely at {self.speed} km/h")

    def challan(self):
        print(f"Your Vechile name is {self.vech_name}\nSpeed: {self.speed} \nChallan is PkR {challan_pay}")

class car(vechile):
    def check_speed(self):
        return 100

class Truck(vechile):
    def check_speed(self):
        return 120
        

class Bike(vechile):
    def check_speed(self):
        return 80
        

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
