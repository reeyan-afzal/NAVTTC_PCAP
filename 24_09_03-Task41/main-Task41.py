# Task 41 - Exploring OOP

from vehicle import Vehicle

if __name__ == "__main__":
    car1 = Vehicle("Ferrari", 10, "RED", 4)
    car2 = Vehicle("Toyota Prius", 15, "BLUE", 4)
    car3 = Vehicle("BMW", 20, "PURPLE", 4)

    car1.buy_car()
    car2.buy_car()
    car3.buy_car()

    print()
    car1.sell_car()
