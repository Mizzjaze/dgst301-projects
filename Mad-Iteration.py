###Mad-Iteration.py
###This program is a poem generator
###It is part of a poem remix project for my Creative Coding course
###It is inspired by hip-hop artist/producer MF Doom's album MM..FOOD (2007)

##imports Python random module
import random

##The following lists will populate lines of poetry when the program is executed
##lines[] includes nouns I inputted that are related to eating and/or food
##This list includes selected line breaks after certain items
lines = [
    "cafe\n","booth\n", "restaurant", "bistro\n", "kitchen\n", "market\n","din-din\n",
    "suppertime\n","counter\n", "service\n", "lunch pack\n", "recipe\n", "menu\n",
    "hostess\n", "monkey suit","barkeep\n", "waitresses", "frycook",
    "pub\n","table\n", "diner\n", "take-out\n", "doggy bag\n", "leftovers"
]
##lines2[] includes food dishes referenced in the album (MM..FOOD)
##Includes adjectives/adverbs I inputted for added description
##This list includes selected line breaks after certain items
lines2 = ["hot johnny cakes!","steaming shoofly","yearning for beef wraps","delicious ragu",
           "mealy couscous", "enourmous beef patty", "eighty-six the coco bread", "glistening queso",
           "dripping caramel", "shaved coconuts", "fresh baked samoas", "tasty snack cakes",
           "spicy knishes", "savory pudding"," verdant herbs", "beets\n"
]
##lines3[] includes the album's full tracklist as it appears
##List includes selected line breaks after certain items
lines3 = ["Beef Rap\n", "Hoe Cakes\n", "Potholderz","One Beer",
          "Deep Fried Frenz\n", "Poo-Putt Platter\n", "Poo-Putt Platter\n",
          "Fillet-O-Rapper\n", "Gumbo", "Fig Leaf Bi-Carbonate",
          "Kon Karne", "Guinesses\n", "Kon Queso", "Rapp Snitch Knishes",
          "Vomitspit", "Kookies"
]
##lines4[] includes list of verbs
lines4 = ["eat", "want", "grub", "cop", "butter", "nibble", "pick-up",
          "order", "cook", "prep"
]

##main function
def main():
#Prints poem title/author
#Prints a short intro on what the program does
    
    print("Mad-Iteration By: Jasmyn Y. Oliver\n*This poem will change everytime you run this program\n")

   #Loops through lines3[], lines[], and lines2[] to output poem lines
   #Prints randomly selected items using random.choice call from random module 
    for l in range(22):
        print ((random.choice(lines)),(random.choice(lines4)),(random.choice(lines2)),(random.choice(lines3)))
   #Prints a line break after the poem for spacing
    print("\n")
   #Prints a special thank you indicating the end of the poem
    print("Special thanks to MF DOOM for making MM...FOOD.\n Thank you for providing poetic inspiration.")

main()
