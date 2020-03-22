#----------------------------------------
#David Gibbs
#March 1, 2020
#
#This module contains functions which can be
#called by the interpreter to execute player,
#Riley's movements
#----------------------------------------


def print_north( north ):
   print ("\nRiley lights a marking flare, drops it on the ground, and she proceeds to walk north")   
   return
#- Moves Riley north to her next destination


def print_south( south ):
   print ("\nRiley walks south")   
   return
#- Moves Riley south to her next destination

def print_destroy( destroy ):
   print (
'''\nRiley clears a path with her flamethrower while she heads south. She destroys
Aliens, roasting alien eggs, and she heads for the sub level 3 elevator''')
# Sends Riley on a killing spree while she makes her way back to the sub level 3 elevator  

def print_noDisturb( noDisturb):
   print (
'''\nRiley walks south towards the cargo elevator on sub level 3
carefully without disturbing the nest''')
#Moves Riley toward the elevator on sub level 3 without disturbing the nest
          
def print_southToElev( southToElev ):
   print ("\nRiley walks south towards the cargo elevator")   
   return
#- Moves Riley south to her next destination


def print_stay( stay ):
    print ("\nRiley stays right where she's at")   
    return
#- Riley stays and does not move


def print_turnAround( turnAround ):
    print ("\nRiley turns around 180 degrees")   
    return
#- Moves Riley 180 degrees


def print_northDownSub2( northDownSub2 ):
   print ("\nRiley walks north to go downstairs to sub level 2")   
   return
#- Moves Riley north to go downstairs to sub level 2 


def print_northDownSub3( northDownSub3 ):
   print ("\nRiley walks north to go downstairs to sub level 3; she sees Rebecca")   
   return
#- Moves Riley north to go downstairs to sub level 3


def print_southUpSub2( SouthUpSub2 ):
   print ("\nRiley walks south to go upstairs to sub level 2")   
   return
#- Moves Riley south to go upstairs to sub level 2 


def print_escape( escape ):
    print ("\nRiley boards the rescue ship and escapes the planet")   
    return
#- Riley escapes the planet

