#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
40b7976eceaf639f5bb85107db8fc5e0
python
lab3
maaa16
2016-02-05 13:18:20
v2.0.1x (2015-09-29)

Generated 2016-02-10 08:44:07 by dbwebb lab-utility v2.0.1x (2015-09-29).
https://github.com/mosbth/lab
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 3 - python 
 
 
"""

"""
--------------------------------------------------------------------------
Section 1. List basics 
 
 
"""

"""
Exercise 1.1 
 
Concatenate the two lists [drums, bumblebee] and [piano, wall]. Answer with
your list.  

Write your code below and put the answer into the variable ANSWER.
"""

list1 = ["drums", "bumblebee"]
list2 = ["piano", "wall"]
list3 = list1 + list2

ANSWER = list3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Use the list [wasp, fly, butterfly, bumblebee, mosquito]. Add the words:
'icecream' and 'donkey' as the second and third element. Answer with the
modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list4 = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]
list4.insert(1, "icecream")
list4.insert(2, "donkey")

ANSWER = list4

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Use the list [wasp, fly, butterfly, bumblebee, mosquito]. Replace the third
word with: 'tablet'. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list5 = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]
list5.pop(2)
list5.insert(2, "tablet")


ANSWER = list5

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Sort the list [Dafoe, Sheen, Berenger, Depp, Whitaker] in ascending
alphabetical order. Answer with the sorted list. 

Write your code below and put the answer into the variable ANSWER.
"""
list6 = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]
list6.sort()

ANSWER = list6

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Use the list from the last excercise ([Dafoe, Sheen, Berenger, Depp,
Whitaker]) and sort it in decending alphabetical order. Answer with the
sorted list. 

Write your code below and put the answer into the variable ANSWER.
"""
list7 = ["Dafoe", "Sheen", "Berenger", "Depp", "Whitaker"]
list7.sort(reverse=True)

ANSWER = list7

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Use pop() to get the second and the last element in the list: [wasp, fly,
butterfly, bumblebee, mosquito]. Answer with the popped elements in a new
list. 

Write your code below and put the answer into the variable ANSWER.
"""
list8 = ["wasp", "fly", "butterfly", "bumblebee", "mosquito"]
sec_item = list8.pop(1)
last_item = list8.pop(-1)
list9 = [sec_item, last_item]
ANSWER = list9

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Use remove() to delete the word: 'bobcat' from the list: [lion, tiger,
ozelot, bobcat, cougar]. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list10 = ["lion", "tiger", "ozelot", "bobcat", "cougar"]
list10.remove("bobcat")

ANSWER = list10

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Built-in list functions 
 
Some basic built-in functions 
"""

"""
Exercise 2.1 
 
Use a built-in function to sum all numbers in the list: [123, 4, 125, 69,
155]. Answer with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
list11 = [123, 4, 125, 69, 155]
sum_list11 = sum(list11)
ANSWER = sum_list11

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Use built-in functions, such as 'sum' and 'len' to get the average value of
the list: [123, 4, 125, 69, 155]. Answer with the result as a float with at
most one decimal. 

Write your code below and put the answer into the variable ANSWER.
"""
list12 = [123, 4, 125, 69, 155]
avg_list12 = sum(list12)/len(list12)
ANSWER = avg_list12

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Use a built-in function to get the lowest number in the list: [67, 50, 2,
39, 15]. Answer with the result as a integer. 

Write your code below and put the answer into the variable ANSWER.
"""
list13 = [67, 50, 2, 39, 15]
list13.sort()
low_list13 = list13.pop(0)

ANSWER = low_list13

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Use the built-in functions split() and join() to fix this string:
'The?grass?is?growing' into a real sentence, (without '?'). Answer with the
fixed string. 

