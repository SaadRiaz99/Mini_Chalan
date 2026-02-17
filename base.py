import random 
challan_pay = random.randint(250 ,1500)
class vechile:
    def __init__(self, vech_name , speed):
        self.vech_name = vech_name
        self.speed = speed

        def check_Speed(self):
            if self.speed > 90 :
                print(f"Your Speed is {self.speed} Km/h and Your Vechile Number is {self.vech_name} ")
                self.challan()
            else:
                print(f"{self.name} is driving safely at {self.speed} km/h")

        def challan():
            print(f"Your Vechiel name is {self.vech_name}Speed\n{self.speed} \nChallan is PkR {challan_pay}")

        