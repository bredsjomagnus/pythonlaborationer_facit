#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
f99080029aebc8e12642f9cdf7a084ca
python
lab4
maaa16
2016-02-15 10:05:08
v2.0.1x (2015-09-29)

Generated 2016-02-15 11:05:09 by dbwebb lab-utility v2.0.1x (2015-09-29).
https://github.com/mosbth/lab
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 4 - python 
 
Dictionaries and tuples 
"""

"""
--------------------------------------------------------------------------
Section 1. Dictionaries 
 
Some basics with dictionaries. 
"""

"""
Exercise 1.1 
 
Create a small phonebook using a dictionary. Use the names as keys and
numbers as values. Use 'Chandler, Monica, Ross' and corresponding numbers:
'55523645, 55564452, 55545872'. Add the phonenumbers as integers. Answer
with the resulting dictionary. 

Write your code below and put the answer into the variable ANSWER.
"""

phonebook = {"Chandler": 55523645, "Monica": 55564452, "Ross": 55545872}

ANSWER = phonebook

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
How many items are there in the dictionary?  

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = len(phonebook)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Use the 'get()' method on your phonebook and answer with the phonenumber of
'Ross'.  

Write your code below and put the answer into the variable ANSWER.
"""

ANSWER = phonebook.get("Ross")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Get all keys from the dictionary and return them in a sorted list.  

Write your code below and put the answer into the variable ANSWER.
"""
sorted_phonebook = sorted(phonebook)
ANSWER = sorted_phonebook

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Get all values from the dictionary and return them in a sorted list.  

Write your code below and put the answer into the variable ANSWER.
"""

sorted_phonebookvalues = sorted(phonebook.values())
ANSWER = sorted_phonebookvalues

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Use the in-operator to test if the name 'Ross' exists in the dictionary.
Answer with the return boolean value. 

Write your code below and put the answer into the variable ANSWER.
"""
if "Ross" in phonebook:
    boo = True
else:
    boo = False

ANSWER = boo

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Use the in-operator to test if the phone number 55545872 exists in the
dictionary. Answer with the return boolean value. 

Write your code below and put the answer into the variable ANSWER.
"""
if 55545872 in phonebook.values():
    boo2 = True
else:
    boo2 = False



ANSWER = boo2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Use a for-loop to walk through the dictionary and and create a string
representing it. Each name and number should be on its own row, separated
by a space. The names must come in alphabetical order. Answer with the
resulting string. 

Write your code below and put the answer into the variable ANSWER.
"""
i = 0
s = ""
for contact in phonebook:
    s = s + sorted_phonebook[i]+" "+ str(phonebook[sorted_phonebook[i]])+'\n'
    i += 1

ANSWER = s

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Convert the phonenumber to a string and add the prefix '+1-', representing
the language code, to each phone-number. Answer with the resulting
dictionary. 

Write your code below and put the answer into the variable ANSWER.
"""
i = 0
s2 = ""
for contact in phonebook:
    s2 = "+1-" + str(phonebook[contact])
    phonebook[contact] = s2

ANSWER = phonebook

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Get and remove the item 'Ross' from the phonebook (use pop()). Answer with
the resulting dictionary. 

Write your code below and put the answer into the variable ANSWER.
"""
phonebook = {"Chandler": 55523645, "Monica": 55564452, "Ross": 55545872}
phonebook.pop("Ross")
ANSWER = phonebook

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11 
 
Add the item you just popped from the phonebook. Answer with the resulting
dictionary. 

Write your code below and put the answer into the variable ANSWER.
"""

phonebook["Ross"] = 55545872
ANSWER = phonebook

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Tuples 
 
Some basics with tuples 
"""

"""
Exercise 2.1 
 
Create a tuple with 'bear, 65, 6.47, chair, 5'. Answer with the length of
the tuple as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""

tp = ('bear', 65, 6.47, 'chair', 5)

ANSWER = len(tp)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Create a tuple out of: (bear, 65, 6.47, chair, 5). Assign each value in the
tuple to different variables: 'a','b','c','d','e'. Answer with the
variable: 'd'. Hint: a,b,c = tuple. 

Write your code below and put the answer into the variable ANSWER.
"""
a, b, c, d, e = tp
ANSWER = d

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Use the list [45, 22, 2, 498, 78]. Assign the first two elements to a tuple
with a slice on the list. Answer with the first element in the tuple as an
integer. 

Write your code below and put the answer into the variable ANSWER.
"""
l = [45, 22, 2, 498, 78]
tp2 = tuple(l[0:2])

ANSWER = tp2[0]

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Create a tuple with (moose, 12, 1.98, table, 7). Convert it to a list and
replace the second element with: 'elevator'. Convert it back to a tuple and
answer with the first three elements in a comma-separated string. 

Write your code below and put the answer into the variable ANSWER.
"""
tp3 = ("moose", 12, 1.98, "table", 7)
l2 = list(tp3)

l2[1] = "elevator"
tp3 = tuple(l2)
s = ""
c = 0
while c < 2:
    s = s + str(tp3[c]) + ","
    c += 1
s = s + str(tp3[2])
   

ANSWER = s

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))


dbwebb.exitWithSummary()
