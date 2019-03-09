#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
7cf244cfbcc55a41070a891838e397b4
python
lab1
maaa16
2016-01-24 09:21:27
v2.0.1x (2015-09-29)

Generated 2016-01-24 10:21:28 by dbwebb lab-utility v2.0.1x (2015-09-29).
https://github.com/mosbth/lab
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 1 - python 
 
If you need to peek at examples or just want to know more, take a look at
the page: https://docs.python.org/3/library/index.html. Here you will find
everything this lab will go through and much more. 
"""

"""
--------------------------------------------------------------------------
Section 1. Integers, strings, floats and basic arithmetics 
 
The foundation of numbers and basic arithmetic. 
"""

"""
Exercise 1.1 
 
Create a variable called 'numOne' and give it the value 76. Create another
variable called 'numTwo' and give it the value 76. Create a third variable
called 'result' and assign to it the sum of the first two variables. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
numOne = 76
numTwo = 76

result = numOne + numTwo



ANSWER = result

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Create a variable called 'numThree' and give it the value 81. Create
another variable called 'numFour' and give it the value 61. Subtract
'numThree' from 'numFour' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

numThree = 81
numFour = 61

result2 = numFour - numThree



ANSWER = result2

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Find out the product of 'numOne' and 'numThree' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

result3 = numOne * numThree

ANSWER = result3

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Divide 30 with 5 and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

result4 = 30/5

ANSWER = result4

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Create a variable called 'floatOne' and give it the value 98.76. Create
another variable called 'floatTwo' and give it the value 21.93. Sum the two
values and answer with the result, rounded to 2 decimals. 

Write your code below and put the answer into the variable ANSWER.
"""

floatOne = 98.76
floatTwo = 21.93

result5 = floatOne + floatTwo

ANSWER = result5

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Subtract 'floatTwo' from 'floatOne' and answer with the result. Round to 2
decimals. 

Write your code below and put the answer into the variable ANSWER.
"""

result6 = floatOne - floatTwo

result7 = round(result6, 2)

ANSWER = result7

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Answer with the product of 'floatOne' and 'floatTwo', rounded to 4
decimals. 

Write your code below and put the answer into the variable ANSWER.
"""

result8 = floatOne * floatTwo

result9 = round(result8, 4)

ANSWER = result9

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create three variables: 'n1' = 327, 'n2' = 209 and 'n3' = 80. Sum up 'n1'
and 'n2'. Subtract 'n3' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

n1 = 327
n2 = 209
n3 = 80

result10 = n1 + n2 - n3


ANSWER = result10

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Answer with the result of 507 modulo (%) 35. 

Write your code below and put the answer into the variable ANSWER.
"""

result11 = 507 % 35


ANSWER = result11

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Add the word: 'device' to the word: 'beach' and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

result12 = "beach" + "device"



ANSWER = result12

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Conditions, exceptions, booleans, if, else and elif 
 
 
"""

"""
Exercise 2.1 
 
Answer with the boolean value of: 70 is less than 259. 

Write your code below and put the answer into the variable ANSWER.
"""

result13 = 70 < 259

ANSWER = result13

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Answer with the boolean value of: 444 is larger than 490. 

Write your code below and put the answer into the variable ANSWER.
"""

result14 = 444 > 490



ANSWER = result14

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Answer with the boolean value of: 70 == 444. 

Write your code below and put the answer into the variable ANSWER.
"""

result15 = 70 == 444



ANSWER = result15

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, False))

"""
Exercise 2.4 
 
Create three variables representing dice values: 'd1' = 1, 'd2' = 6 and
'd3' = 6. Sum them up and answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

d1 = 1
d2 = 6
d3 = 6

result16 = d1 + d2 + d3



ANSWER = result16

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Create an if statement to see if the total value of your dices is 11 or
higher. If that is the case, answer with the string: 'big', else answer
with the string: 'nothing'.  

Write your code below and put the answer into the variable ANSWER.
"""

if result16 >= 11:
    result17 = "big"
else:
    result17 = "nothing"


ANSWER = result17

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Create an elif statement that checks your total dice value. The checks and
results should be: three of the same value = 'triple', total of 11 or
higher = 'big', total of 10 or lower = 'small'. If you get a triple you
should not make more checks. 

Write your code below and put the answer into the variable ANSWER.
"""

if d1 == d2 == d3:
    result18 = "triple"
elif d1 + d2 + d3 >= 11:
    result18 = "big"
else:
    result18 = "small"

ANSWER = result18

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 3. Built-in functions 
 
Some useful built-in functions 
"""

"""
Exercise 3.1 
 
Use max() to find the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""

serie = (6, 8, 95, 2, 12, 152, 4, 78, 621, 45)

result19 = max(serie)







ANSWER = result19

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.1", ANSWER, False))

