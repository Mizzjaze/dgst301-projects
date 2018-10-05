#The Letters.py
#By: Jasmyn Y. Oliver
#
#

from textblob import TextBlob #imports Textblob module
import random #imports random module
import pycorpora #imports pycorpora library
import pronouncing #imports Pronouncing module


#Defines function to select random types of 'passages' from pycorpora data set
def get_entry():
    #word_list = [pycorpora.architecture.passages['passages'],pycorpora.architecture.rooms['rooms']]
    ewords = []
    for entry in pycorpora.architecture.rooms['rooms']:
        plist = pronouncing.phones_for_word(entry)
        if(len(plist)> 0):
            scount = pronouncing.syllable_count(plist[0])
            if (scount == 2):
                ewords.append(entry)
    return ewords
        
##    entry = random.choice(pycorpora.architecture.passages['passages'])
##    plist = pronouncing.phones_for_word(entry)
##    scount = pronouncing.syllable_count(plist[0])
##    return entry

# Defines function to select random types of 'objects' from pycorpora data set
def get_object():
    owords = []
    for ranobject in pycorpora.objects.objects['objects']:
        plist = pronouncing.phones_for_word(ranobject)
        if(len(plist)> 0):
            scount = pronouncing.syllable_count(plist[0])
            if (scount ==2):
                owords.append(ranobject)
##    ranobject = random.choice(pycorpora.objects.objects['objects'])
##    plist = pronouncing.phones_for_word("tool")
##    scount= pronouncing.syllable_count(plist[0])
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
##    poem = template.format(get_object(), get_entry())
##    for i in range(4):
##        low_rhyme = pronouncing.rhymes(get_object(),get_entry())
##
##        write_rhyme = random.choice(pronouncing.rhymes("write"))
##
##        print(poem.format(low_rhyme,write_rhyme))
##
##    poem = poem.format(get_object(), get_entry())
##
    
    print(poem)

main()
