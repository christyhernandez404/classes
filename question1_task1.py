# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner.
# Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self):
        # getting input of new owner
        new_owner = input(f"Input the name of the new owner of the {self.type}: ")
        self.owner = new_owner
        print(f"Congratulations! {self.owner} is the new owner of {self.type}!")


vehicle_1 = Vehicle("123456", "boat", "Ricky Martin")
vehicle_2 = Vehicle("999999", "motorcyle", "Christy Benz")
vehicle_3 = Vehicle("987654", "car", "Carolina Cherry")
vehicle_4 = Vehicle("565656", "van", 'Elaine Marie Benes')
vehicle_5 = Vehicle("983636", "taxi", "Cosmo Kramer")

vehicle_1.update_owner()

vehicle_4.update_owner()  
