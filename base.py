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
                fine += 1000

            print(f"Vehicle: {self.vech_name}")
            print(f"Registration No: {self.rgs_number}")
            print(f"Speed: {self.speed} Km/h")
            print(f"Speed Limit: {self.speed_limit()} Km/h")
            print(f"Total Fine: PKR {fine}\n")
        else:
            print(f"{self.vech_name} is driving safely at {self.speed} km/h\n")


class car(vechile):
    def speed_limit(self):
        return 100


class Truck(vechile):
    def speed_limit(self):
        return 120
        

class Bike(vechile):
    def speed_limit(self):
        return 80
        

def main():
    print("Traffic Speed Monitoring System\n")

    vech_type = input("Enter vehicle type (car/bike/truck): ").lower()
    name = input("Enter vehicle name: ")
    rgs = input("Enter registration number: ")
    speed = int(input("Enter vehicle speed: "))
    licence = input("Is licence valid? (yes/no): ").lower()

    licence_status = True if licence == "yes" else False

    if vech_type == "car":
        vehicle = car(name, speed, rgs, licence_status)
    elif vech_type == "bike":
        vehicle = Bike(name, speed, rgs, licence_status)
    elif vech_type == "truck":
        vehicle = Truck(name, speed, rgs, licence_status)
    else:
        print("Invalid vehicle type")
        return

    vehicle.check_Speed()


if __name__ == "__main__":
    main()
