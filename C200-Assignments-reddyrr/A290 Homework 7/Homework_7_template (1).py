# A90 HOMEWORK 7
# Your name here: ___Ronan Reddy______


# 1) Tail recursion
# Power: Given a base number n, a exponent number p, return n to p power
# eg. n = 2, p = 3, 2^3 = 2*2*2 = 8
# NOTE: you must implement this using tail recursion. Remember, If the last line in a recursive function definition is 
# just to return the result of a recursive function call, then you are using tail recursion.

def powerTail(n,p,res = 1): # You need to figure out the parameter of this function
    if p == 0:
        return res
    else:
        return powerTail(n,p-1,res*n)


# 2) Generator - fibonacci sequence
# Make a generator using an infinite loop. The generator will return a different fibonacci number every time it's called
# eg. x1 = generateFibonacciSolution(), print(next(x1)) => 1, print(next(x1)) => 2, print(next(x1)) => 3, print(next(x1)) => 5, 

def generateFibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b


# 3) With open and CSV
# Use "with open" and csv.reader() to read in the provided CSV file named employmentIndicator.csv (on Canvas)
# This will require you to understand your machine's file paths.
# You'll either need to move the CSV file to the folder your .py file is working from,
# or you'll need to call the full file path from where it downloads to.

import csv

#start here
path = "A290 Homework 7/employmentIndicator (1).csv"
with open(path,'r') as fileToWrite:
    file = csv.reader(fileToWrite)
    for i in file:
        print(i)

# For a bonus point, uncomment the below chunk and replace VARIABLE_NAME with what you named the reader file above.
# This will print the first ten rows of the file if done correctly.

    for i,row in enumerate(file):
        print(row)
        if i >= 9:
            break