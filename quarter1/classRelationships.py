class BasketballEquipments:
    def __init__(self, brand, price):
        self.brand = brand
        self.__price = price
        self.owner = None   

    def assign_owner(self, athlete):
        self.owner = athlete

    def display_info(self):
        owner_name = self.owner.name if self.owner else "No owner"
        return f"Brand: {self.brand}, Price: ₱{self.__price}, Owner: {owner_name}"


class NBAAthletes:
    def __init__(self, name, team, nationality, salary):
        self.name = name                
        self.team = team                
        self.__nationality = nationality  
        self.__salary = salary    

    def display_point(self, points):
        """Show how many points the athlete scored."""
        return f"{self.name} scored {points} total points!"

    def get_salary(self):
        return self.__salary

    def get_nationality(self):
        return self.__nationality

print("--- BEFORE RELATIONSHIP ---")
ball = BasketballEquipments("Wilson", 2500)
player = NBAAthletes("Kobe Bryant", "Los Angeles Lakers", "American", 25000000)

print(ball.display_info())
print(player.display_point(33643))  

print("\n--- BUILDING RELATIONSHIP ---")
ball.assign_owner(player)

print("\n--- AFTER RELATIONSHIP ---")
print(ball.display_info())
print(f"{ball.brand} is owned by {ball.owner.name}, who plays for {ball.owner.team}.")
print(f"{ball.owner.name}'s nationality is {ball.owner.get_nationality()} and salary is ₱{ball.owner.get_salary()}.")









