import sys
from island_pkg.project_lists import *
from island_pkg.project_functions import *


while True:
    print("Welcome to the Deserted Island! Do you think that you can survive the night?")
    print("1) Play game")
    print("2) Exit")
    option = input("Choose an option: ")

    if option == "1":
        name = input("What is your name?: ")
        print("Hello", name + "!")
        break
    elif option == "2":
        sys.exit("Goodbye!")
    else: 
        print("That is not a valid choice.")

while True:
    print("You have just woken up on a deserted island with no idea what happened." , 
    "\nYou look around and realize that you must have gotten into a plane crash.")
    print("\nNow that your memory has started to come back to you, you realize that you need to collect supplies." ,
    "\nThe only things you see around you are (1) a glass shard, (2) a pipe, (3) a first-aid kit, (4) a backpack, and (5) a waterbottle.")
    while True:  
        carry_item = input("\nYou know that you will only be able to carry one item with you, which do you choose? ")
        if carry_item == "1":
            my_item = supplies_list[0]
            my_xp = glass_xp
            print("You have chosen the", my_item + ". With this item, you have gained", glass_xp, "survival points.")
            break
        elif carry_item == "2":
            my_item = supplies_list[1]
            my_xp = pipe_xp
            print("You have chosen the", my_item + ". With this item, you have gained", pipe_xp, "survival points.")
            break
        elif carry_item == "3":
            my_item = supplies_list[2]
            my_xp = first_aid_kit_xp
            print("You have chosen the", my_item + ". With this item, you have gained", first_aid_kit_xp, "survival points.")
            break
        elif carry_item == "4":
            my_item = supplies_list[3]
            print("You have chosen the", my_item + ". With this item, you have gained", backpack_xp, "survival points.",
            "\nThis item allows you to fit (1) the glass shard or (2) the watterbottle inside of it, with some extra room.")
            backpack1 = input("Which of those items do you choose? ")
            if backpack1 == "1":
                my_item = supplies_list[5]
                my_xp = backpack_pipe_xp
                print("Your new amount of survival points is:", backpack_pipe_xp)
            elif backpack1 == "2":
                my_item = supplies_list[6]
                my_xp = backpack_water_xp
                print("Your new amount of survival points is:", backpack_water_xp)
            else:
                print("Invalid selection, try again.")
            break
        elif carry_item == "5":
            my_item = supplies_list[4]
            my_xp = waterbottle_xp
            print("You have chosen the", my_item + ". With this item, you have gained", waterbottle_xp, "survival points.")
            break
        else:
            print("Invalid selection, try again.")

    print("\nThe first thing that you decide is that you need to find a shelter for the night.")
    while True:
        shelter_location = input("Do you want to go (1) into the woods or (2) stay on the beach? ")
        if shelter_location == "1":
            my_shelter = shelter_list[0]
            print("You have chosen to go into the woods and you build your shelter out of fallen branches and dry leaves.")
            break
        elif shelter_location == "2":
            my_shelter = shelter_list[1]
            print("You have chosen to stay on the beach and you build your shelter out of rocks and twigs.")
            break
        else:
            print("Invalid selection, try again.")

    print("\nNow that you have built your shelter, you hear your stomach rumbling.\nIt is time to hunt for food.")
    print("\nYou start walking around the woods and you notice some potential food items.",
    "\nOn the left, you see a bush full of berries. And on the right you hear a sleeping fawn.",
    "\n(You have never hurt an animal in your life, but this might be your only chance of survival.)")
    while True:
        food = input("Which do you choose (1) berries or (2) fawn? ")
        if food == "1":
            if my_item != supplies_list[2]:
                sys.exit("\nLooks like those berries were poisonous and you did not have the first-aid kit.\nYou were unable to survive the night.")
            else:
                print("\nThe berries were poisonous, but you had the", my_item, "which saved your life.")
                break
        elif food == "2":
            battle(my_item, my_xp, fawn_xp)
            break
        else:
            print("Invalid selection, try again.")

    print("\nOn your way back to your shelter, you hear a river and realize you are thirsty.")
    if my_item == supplies_list[4] or my_item == supplies_list[6]:
        my_xp += 50
        print("Because you chose the waterbottle, you are able to fill it up and drink the water.")
        show_xp(my_xp)
    else:
        my_xp -= 50
        print("You did not choose the waterbottle so you are not able to get any water.")
        show_xp(my_xp)
    
    print("\nYou have now come across a blanket that might be useful.")
    if my_item == supplies_list[5] or my_item == supplies_list[6]:
        my_xp += 50
        print("Because you chose the backpack, you are able to pick up the blanket and take it with you.")
        show_xp(my_xp)
    else:
        my_xp -= 50
        print("You did not choose the backpack so you are not able to take the blanket with you.")
        show_xp(my_xp)

        #FIX this the xp should have changed from the battle
    print("\nYou have finally arrived at your shelter for the night just in time for the sun to set.",
    "\nIt is getting very cold and you need to gain some warmth.")
    while True:
        warmth = input("Because you are getting very cold, you have the option to (1) start a fire or (2) no fire. ")
        if warmth == "1":
            if my_shelter == shelter_list[0]:
                if my_item == supplies_list[5] or my_item == supplies_list[6]:
                    print("\nYour shelter was built using dry leaves, the fire has destroyed your shelter.\nHowever, you have a blanket to keep you warm through the night.")
                    break
                else:
                    sys.exit("\nYour shelter was built using dry leaves, the fire has destroyed your shelter and you did not have a blanet to keep warm.\nYou were unable to survive the night.")
            if my_shelter == shelter_list[1]:
                if my_item == supplies_list[5] or my_item == supplies_list[6]:
                    print("\nYou were able to build a fire because your chose to put your shelter on the beach. You also have a blanket to keep you warm.")
                    break
                else:
                    print("\nYou do not have a blanket, but you were able to build a fire because your chose to put your shelter on the beach and keep you warm.")
                    break
        elif warmth == "2":
                if my_item == supplies_list[5] or my_item == supplies_list[6]:
                    print("\nYou did not build a fire. However, you have a blanket to keep you warm through the night.")
                    break
                else:
                    sys.exit("\nYou did not build a fire or have a blanet to keep warm.\nYou were unable to survive the night.")
        else:
            print("Invalid selection, try again.")

    print("\nYou wake up in the morning to sounds of a ship coming to your rescue.",
    "\nCongratulations! You have survived the night on this island and won the game with", my_xp, "survival points.")
    break