"""
Exercise 3.2 
 
Use min() to find the smallest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

serie = (6, 8, 95, 2, 12, 152, 4, 78, 621, 45)

result20 = min(serie)



ANSWER = result20

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.2", ANSWER, False))

"""
Exercise 3.3 
 
Use len() to find the number of letters in the word: error. Answer with the
result. 

Write your code below and put the answer into the variable ANSWER.
"""

result21 = len("error")



ANSWER = result21

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.3", ANSWER, False))

"""
Exercise 3.4 
 
Convert the number 353 to a string and add it to the word 'error'. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

result22 = "error" + str(353)



ANSWER = result22

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.4", ANSWER, False))

"""
Exercise 3.5 
 
Convert the number 640.49 to an integer and then to a string. Add it to the
beginning of the word: 'error'. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""

result23 = str(int(640.49)) + "error"



ANSWER = result23

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("3.5", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 4. Functions 
 
Basic functions 
"""

"""
Exercise 4.1 
 
Create a function called 'prodNr' that takes two arguments, 34 and 77. The
function should return the product of the numbers. Answer with a call to
the function.  

Write your code below and put the answer into the variable ANSWER.
"""

def prodNr(x, y):
    '''beräknar produkten av x och y'''
    return x*y

result24 = prodNr(34, 77)

ANSWER = result24

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.1", ANSWER, False))

"""
Exercise 4.2 
 
Create a function called 'funnyWord' that takes one argument and adds it to
the string ' is a funny word'. If the argument is 'water', the function
should return: 'water is a funny word'. Use the argument 'restaurant' and
answer with a call to the function. 

Write your code below and put the answer into the variable ANSWER.
"""

def funnyWord(word):
    '''returnerar input + is a funnay word'''
    return str(word) + " is a funny word"




ANSWER = funnyWord("restaurant")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.2", ANSWER, False))

"""
Exercise 4.3 
 
Create a function called 'inRange' that takes one argument. The function
should return 'true' if the argument is higher than 50 and lower than 100.
If the number is out of range, the function should return 'false'. The
return type should be boolean. Use the argument 31 and answer with a call
to the function. 

Write your code below and put the answer into the variable ANSWER.
"""

def inRange(x):
    '''kontrollerar ifall input ligger mellan 50-100'''
    if 50 < x < 100:
        result25 = True
    else:
        result25 = False
	
    return result25
	

ANSWER = inRange(31)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("4.3", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 5. Iteration and loops 
 
For-loops and while-loops.  
"""

"""
Exercise 5.1 
 
Create a while-loop that adds 8 to the number 64, 73 times. Answer with the
result.  

Write your code below and put the answer into the variable ANSWER.
"""
i = 0
result26 = 64
while i < 73:
    result26 += 8
    i += 1



ANSWER = result26

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.1", ANSWER, False))

"""
Exercise 5.2 
 
Create a while-loop that subtracts 5 from 28, 68 times. Answer with the
result.  

Write your code below and put the answer into the variable ANSWER.
"""

i = 0
result27 = 28
while i < 68:
    result27 -= 5
    i += 1


ANSWER = result27

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.2", ANSWER, False))

"""
Exercise 5.3 
 
Create a for-loop that counts the number of elements in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""

serie = (6, 8, 95, 2, 12, 152, 4, 78, 621, 45)
result28 = 0
for number in serie:
    result28 += 1


ANSWER = result28

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.3", ANSWER, False))

"""
Exercise 5.4 
 
Create a for-loop that sums up the numbers in the serie:
67,2,12,28,128,15,90,4,579,450. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""
serie = (67, 2, 12, 28, 128, 15, 90, 4, 579, 450)
result29 = 0
for number in serie:
    result29 += number

ANSWER = result29

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.4", ANSWER, False))

"""
Exercise 5.5 
 
Create a for-loop that finds the largest number in the serie:
6,8,95,2,12,152,4,78,621,45. Answer with the result.  

Write your code below and put the answer into the variable ANSWER.
"""

serie = (6, 8, 95, 2, 12, 152, 4, 78, 621, 45)
largestNumber = serie[0]
for number in serie:
    if number > largestNumber:
        largestNumber = number
		
ANSWER = largestNumber

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.5", ANSWER, False))

"""
Exercise 5.6 
 
Create a for-loop that goes through the numbers:
67,2,12,28,128,15,90,4,579,450. If the current number is even, you should
add it to a variable and if the current number is odd, you should subtract
it from the variable. Answer with the final result.  

Write your code below and put the answer into the variable ANSWER.
"""

serie = (67, 2, 12, 28, 128, 15, 90, 4, 579, 450)
result30 = 0
for number in serie:
    if number%2 == 0:
        result30 += number
    else:
        result30 -= number



ANSWER = result30

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("5.6", ANSWER, False))


dbwebb.exitWithSummary()
