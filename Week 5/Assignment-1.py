# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, number):
        print(f"{self.model} is calling {number}...")

    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"{self.model} charged to {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, Battery: {self.battery}%)"


# Child Class with inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        print(f"{self.model} is playing {game} with {self.cooling_system} cooling!")


# Create objects
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 50)
phone2 = GamingPhone("Asus", "ROG Phone 6", 256, 80, "Liquid Cooling")

print(phone1)
phone1.call("0745407727")
phone1.charge(30)

print(phone2)
phone2.play_game("PUBG Mobile")

