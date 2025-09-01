player = "Eberechi Eze"
national_team = "England"
shirt_number = 15
is_national_team_player = True
is_captain = False
is_number_10 = False

if is_national_team_player:
    print(f"{player} plays for the {national_team} national team.")
if is_captain:
    print(f"{player} is the captain of the {national_team} national team.")
elif is_number_10:
    print(f"{player} is number #10 of the {national_team} national team.")
else:
    print(f"{player} is not the captain and use number #{shirt_number} of the {national_team} national team.")
