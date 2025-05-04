class Fruit:
    """
    Represents a fruit with a name, quantity (amount), and price.
    Encapsulates data using private attributes and exposes them with properties.
    """

    def __init__(self, name: str, amount: int, price: float):
        self.__name = name
        self.__amount = amount
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, value: int):
        self.__amount = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        self.__price = value

    def __str__(self) -> str:
        return f"Name: {self.__name}\nAmount: {self.__amount}\nPrice: {self.__price} kr"
