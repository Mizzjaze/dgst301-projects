###Mad-Iteration.py
###Poem remix project

import random

lines = [
    "cafe","booth", "restaurant", "bistro", "kitchen", "market","din-din",
    "suppertime","grub", "counter", "service", "lunch pack", "recipe", "menu",
    "reservation", "hostess", "monkey suit\n","barkeep", "waitresses", "frycook",
    "pub\n","table", "diner", "take-out\n", "doggy bag", "leftovers"
    
]
lines2 = ["hot johnny cakes!","steaming shoofly","yearning for beef wraps","delicious ragu",
           "mealy couscous", "enourmous beef patty", "eighty-six the coco bread", "glistening queso",
           "dripping caramel", "shaved coconuts", "fresh baked samoas", "tasty snack cakes",
           "spicy knishes", "savory pudding"," verdant herbs", "beets\n"
]
lines3 = ["Beef Rap\n", "Hoe Cakes\n", "Potholderz","One Beer",
          "Deep Fried Frenz\n", "Poo-Putt Platter\n", "Poo-Putt Platter\n",
          "Fillet-O-Rapper\n", "Gumbo", "Fig Leaf Bi-Carbonate",
          "Kon Karne", "Guinesses\n", "Kon Queso", "Rapp Snitch Knishes",
          "Vomitspit", "Kookies"
]



def main():
#poem title/author
    print("Mad-Iteration By: Jasmyn Y. Oliver\n*This poem will change everytime you run this program\n")

    #loops through lists to output poem lines
    for l in range(22):
        print ((random.choice(lines3)),(random.choice(lines)),(random.choice(lines2)))
    print("\n")
    print("Special thanks to MF DOOM for making MM...FOOD.\n Thank you for providing poetic inspiration.")

main()
