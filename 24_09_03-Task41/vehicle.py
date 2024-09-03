
class Vehicle:
    def __init__(self, name, size, color, tyres):
        self.name = name
        self.size = size
        self.color = color
        self.tyres = tyres

    def buy_car(self):
        print(f"You brought the {self.name}, color {self.color}")

    def sell_car(self):
        print(f"The car {self.name}, color {self.color} has been sold")
