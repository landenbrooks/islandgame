def battle(my_item, my_xp, fawn_xp):
    if my_xp > fawn_xp:
        my_xp += 50
        print("\nYou have used your", my_item, "to win the battle with the fawn and are able to fill your stomach.")
        show_xp(my_xp)
    else:
        my_xp -= 50
        print("\nYou have lost the battle with the fawn because your", my_item, "was not powerful enough and you were not able to eat anything.")
        show_xp(my_xp)

def show_xp(my_xp):
    print("You now have", my_xp, "survival points.")