"""Cara Krug 12/23/2020 cjkrug@dmacc.edu
Final project for python course.
"""
import tkinter
import random
import datetime
import unittest
import self as self
import doctormodule
import constructor
import mysql.connector


#Setup
from pip._vendor.distlib.compat import raw_input

yes_no = ["yes", "Y", "YES", "Yes", "no", "N", "NO", "No"]
directions = ["left", "right", "forward", "backward"]

#==================================================================Chapter One Introduction
name = input("What is your name ensign?")
print("Congrats on your enlistment, " + name + ". As an ensign you are apart of the Starfleet engineering department. ")
print("You find yourself at your station when your system flickers and then shuts down.")
print("The systems are convulsing into mania with sparks and very warm controls.")
print("At that moment a huge burst of electronic outage kills the Chief Engineer. What do you do? Do you find the captain or think it was a mistake joining The Federation and quit.")

response = ""
while response not in yes_no:
    response = input("Would you like to move away from the engineering station?\n please respond lower yes/no\n")
    if response == "yes": #this is an area I fixed
        print("You move away from the station out into the corridor to look for the Captain,\n")
    elif response == "no":
        print("You're not ready to be an ensign, " + name + ".")
        quit()
    else:
        print("Please repeat ensign.\n")

#===================================================================Next part of Chapter 1

response = ""
while response not in directions: #keep an eye on this
    print("To your left you see an empty corridor.")
    print("To your right you see your best friend and other engineering ensign")
    print("Behind you the flickering is now covering all systems")
    print("Forward you see your future collapsing into darkness")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("Well, actually there's an invisible alien that is disrupting the systems. Mostly a being with phasing abilities. You don't know it yet, so you go with your best friend.")
    elif response == "right":
        print("You go with your best friend to find the Captain.\n")            #the many if and else statements.
    elif response == "backward":
        print("You go back and get shocked and die, sorry " + name)
    elif response == "forward":
        print("You get lost in panic and run right")
    else:
        print("There's no crying in Star Trek")

#===============================================================Chapter 2 The Wrap Core mishap

response = ""
print("As you and your best friend Mika go down the ships corridors you both realize the doors are shut and cannot be opened.")
print("So you locate the manual systems for a door to open into the common area.")
print("You push the keys to the machine.")


class Machine: #one of my methods
  def __init__(self, name, number):
    self.name = name
    self.number = number

  def myfunc(self):
    print("Hello this is air lock door " + self.name)

p1 = Machine("U53691", 33)
p1.myfunc()

a = input("Pick a number between 1 and 5\n") #this is supposed to give the user some agency with the story too.
i = 0

while i < len(a): #my while loop
    i += 1
    pass
    print("You have access to this space.\n") #do an else if statement with number

response = ""
print("As you gain access to the common room where crew member's eat and relax, you find it completely empty.")
print("Both of you look around and disbelief at the surrounding area.")
print("Where has everyone gone to?")
print("You're going to call out on your badge for a ship wide call if anybody is alive or present on this ship.")
print("You communicate with your Starfleet badge. Please answer prompt.")

str = raw_input("Enter your input: ")
print ("Received call from Ensign " + name, str)
print("Can't confirm")
print("As both of you start to think about your Starfleet training, you both start to walk towards an exit but remember the doors are still non active.")
print("But then all around you the common room lights and indoor systems around start to flicker again, and all of a sudden the door opens!")

response = ""
while response not in yes_no:
    response = input("Would you like to go through the door?\n please respond lower yes/no\n") #yes or no write
    if response == "yes":
        print("Then both of you travel through the open door.")
    elif response == "no":
        print("Then I guess you both just hang out and play some three-dimensional chess until something happens and end game.")
        quit()
    else:
        print("Don't be a drag.")


#===========================================================Chapter 3 Figuring out what has happened.


print("\n")
print("As the both of you travel down the ship's corridor you make your way to the Bridge")
print("As the both of you are only juniors you both feel alert and stress with a tinge of fear between the brows.")
print("The door to the Bridge is closed as well. So you fiddle with the manual systems to the door as well.")

class Machine1: #one of my methods
  def __init__(self, name, number):
    self.name = name
    self.number = number

  def myfunc(self):
    print("Hello this is air lock door to the Bridge " + self.name)

p1 = Machine1("V10150", 33)
p1.myfunc()

a = input("Pick a number between 1 and 5") #this is supposed to give the user some agency with the story too.
i = 0

while i < len(a): #my while loop
    i += 1
    pass
    print("You have access to this space.") #do an else if statement with number
else:
    print("Or you totally did away with my instructions.")

