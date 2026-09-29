class BasketballEquipments:
    def __init__(self, brand, color, price, weight):
        self.brand = brand
        self.color = color
        self.price = price
        self.weight = weight

    def display_info(self):
        return f"Brand: {self.brand}, Color: {self.color}, Price: ₱{self.price}, Weight: {self.weight}g"


class BasketballShoes(BasketballEquipments):
    def __init__(self, brand, color, price, weight, size, material):
        super().__init__(brand, color, price, weight)
        self.size = size
        self.material = material

    def display_size(self):
        return f"Shoe Size: {self.size}"

    def display_materials(self):
        return f"Material: {self.material}"


class NBAAthletes:
    def __init__(self, name, team, nationality, salary):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.salary = salary
        self.equipments = []

    def add_equipment(self, equipment):
        self.equipments.append(equipment)

    def display_profile(self):
        return f"Name: {self.name}, Team: {self.team}, Nationality: {self.nationality}, Salary: ₱{self.salary}"

    def display_equipments(self):
        if not self.equipments:
            return f"{self.name} has no equipments."
        details = [eq.display_info() for eq in self.equipments]
        return f"{self.name}'s Equipments:\n" + "\n".join(details)


if __name__ == "__main__":
    ball = BasketballEquipments("Wilson", "Orange", 2500, 600)
    shoes = BasketballShoes("Nike", "White", 5000, 800, 42, "Leather")

    player = NBAAthletes("Kobe Bryant", "Los Angeles Lakers", "American", 25000000)
    player.add_equipment(ball)
    player.add_equipment(shoes)

    print("Test 1: Inheritance")
    print(shoes.display_info())
    print(shoes.display_size())
    print(shoes.display_materials())

    print("\nTest 2: Composition/Aggresion")
    print(player.display_profile())
    print(player.display_equipments())


