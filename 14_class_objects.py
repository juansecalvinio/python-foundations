# clases y objetos
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.shirt_number = None
        self.is_injured = False
        self.__secret_code = "xyz123"  # atributo privado

    def add_to_squad_list(self):
        return f"{self.name} is added to the squad list"

    def add_to_injured_list(self):
        self.is_injured = True
        return f"{self.name} is added to the injured list"

    def set_shirt_number(self, shirt_number):
        self.shirt_number = shirt_number
        return f"{self.name} has shirt number {self.shirt_number}"

    def __generate_secret_code(self):
        return f"Secret code for {self.name} is {self.__secret_code}"


player_one = Player("Bukayo Saka", 25)
print(player_one.add_to_injured_list())

player_two = Player("Eberechi Eze", 27)
print(player_two.set_shirt_number(10))
print(player_two.add_to_squad_list())

# Error: AttributeError: 'Player' object has no attribute '__secret_code'
# print(player_two.__secret_code)

# para acceder a un atributo privado, se puede usar name mangling
print(player_two._Player__secret_code)
print(player_two._Player__generate_secret_code())
