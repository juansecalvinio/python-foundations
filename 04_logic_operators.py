# and
player_one = "Eberechi Eze"
player_one_age = 27
player_one_national_team = True

player_two = "Max Dowman"
player_two_age = 15
player_two_national_team = True

player_three = "Myles Lewis-Skelly"
player_three_age = 18
player_three_national_team = True

player_is_injured = False

if player_one_age >= 21 and player_one_national_team:
    print(f"{player_one} can play for the mayor national team.")

if player_two_age >= 21 and player_two_national_team:
    print(f"{player_one} can play for the mayor national team.")
else:
    print(f"{player_two} can play for the U21 national team.")

# or
if player_three_age >= 21 or player_three_national_team:
    print(f"{player_three} plays for the mayor national team.")

# not
if not player_is_injured:
    print(f"{player_one} is ready to play.")
