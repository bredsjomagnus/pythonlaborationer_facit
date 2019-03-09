#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ae949ef06c305dd1bd7f4af13bf76a11
python
lab2
maaa16
2016-01-29 05:52:53
v2.0.1x (2015-09-29)

Generated 2016-01-29 06:52:54 by dbwebb lab-utility v2.0.1x (2015-09-29).
https://github.com/mosbth/lab
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 2 - python 
 
Strings and files 
"""

"""
--------------------------------------------------------------------------
Section 1. Strings 
 
The basics of strings 
"""

"""
Exercise 1.1 
 
Assign the word: 'lemonade' to a variable and put your variable as the
answer. 

Write your code below and put the answer into the variable ANSWER.
"""
result = "lemonade"

ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Assign the word 'lemonade' to a variable. Create another variable where you
put the first and the last letter in the word. Answer with the second
variable. 

Write your code below and put the answer into the variable ANSWER.
"""
result2 = result[:2]

ANSWER = result2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Assign the word: melon to a variable. Answer with the length of the word as
an integer. 

Write your code below and put the answer into the variable ANSWER.
"""

word1 = "melon"



ANSWER = len(word1)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Use the 'in-operator' to see if the word: 'train' contains the letter 'a'.
Answer with a boolean result. 

Write your code below and put the answer into the variable ANSWER.
"""

result3 = "a" in "train"

ANSWER = result3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Make all the letters in the word 'melon' capitalized. Answer with the
capitalized word. 

Write your code below and put the answer into the variable ANSWER.
"""
word2 = "melon"
word3 = ""
for letter in word2:
    word3 = word3 + letter.capitalize()
    
ANSWER = word3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Use the built-in function 'startswith()' to see if the word 'lemonade'
starts with the letter 'e'. Answer with the boolean value. 

Write your code below and put the answer into the variable ANSWER.
"""

word4 = "lemonade"




ANSWER = word4.startswith("e")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Assign the words: 'lemonade' and 'onion' to two different variables. Create
a function and pass the two words as arguments to it. Your function should
return them as a single word. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""


def wordanizer(w1, w2):
    '''
    Sammansätter två ord till ett
    '''
    return w1+w2

word5 = "lemonade"
word6 = "onion"

ANSWER = wordanizer(word5, word6)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create a function and pass the word: 'lemonade' to it. Your function should
return the sentence: 'This word was: lemonade'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
def thisWordWas(w3):
    '''
    Lägger till this word was på argument
    '''
    word7 = "This word was: " + w3
    return word7




ANSWER = thisWordWas("lemonade")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Create a function and pass the word: 'onion' to it. Your function should
return the string 'yes' if the word is longer than 5 characters. Else
return 'no'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

def isWordLength(w4):
    '''
    kollar om ordet är mer än 5 bokstäver långt
    '''
    if len(w4) < 6:
        result4 = "no"
    else:
        result4 = "yes"
    return result4



ANSWER = isWordLength("onion")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Create a function and pass the word: 'melon' to it. Your function should
return a string with the word backwards. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
def wordBackwards(w5):
    '''
    Returnerar ordet baklänges
    '''
    word9 = ""
    for letter2 in w5:
        word9 = letter2 + word9
    
    return word9



ANSWER = wordBackwards("melon")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11 
 
Create a function and pass the word: 'lemonade' to it. Your function should
exclude the first and the last letter of the word and return it. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
def cutWord(w6):
    '''
    Kapar första och sista bokstaven och returnerar
    '''

    cuttedword = w6[1:len(w6)-1]
    return cuttedword

ANSWER = cutWord("lemonade")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
Exercise 1.12 
 
Use str.format() to print out: 'My 'string' has 'integer' 'string''. Use
the values: 'brother', '2' and 'dogs'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word10 = "My {} has {} {}".format("brother", 2, "dogs")

ANSWER = word10

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.12", ANSWER, False))

"""
Exercise 1.13 
 
Use 'find' and 'slice' on the string: '154.84.56.0 : (wallpaper), soda' to
get the word inside the parenthesis. Answer with the word as a string. 

Write your code below and put the answer into the variable ANSWER.
"""
word11 = "154.84.56.0 : (wallpaper), soda"
firstparenestindex = word11.find("(")+1
secondparentesindex = word11.find(")")

wordinsideparentes = word11[firstparenestindex:secondparentesindex]




ANSWER = wordinsideparentes

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Files 
 
This section uses the text file: 'httpd-access.txt' 
"""

"""
Exercise 2.1 
 
Open the file and count the number of times a line starts with '81'. Answer
with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""

fh = open("httpd-access.txt", "r")
c = 0
for line in fh:
    if line.startswith('81'):
        c += 1
fh.close()
ANSWER = c

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Find out the last 4 digits on line 821 in the file. Answer with the result
as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
fh = open("httpd-access.txt", "r")

counter = 0
for line in fh:
    counter += 1
    if counter == 821:
        starters = line[len(line)-5:len(line)-1]
    
            
fh.close()
ANSWER = int(starters)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Find out which of the ip adresses 81.226.253.26 and 95.19.133.73 that has
the highest amount of entries in the file. Answer with the result as an
integer. 

Write your code below and put the answer into the variable ANSWER.
"""
fh = open("httpd-access.txt", "r")
counter81 = 0
counter95 = 0
for line in fh:
    if line.startswith("81.226.253.26"):
        counter += 1
    elif line.startswith("95.19.133.73"):
        counter95 += 1
if counter81 < counter95:
    result5 = counter95
else:
    result5 = counter81


fh.close()
ANSWER = result5

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Count the number of periods (.) there are in the file. Use the built-in
function count() on the file after you have converted it to a string.
Answer with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
fh = open("httpd-access.txt", "r")

filen = fh.read()

punkter = filen.count(".")
fh.close()
ANSWER = punkter

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Find the characters on line 637 from index 65 to index 75. Make sure that
the character at index 75 also gets included. Answer with the piece of
string you found. 

Write your code below and put the answer into the variable ANSWER.
"""
fh = open("httpd-access.txt", "r")
counter = 0
for line in fh:
    counter += 1
    if counter == 637:
        partofline = line[65:76]
    
            
fh.close()




ANSWER = partofline

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Find the last element (digit) on each line, if there are any, and sum all
that are even. Answer with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
fh = open("httpd-access.txt", "r")

summa = 0
for line in fh:
    last = line[len(line)-2:len(line)-1]  
    if last.isdigit():
        lastint = int(last)
        if lastint%2 == 0:
            summa = summa + lastint
        
        
fh.close()


ANSWER = summa

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))


dbwebb.exitWithSummary()
