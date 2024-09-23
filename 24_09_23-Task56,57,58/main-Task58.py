# Task 58 - PizzaError

class PizzaError(Exception):
    def __init__(self, pizza_name, message="Error with pizza"):
        self.pizza_name = pizza_name
        super().__init__(f"{message}: {self.pizza_name}")


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza_name, cheese_amount):
        message = f"Too much cheese! {cheese_amount}% is over the limit."
        super().__init__(pizza_name, message)


class NoSauceError(PizzaError):
    def __init__(self, pizza_name):
        message = "No sauce detected!"
        super().__init__(pizza_name, message)


class TooManyToppingsError(PizzaError):
    def __init__(self, pizza_name, topping_count):
        message = f"Too many toppings! {topping_count} is over the limit."
        super().__init__(pizza_name, message)


def make_pizza(pizza, cheese, sauce, toppings):
    valid_pizzas = ["Margherita", "Pepperoni", "Hawaiian"]

    if pizza not in valid_pizzas:
        raise PizzaError(pizza, "Unknown pizza type")

    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese)

    if sauce == 0:
        raise NoSauceError(pizza)

    if toppings > 5:
        raise TooManyToppingsError(pizza, toppings)

    print(f"{pizza} Pizza is ready with {cheese}% cheese, {sauce}% sauce, and {toppings} toppings!")


try:
    make_pizza("Pepperoni", 110, 50, 4)
except PizzaError as e:
    print(e)

try:
    make_pizza("Hawaiian", 80, 0, 3)
except PizzaError as e:
    print(e)

try:
    make_pizza("Margherita", 80, 50, 6)
except PizzaError as e:
    print(e)

try:
    make_pizza("Calzone", 70, 40, 2)
except PizzaError as e:
    print(e)