#=====================================#
#=====================================#

print("\n")
fleet = ["Nana", "Chakotay", "T'Phol"]
captain = input("Please pick a Captain's name: ")
print("As the door opens you see all the senior staff closed in.")
print("As Captain " + captain + " comes towards you they say: ")
for x in fleet:
    print(x)

print("We're missing three senior staff members.")
print("And our Chief Engineer is dead and the majority of our crew is locked between doors or are injured or dead.")

doctormodule.doctor("The Doctor") #my python module import

#===================================#
#===================================#

print("\n")
print("Then a figure appears in front of Captain and crew.")
print("Hello, I am Tinya Wazzo and I'm from Bgztl planet.")
print("We're a species who can phase through objects and few of us can be invisible as well.")
print("We've been at war with two other planets for 4 years\n")


constructor.war("Truth") #my constructor requirement

#=====================================================================Chapter 4 The end yet the Beginning

print("Tinya Wazzo has the identical appearance of a humanoid from the planet Earth.")
print("Tinya speaks: With our predicament surrounding our species and our planet, I as the daughter of our General Captain request for your people's assistance. ")
print("The Captain " + captain + " speaks up: We'd love to help, but how can we if our ship is damaged and our lack of people. We can send a message to Federation for more help.")
print("Tinya Wazzo speaks: We don't have time as we speak, it's either you come with us to help in any way or betray our species.")
print("The Captain " + captain + " looks on towards the alien and says, 'We can't let you take any of our crew members'")
print("The Bgztl alien then targets and shoots the Captain and everyone around you and your friend.\n")

print("As you both stand there and feel the real fear of death very close and you realize that it's not only you but you're bestest friend there as well about to await the next blast.")
print("What do you do?\n")

response = ""
while response not in yes_no:
    response = input("Would you like to combat the alien?\n please respond lower yes/no\n")
    if response == "yes":
        print("You run over to the control systems and overpower the system enough for the electric shock to explode behind and from the side of the alien.")
    elif response == "no":
        print("Well...you're taken with the alien to either start a new life there or fight in their war and die.")
        quit()
    else:
        print("Don't be a guber.")

print("As the alien falls to the floor in pain, with heavy breathing and sweat developing on their brow.")
print("They look as if they're dying.So you pull out your Tricorder to inspect the Alien.")

class Alien: #my class requirment
    def __init__(self, name, age, location, life):
        self.name = name
        self.age = age
        self.location = location
        self.life = life

p1 = Alien("Tinya", 33, "Bgztl", "CRITICAL")

print(p1.name)
print(p1.age)
print(p1.location)
print(p1.life)
x = datetime.datetime.now() #my datetime stamp.
print(x)

print("\n")
print("Tinya then says...")
try: # my exception handling
    print("Hello.")
except:
    print("Something went wrong")
else:
    print("Well, actually nothing went wrong")

print("Tinya jumps shoots and kills Mika, then stares right at your face and runs through the wall and controllers. ")
print("What is happening is everything is flickering, the alarms are going off and on, the ship's main navigation is off and the ship is now pumpting downward.")
print("What do you do? Do you go towards the escape pod station even though it's far away and time is limited. Or do you go down with the ship?")

response = ""
while response not in yes_no:
    response = input("Do you want to go towards the escape pods?\n please respond lower yes/no\n")
    if response == "yes":
        print("Then you run as fast as you can towards the escape pods. With the systems down, the doors are all open and you make it safely out!")
    elif response == "no":
        print("Then you go down with the ship. Good-bye ensign" + name)
        quit()
    else:
        print("Don't be a Feregni")

print("\n")
print("As you escape the ship with your pod, you look at the wreckage of the ship from your little window")

def t1(): #my inner function
    s = 'Good speed and pray for safety'

    def t2():
        s = 'It was an honor to be apart of the Federation.'
        print(s)

    t2()
    print(s)
t1()

def myJourney(*argv): #my args requirment
    for arg in argv:
        print(arg)
myJourney('Log 3872:', 'Ensign ' + name,'Here', 'Saying Goodbye')
# ==========================================================================================================Driver Code

# create a GUI window
root = tkinter.Tk()

from time import strftime

# set the title
root.title("Federation Licensing")

# set the size
root.geometry("500x300")

instructions = tkinter.Label(root, text = "Congrats Ensign you made it through the\n "
                                          "Kobayashi Maru test!", font=('Helvetica', 15))



instructions.pack()



# start the GUI
root.mainloop()

if __name__ == '__main__': #TDD
    myJourney(name)
    unittest.main()
