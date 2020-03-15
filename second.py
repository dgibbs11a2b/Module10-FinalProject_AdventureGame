#-------------------------------------
#David Gibbs
#March 8, 2020
#
#Program Name: Adventure Game Project - Second Chapter
#-------------------------------------

#Global Imports
import action
import movement
import fight
import second

#Functions

def chapter_two():
    print(" You are now on sub level 2")
    chapter_two_options = ["1","2","3"]
    user_choice = ""
    #while user_choice not in chapter_two_options:
    print('''what do you want to do?

    1) Walk north toward the dim lights in the distance
    2) stay
    3) Turn aroud and walk south back towards the elevator ''')

        user_choice = str(input("Enter option number: "))
    #print("You have selected " + user_choice)
    if user_choice == chapter_two_options [0]:
        movement.print_north( "north" )
        chapter_one()
    elif user_choice == chapter_two_options [1]:
        movement.print_stay( "stay" )
    elif user_choice == chapter_two_options [2]:
        chapter_five_noRescue


