##Program generates a 50k novel for NaNoGeno 2018 submission
##Novel is a mash-up of "The Fall of the House of Usher" by Edgar A. Poe
##and "Alice in Wonderland" by Lewis Carroll


import random  #imports random library
import markovify  #imports markovify library source in GitHub
import dominate  #imports dominate library source in GitHub
from dominate.tags import *  #from dominate library

novel = '' #Set variable for novel as a string for text manipulation

with open("poe-alice.txt") as f: #Opens file with 'f' as the variable. Text file contains combined texts of "The Fall of the House of 
                                 #Usher", by Edgar A. Poe and "Alice in Wonderland", by Lewis Carroll.  
    text = f.read()
    
# Build the model using Markovify library
text_model = markovify.Text(text)

# Print 2005 randomly-generated sentences using Markovify Library
#Loop produces a novel with approx. 54k word count  
for i in range(2005):
    
    novel += str(text_model.make_sentence()) + " "
    
    r = random.randint(0,100) #Using random to choose a no. between 1-100
    if (r < 25):              #About 25% of the time inserts line breaks to produce paragraphs
        novel += "\n\n"  
    


paragraphs = novel.split('\n\n')

#Uses dominate to tag novel with html/css for style
#Allows for saving output as an html file
doc = dominate.document(title='The Fall of the House of Alice')


with doc.head:
    style('body  {background-color: red; color: white}') #CSS sets background color of novel to red & text to white for testing
    

with doc:
    for i in paragraphs:
        p(i)
        
        
#print(doc)
