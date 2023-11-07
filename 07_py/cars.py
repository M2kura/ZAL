class Car:
    def __init__(self, znacka: str, cena: int) -> None:
        self.znacka = znacka
        self.cena = cena

    def __str__(self) -> str:
        pass

first_car = Car("BMW", 750000)
second_car = Car("Mercedes", 950000)
# print(first_car.znacka)
# print(first_car.cena)