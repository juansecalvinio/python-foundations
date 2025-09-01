list_numbers = [1, 2, 3, 4, 5]
list_strings = ["Hola", "Mundo"]
list_mixed = [1, "Hola", 3.4, True]

list_players = ["Eberechi Eze", "Declan Rice",
                "Willian Saliba"]
injured_players = ["Bukayo Saka", "Martin Ødegaard"]

print(list_numbers)
print(list_strings)
print(list_mixed)
print(type(list_players))

# métodos

# append and remove
list_players.remove("Willian Saliba")
injured_players.append("Willian Saliba")
print(list_players)
print(injured_players)

# count
print(injured_players.count("Willian Saliba"))
