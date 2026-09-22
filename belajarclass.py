class Laptop:
    def __init__(self, name, price, rating,):
        self.name = name
        self.price = price
        self.rating = rating

lenovo = Laptop("Lenovo Yoga", 22000, "B")
macbook = Laptop("Macbook M5 pro", 45000, "A")
print(lenovo.name)
print(macbook.name)
