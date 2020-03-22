#-------------------------------------
#David Gibbs
#March 22, 2020
#
#File Name: TheAlienAdventure.py
#Game: The ALIEN Adventure
#-------------------------------------

#Global Imports

import action
import movement
import fight
import finale
import queen
import title
import time


#Functions

def cls():
    print("\n" * 60)

def pause():
    programPause = input("Press the <ENTER> key to begin...")

def begin():
    programBegin = input("\nPress <ENTER> to start the game...")
    
def resume():
    programResume = input("\n Press the <ENTER> key to continue...")

def game_Over():
    print("\n \n --> The Game Is Over")
    game_Over_options = ["1","2"]
    user_choice = ""
    while user_choice not in game_Over_options:
        print(
'''\nRebecca needs your help''',(person),'''\nWould you like to try The ALIEN Adventure again\n?

What do you do?

    1) Play Again
    2) Quit\n''')
        
        user_choice = str(input("Enter option number: "))
        print("\nYou have selected " + user_choice)
        if user_choice == game_Over_options [0]:
            cls()
            time.sleep(2.0)
            chapter_one() 
        elif user_choice == game_Over_options [1]:
            print("\n \nThank You for playing The ALIEN Adventure")
        elif user_choice != game_Over_options:
            print("\nThat was an incorrect choice. Please try again\n")
            time.sleep(3.5)
            cls()
            game_Over()

#Breaks the loop after choosing an incorrect response
        break

cls()

title.print_startTitle( "startTitle" )

count = 0
while(count < 10):
	print("")
	count += 1


begin()

#cls()

#count = 0
#while(count < 20):
	#print("")
	#count += 1

person = input('\nWhat is your name?: ')
greeting = 'Hello {}!'.format(person)
cls()

print(greeting)

print('''\nThis is a text based adventure game called ALIEN. You have assumed the role of the main character in the game,LT. Helen Riley.
Your mission will challenge you to travel deep into the Alien layer to rescue your friend Rebecca, and then escape before
the atmospheric processors explode. Every choice you make will determine Riley's actions and the plot's outcome.
\n \nGood luck!\n \n \n \n \n''')          

pause()


cls()

def chapter_one():
    chapter_one_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in chapter_one_options:
        print(
'''\nIt was the year 2045. Lieutenant Helen Riley, a warrant officer formerly assigned to the USCSS Nostradamus,
an M-Class Star freighter touched down on FURY-161 to home in a on a distress beacon from a derelict spacecraft.
Helen and her team discover that the spacecraft belonged to a dangerous alien species. The crew set down on the
planet and one of the crew members had to be rescued after he was attacked. He was brought back to the ship with
something attached to his face; some sort of alien species. The alien used the crew member's body as a host for a
new Alien. The creatures exploded through the crew member's chest and escaped into the ducts of the ship, only to
grow to an enormous size over a period of 2 weeks. The creature invaded her and her team’s ship, eliminating each
member one by one. Helen, knowing that she didn't have a chance against the creature, abandoned the ship before
becoming its final victim.She escaped on a lifeboat vessel, after detonating aand destroying the star freighter,
and the alien creature with it. She sought refuge in the lifeboat and drifts through space for a period of 57
years in hyper sleep until finally being rescued by a salvage team.\n''')
        resume()
        cls()

        print(

'''\nIt is now 2102. The once desolate planet, FURY161, is now home to a terraforming
colony with 75 families. Surrounding the base are large atmospheric processors
to help make the air breathable for its inhabitants. The recent silence from
the colony is un-nerving. No one has been able to contact these families for weeks.
Riley, last survivor of the Nostradamus incident from years past, and an employee of
the Weyland Markham corporation goes through the company debriefing and goes back to
her quarters to unwind. Riley receives the news of the latest loss of communications
an is asked by the company to accompany the team of specially trained marines to
travel down to the planet and establish contact with the colony. Once on the planet,
they discover that the entire colony has disappeared and, in their attempts, to search
for any survivors, they encounter an alien species which totally wipes out the majority
of their team. now she must make a choice to leave the planet with the remaining survivors,
Corporal Hickson, Cardinal the android, or travel deep into the Alien nest to locate the only remaining.
survivor, Rebecca, a young girl that Riley had befriended during the initial visit.
During the battle on FURY-161, Riley and Rebecca became separated and Rebecca has now
been taken by the alien creatures soon to be made a host for creating new alien creatures.\n''')
        resume()
        cls()

        print(

'''\nWe cut directly to the scene where Cardinal, piloting the rescue ship, lands on the
platform many stories up where there is an elevator which leads down to the alien nest.
This elevator can be taken down to where Rebecca is being held.
During the earlier battle, Riley placed a tracking beacon on Rebecca in order to track
her whereabouts in the event they become separated. The determined Riley, armed with
an assault rifle and a flame thrower, is now challenged with a race against the clock
to find Rebecca and escape before the meltdown of the unstable atmospheric reactor explodes.
It would cause a cloud of poisonous vapor the size of Texas, killing all forms of life on the planet.
Cardinal lands the dropship onto the platform near a service entrance. There is a cargo elevator there.
On top of the landing platform, the unstable atmospheric processor is on fire.

Riley, determined to find her friend, is surrounded by exploding shards of metal from the refinery,
and there is only one way into the nest, through the elevator. Riley deploys from the dropship and approaches the elevator.

-->  You are now on the landing platform facing the cargo elevator

What do you do??

    1) Stay on the platform
    2) Press the 'down' button on the cargo elevator, go down to sub level 2
    3) Turn around, board the dropship, take off and abandon the rescue operation. \n''')

        user_choice = str(input("Enter option number: "))
        print("\nYou have selected " + user_choice)
        if user_choice == chapter_one_options [0]:
            movement.print_stay( "stay" )
            time.sleep(4.5)
            cls()
            chapter_one()
        elif user_choice == chapter_one_options [1]:
            action.print_downElev( "downElev" )
            time.sleep(4.5)
            cls()
            chapter_two()
        elif user_choice == chapter_one_options [2]:
            time.sleep(4.5)
            cls()
            finale.print_noRescue( "noRescue" )
            game_Over()
        elif user_choice != chapter_one_options:
            print("\nThat was an incorrect choice. Please try again\n")
            time.sleep(3.5)
            cls()
            chapter_one()

