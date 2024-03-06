#Homework 5
#Your name here: __Ronan Reddy_____

# Question 1 -> dictionary iteration
# Given a string, return which letter appears most often.
# You can assume all letters are lowercase, and there are only letters in the string.

random = "qoxkrgunxvdejmjhjvjwifugpfliohiduqmqwbdxdujcosmeyoberifnqsrrwljzimajaasyijayaiql"

def count(str):
    letcnt = {}
    for l in str:
        if l in letcnt:
            letcnt[l]+=1
        else:
            letcnt[l]=1
    com = max(letcnt, key=letcnt.get)
    return com
print(count(random))    



# Question 2 -> dictionary update
# The record of school name -> school description is wrong. Fix them using a method, and return the fixed dctionary.
# DON'T just edit the declaration code.

dict = {"Luddy": "Business", "Kelly": "Music", "Jacob": "Informatics, Computing and Engineering",
        "O'Neill":  "Public and Environmentl Affairs"}

def fix(dict):
    cord = {}
    for key,value in dict.items():
        cork = key.replace(";",":")
        corv = value
        cord[cork] = corv
    return cord
print(fix(dict))



# Question 3 -> string strip & replace
# Given a list of messy strings, writing a method to format them. Return the cleaned list.
# Get rid of the leading and trailing spaces, and replace all the number 2 with word "two."
# Output shoud be:
#['two apples', 'two exams in two days', 'two friends are chatting']

messy = ["    2 apples ",
         "  2 exams in two days    ",
         "      2 friends are chatting    "]

def format(lst):
    c = []
    for i in lst:
        ck = i.strip().replace("2", "two")
        c.append(ck)
    return c
print(format(messy))




