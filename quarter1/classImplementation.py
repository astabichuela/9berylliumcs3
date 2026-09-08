class BasketballEquipments:
    def __init__(self, brand, color, price, weight):
        self.brand = brand
        self.color = color
        self.__price = price
        self.__weight = weight

    def lift(self):
        return f"Lifting the {self.brand} equipment weighing {self.__weight}g."

    def bounce(self, times):
        return f"The {self.brand} basketball bounced {times} times!"

    def apply_discount(self, percent):
        self.__price -= self.__price * (percent / 100)
        return f"Price updated to {self.__price}."

    def get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight


equipment1 = BasketballEquipments("Nike", "Orange", 2500, 600)
equipment2 = BasketballEquipments("Spalding", "Brown", 3000, 650)

print("--- BEFORE ---")
print("Equipment 1:", equipment1.brand, equipment1.color, equipment1.get_price(), equipment1.get_weight())
print("Equipment 2:", equipment2.brand, equipment2.color, equipment2.get_price(), equipment2.get_weight())

print("\nApplying discount to Equipment 1...")
print(equipment1.apply_discount(10))

print("\n--- AFTER ---")
print("Equipment 1:", equipment1.brand, equipment1.color, equipment1.get_price(), equipment1.get_weight())
print("Equipment 2:", equipment2.brand, equipment2.color, equipment2.get_price(), equipment2.get_weight())