#Breaks the loop after choosing an incorrect response
        break
          

def chapter_two():
    print(" \n \n -->  You are now on sub level 2")
    chapter_two_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in chapter_two_options:
        print(
'''\nRiley stands at the opening of the Alien nest, it is dark, steamy, and filled with
the stench of dead bodies. As she begins her search for Rebecca, she observes her surroundings
on Sub level 2 and sees what appears to be a cavern that leads into an area with dim lighting.

What do you do?

    1) Walk north toward the dim lights in the distance, drop a marking flare
    2) Stay
    3) Abandon the mission, turn around and walk south back to the elevator, take the elevator to escape.\n''')

        user_choice = str(input("Enter option number: "))
        print("\nYou have selected " + user_choice)
        if user_choice == chapter_two_options [0]:
            movement.print_north( "north" )
            time.sleep(5.5)
            cls()
            chapter_three()
        elif user_choice == chapter_two_options [1]:
            movement.print_stay( "stay" )
            time.sleep(4.5)
            cls()
            chapter_two()
        elif user_choice == chapter_two_options [2]:
            action.print_upElev( "upElev" )
            time.sleep(4.5)
            cls()
            finale.print_noRescue( "noRescue" )
            game_Over()
        elif user_choice != chapter_two_options:
            print("\nThat was an incorrect choice. Please try again\n")
            time.sleep(3.5)
            cls()
            chapter_two()

#Breaks the loop after choosing an incorrect response
        break

def chapter_three():
    print(" \n \n --> You are now in Chapter 3, immersed deep into the Alien nest on sub level 2")
    chapter_three_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in chapter_three_options:
        print(
'''\nHeading deeper into the catacombs of the Alien nest, Riley hears the fast pace
chime of the location beacon which indicates that Rebecca is close. Frantically searching, she comes
upon the location beacon and realizes that it's on the ground but Rebecca is nowhere to be found.
Rebecca sees the hatching of an Alien egg where a chest bursting alien is about to attack her.
She begins screaming wildly for help and Riley hears the call of her desperate cry which alerts
some alien soldiers nearby. Riley quickley gets rid of them with her assault rifle”

What do you do?

    1) Proceed to sub level 3, run deeper into the Alien nest, help Rebecca and take her by the hand
    2) Stay where you are
    3) Turn around and go back upstairs to sub level 2.\n''')

        user_choice = str(input("Enter option number: "))
        print("\nYou have selected " + user_choice)
        if user_choice == chapter_three_options [0]:
            movement.print_northDownSub3( "northDownSub3" )
            time.sleep(4.5)
            cls()
            chapter_four()
        elif user_choice == chapter_three_options [1]:
            movement.print_stay( "stay" )
            time.sleep(4.5)
            cls()
            chapter_three()
        elif user_choice == chapter_three_options [2]:
            movement.print_southUpSub2( "southUpSub2 ")
            time.sleep(4.5)
            cls()
            chapter_two()
        elif user_choice != chapter_three_options:
            print("\nThat was an incorrect choice. Please try again\n")
            time.sleep(3.5)
            cls()
            chapter_three()

