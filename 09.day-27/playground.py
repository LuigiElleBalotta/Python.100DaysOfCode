def add(*args):
    for n in args:
        print(n)
    return sum(args)


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # .get serve per non mandare il crash l'app se non si specifica la keyword
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

    def __str__(self):
        return f"{self.make} {self.model}: the color is {self.color} and it has {self.seats} seats."


my_car = Car(make="Nissan", model="GT-R", color="brown", seats=5)
print(my_car)
