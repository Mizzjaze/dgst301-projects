#The Letters.py
#By: Jasmyn Y. Oliver
#
#

from textblob import TextBlob #imports Textblob module
import random #imports random module
import pycorpora #imports pycorpora library
import pronouncing #imports Pronouncing module


#Defines function to select random types of 'rooms' from pycorpora data set
def get_entry():
    ewords = []
    for entry in pycorpora.architecture.rooms['rooms']:
        plist = pronouncing.phones_for_word(entry)
        if(len(plist)> 0):
            scount = pronouncing.syllable_count(plist[0])
            if (scount == 2):
                ewords.append(entry)
    return ewords
        
# Defines function to select random types of 'objects' from pycorpora data set
def get_object():
    owords = []
    for ranobject in pycorpora.objects.objects['objects']:
        plist = pronouncing.phones_for_word(ranobject)
        if(len(plist)> 0):
            scount = pronouncing.syllable_count(plist[0])
            if (scount ==2):
                owords.append(ranobject)
    return owords

def rhyme():
    #function gets pair of 1 entry and 1 object that rhyme

    entries = get_entry()
    objects = get_object()

    pairs = []

    for e in entries:
        for o in objects:
            if (e in pronouncing.rhymes(o)):
                pairs.append((e,o))

    return pairs    

#Defines main function
def main():
    #Poem template
    #Features an A,B,A,B meter marked by 4,5,4,5 syllables per line
    template = "Where do we go? \nI don't have a {0} \nThe lake is cold \nWe need a {1}"
    pair = random.choice(rhyme())
    poem = template.format(pair[0],pair[1]) 
    
    print(poem)

main()