#Breaks the loop after choosing an incorrect response
        break

def chapter_four():
    print("\n \n --> You are now in Chapter 4 on sub level 3")
    chapter_four_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in chapter_four_options:
        print(
'''\nYou've found Rebecca. But, you are running out of time! Let's get out of here! 
In your frantic efforts to escape, an explosion blocks you from going back from where you came.
Still heading south, you take a different path back towards the south cargo elevators on sub level 3
only to discover you have intruded upon the Alien queen’s nest and your are surrounded by alien eggs.

Your presence has interrupted her egg laying and she sees you as a threat.
The queen recognizes you are rescuing Rebecca and just trying to pass through, but you threaten to
destroy her eggs if she doesn't let you pass.
She gets the hint, and she calls off her alien henchman while allowing to proceed.

What do you do?

    1) Turn around and walk south towards the elevator on sub level 3 without disturbing the nest.
    2) Stay where you are
    3) Clear a path with your flamethrower, while walking south, kill aliens, destroy eggs, then
    run south towards sub level 3 elevator.\n''')

        user_choice = str(input("Enter option number: "))
        print("\nYou have selected " + user_choice)
        if user_choice == chapter_four_options [0]:
            movement.print_noDisturb( "noDisturb" )
            time.sleep(4.5)
            cls()
            chapter_five()
        elif user_choice == chapter_four_options [1]:
            movement.print_stay( "stay" )
            time.sleep(4.5)
            cls()
            chapter_four()
        elif user_choice == chapter_four_options [2]:
            action.print_useFlame( "useFlame" )
            fight.print_killAliens( "killAliens")
            movement.print_destroy( "destroy" )
            time.sleep(10.5)
            cls()
            chapter_five()
        elif user_choice != chapter_four_options:
            print("\nThat was an incorrect choice. Please try again\n")
            time.sleep(3.5)
            cls()
            chapter_four()

#Breaks the loop after choosing an incorrect response
        break


def chapter_five():
    print("\n \n --> You are now in Chapter 5 on sub level 3")
    chapter_five_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in chapter_five_options:
        print(
'''\nYou’ve reached the Cargo elevator however you are unaware that the Alien queen is slowly trailing behind you.
You listen to the sqwak of the overhead automated announcement that you have four minutes
to reach minimum safe distance before the unstable atmospheric processor explodes. You hhear the pulsating pounding
of the Alien queen's footsteps. It's too dark to see her, but you hear the cry of a scourned creature seeking revenge on you.

What do you do?

    1) Press the up elevator button, avoid the queen, close the door and proceed to the landing platform
    2) Stay on sub level 3
    3) Turn around and use the flamethrower to kill the Alien Queen\n''')
        
        user_choice = str(input("Enter option number: "))
        print("\nYou have selected " + user_choice)
        if user_choice == chapter_five_options [0]:
            action.print_upElev( "upElev ") 
            time.sleep(4.5)
            cls()
            finale.print_ending( "ending ")
            time.sleep(2.0)
            print("\n \nThank You for playing The ALIEN Adventure")
        elif user_choice == chapter_five_options [1]:
            movement.print_stay( "stay" )
            time.sleep(4.5)
            cls()
            chapter_five()
        elif user_choice == chapter_five_options [2]:
            time.sleep(3.5)
            action.print_useFlame2( "useFlame2" )
            time.sleep(5.5)
            cls()
            queen.print_queenAttack( "queenAttack" )
            fight.print_killQueen( "killQueen")
            time.sleep(10.5)
            cls()
            chapter_five()
        elif user_choice != chapter_five_options:
            print("\nThat was an incorrect choice. Please try again\n")
            time.sleep(3.5)
            cls()
            chapter_five()
#Breaks the loop after choosing an incorrect response                              
        break            

#Main Program
	
chapter_one()