Write your code below and put the answer into the variable ANSWER.
"""
string1 = "The?grass?is?growing"
string2 = " ".join(string1.split("?"))
ANSWER = string2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Use the string: 'For every minute you are angry you lose sixty seconds of
happiness.' and split it with the delimiter ' ' (space). Answer with the
element at index 2. 

Write your code below and put the answer into the variable ANSWER.
"""
string3 = "For every minute you are angry you lose sixty seconds of happiness."
string4 = string3.split(" ")
index2_string4 = string4.pop(2)
ANSWER = index2_string4

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Use slice on the list [a, b, c, d, e] and replace the second and third
element with 'green, purple'. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list14 = ["a", "b", "c", "d", "e"]
list14[1:3] = ["green", "purple"]
ANSWER = list14

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
Exercise 2.7 
 
Use slice on the list [a, b, c, d, e] and replace the last two elements
with 'green, purple'. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list15 = ["a", "b", "c", "d", "e"]
list15[-2:] = ["green", "purple"]

ANSWER = list15

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.7", ANSWER, False))

"""
Exercise 2.8 
 
Use slice on the list [a, b, c, d, e] and insert the words 'green, purple'
after the third element. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list16 = ["a", "b", "c", "d", "e"]
list16[3:3] = ["green", "purple"]

ANSWER = list16

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.8", ANSWER, False))

"""
Exercise 2.9 
 
Use 'del' on the list [dvd, mp3, blu-ray, vhs, cd] and delete the first
element. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list17 = ["dvd", "mp3", "blu-ray", "vhs", "cd"]
del list17[0]
ANSWER = list17

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.9", ANSWER, False))

"""
Exercise 2.10 
 
Use 'del' on the list [dvd, mp3, blu-ray, vhs, cd] and delete the second
and third element. Answer with the modified list. 

Write your code below and put the answer into the variable ANSWER.
"""
list18 = ["dvd", "mp3", "blu-ray", "vhs", "cd"]
del list18[1:3]
ANSWER = list18

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.10", ANSWER, False))

"""
Exercise 2.11 
 
Assign the list [d, c, b, a, e] to a variable called 'list1'. Assign the
list again, but to another variable called 'list2'. Answer with the result
of 'list1 is list2'.  

Write your code below and put the answer into the variable ANSWER.
"""
list1 = ["d", "c", "b", "a", "e"]
list2 = ["d", "c", "b", "a", "e"]

ANSWER = list1 is list2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.11", ANSWER, False))

"""
Exercise 2.12 
 
Use your lists from the last exercise. Assign 'list1' to another variable
called 'list3' like this: list3 = list1. Answer with the result of 'list1
is list3'. 

Write your code below and put the answer into the variable ANSWER.
"""
list3 = list1

ANSWER = list1 is list3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.12", ANSWER, False))

"""
Exercise 2.13 
 
Use your lists from the last exercise. Change the first element in 'list1'
to 'x'. Answer with 'list3'. 

Write your code below and put the answer into the variable ANSWER.
"""
list1[0:1] = "x"

ANSWER = list3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Lists as arguments 
 
Some excercises with passing lists as arguments to a function. 
"""

"""
Exercise 3.1 
 
Create a function that returns the list passed as argument sorted in
numerical and ascending order. Also multiply all values with 10. Use the
list: [67, 50, 2, 39, 15], and the built-in method 'sort()'. Answer with
the sorted list. 

Write your code below and put the answer into the variable ANSWER.
"""
def sortmultiplyer(l):
    '''
    Sorterar och multiplicerar lista med 10
    '''
    l.sort()
    newlist = []
    for element in l:
        newlist = newlist + [element*10]
    return newlist

list19 = [67, 50, 2, 39, 15]
ANSWER = sortmultiplyer(list19)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2 
 
Create a function that takes the list: [123, 4, 125, 69, 155] as argument.
The function should multiply all even numbers by 3 and add 8 to all odd
numbers. Answer with the modified list sorted in numerical order,
descending. 

Write your code below and put the answer into the variable ANSWER.
"""
def sortmultioddeven(l):
    '''
    Sorterar i descending order och multiplicerar beroende på jämnt eller udda tal
    '''
    newlist = []
    for element in l:
        if element%2 == 0:
            newlist = newlist + [element*3]
        else:
            newlist = newlist + [element+8]
    newlist.sort(reverse=True)
    return newlist
list20 = [123, 4, 125, 69, 155]
ANSWER = sortmultioddeven(list20)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))


dbwebb.exitWithSummary()
