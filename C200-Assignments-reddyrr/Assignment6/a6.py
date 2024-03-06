import math
import random as rn
import numpy as np
# import matplotlib.pyplot as plt
import os 
import csv


print(os.getcwd())

# PROBLEM ONE

data = []
# #INPUT path and filename
# #OUTPUT list of parent, child pairs
# #CONSTRAINT use csv reader
def get_data(path, filename):
    dict = {}
    with open(path + filename,"r") as fileToWrite:
        return list(csv.reader(fileToWrite))
data = get_data("Assignment6/", "family.txt")
        

#input parent name
#output children
#constraint using comprehension
def get_child(name):
    return [child for parent, child in data if parent == name]


#input parent name
#output true if has children
#constraint using comprehension
def has_children(name):
    return bool(get_child(name))

#input child name
#output parent of child
#constraint using comprehension
def get_parent(name):
    return [parent for parent, child in data if child == name]


#input child name1, child name2
#output true if children have same parent
#constraint using comprehension
def siblings(name1,name2):
    p1 = get_parent(name1)
    p2 = get_parent(name2)
    return p1==p2
 
#input grandparent name1, grandchild name2
#output true if name1 is grandparent to name2
#constraint using comprehension 
def grandparent(name1, name2):
    return bool([i for i,j in data for a,b in data if j==a and i==name1 and b==name2])

#input nothing
#output all names
#constraint list comprehension only
def get_all():
    return [k for k in [i for i, j in data] + [j for i, j in data]]

#input name1, name2
#output true if name1 and name 2 are cousins, i.e., have the same grandparents
def cousins(name1,name2):
    return [grandparent(i,name1) for i in get_all()]==[grandparent(i,name2) for i in get_all()]

# Problem 2
# input n: total space (size), v: tiles and 
# output all possible patterns where the tiles add exactly to the the space (n)
def tiles(n, v, lst):
    result = []
    for i in lst:
        summ += lst[i]
    if summ == 1:
        return result
    for j in lst:
        for i in v:
            result.append(j+[i])
    for j in lst:
        for i in v:
            temp = tiles(n,[j+[i]], lst-1)
            result.exend(temp)
    return result





#problem 3
# input: a list of numbers
# output: a pair containing the sum and boolean vector (see PDF for sample output)
def max_adjacent(lst):
    def max_helper(substring):
        for i in range(len(substring)-1):
            if substring[i+1] - substring[i] == 1:
                return False
        return True
    def make_substring(lst):
        substrings=[[]]
        for i in lst:
            substrings += [substring +[i] for substring in substrings]
        return substrings
    substrings = make_substring(range(len(lst)))
    corsub = [substring for substring in substrings if max_helper(substring)]
    max = 0
    maxsub = []
    for substring in corsub:
        sumsub = sum(lst[i] for i in substring)
        if sumsub > max:
            max = sumsub
            maxsub = substring
    new = []
    for i,j in enumerate(lst):
        if i in maxsub:
            new.append(1)
        else:
            new.append(0)
    return [max,new]


########################
# PROBLEM 4
########################


# INPUT path and filename (payrollwins.txt)
# OUTPUT payroll and number of wins as a list
# Ouptut example: [[209,89], [139,74]]
# CONSTRAINT use csv reader
def get_data_1(path, filename):
    with open(path + filename,"r") as fileToWrite:
        lst = []
        for i, j in csv.reader(fileToWrite):
            lst.append(([int(i),int(j)]))
        return lst

        


#INPUT data points (x0,y0),...,(xn,yn)
#OUTPUT best regression slope m_hat, intercept b_hat, and R_sq
def std_linear_regression(data):
    def func2(data,f):
        return sum([f(i,j) for i,j in data])
    n = len(data)
    x_yp = func2(data, lambda i,y:i*y)
    x_s = func2(data, lambda i,j:i)
    y_s = func2(data, lambda i,j:j)
    x_sq = func2(data, lambda i,j:i**2)
    y_sq = func2(data, lambda i,j:j**2)
    x_ys = x_yp - ((x_s*y_s)/n)
    x_xs = x_sq - (((x_s)**2)/n)
    m_hat = round(x_ys/x_xs,3)
    b_hat = round(((y_s-m_hat*x_s)/n),3)
    TSS = y_sq - (y_s**2/n)
    ESS = y_sq - b_hat*y_s-m_hat*x_yp
    r_sq = round((TSS-ESS)/(TSS),3)
    return m_hat,b_hat,r_sq



#### Problem 5

# INPUT path and filename (fish_data.txt)
# OUTPUT two separate lists, first one containing the age and second containing 
# the length as given in the fish_data.txt file 
# Ouptut example: [1,2,3, ...], [4.8, 8.8, 8.0, ...]
# CONSTRAINT use csv reader
# make sure to get rid of the first line that just contains the column names (we don't want that)
def get_fish_data(path, name):
    x= []
    y = []
    with open(path + name) as fileToWrite:
        data = fileToWrite.readlines()[1:]
        data = [line.strip().split(',') for line in data]
        x = [int(row[0]) for row in data]
        y = [float(row[1]) for row in data]
        return x,y
        


#INPUT lists X values, Y values of data and degree of the polynomial
#RETURN a polynomial of degree three
def make_function(X,Y,degree):
    x = np.poly1d(np.polyfit(X,Y,degree))
    return x





#### Problem 6
#input string and positive integer n
#output a list of the longest string that have no more than n distinct symbols

def max_n(str, n):
    def longlst(lst):
        def l_h(lst,tmp=[""]):
            if lst:
                x = lst[0]
                lst = lst[1:]
                y = tmp[0]
                if len(x)>len(y):
                    return l_h(lst,[x])
                elif len(x)==len(y):
                    return l_h(lst,tmp+[x])
                else:
                    return l_h(lst,tmp)
            else:
                return tmp
        return l_h(lst)
    
    def cnt_dif(lst, s=[], cnt=0):
        if lst:
            x = lst[0]
            lst = lst[1:]
            if not x in s:
                cnt = cnt+1
                s=s+[x]
            return cnt_dif(lst,s,cnt)
        else:
            return cnt
    cnt=[]
    m={}
    def sub(str,cnt,n):
        for i in range(len(str)):
            for j in range(i+1,len(str)+1):
                k=str[i:j]
                cnt +=[k] if not k in cnt and cnt_dif(k) == n else []
        return cnt
    return longlst(sub(str,cnt,n)) 


#problem 7

#input a tuple of model parameters, second parameter is the number of trials
#output the percent success rounded to two decimal places
def simulation(model_parameters, num_trials):
    test = np.random.binomial(num_trials, .6, 1000000)
    calc1 = 1-model_parameters[1]
    calc2 = (calc1/model_parameters[1])**model_parameters[0]
    calc3 = (1-model_parameters[1])/model_parameters[1]
    calc4 = calc3**model_parameters[2]
    calc = (1-calc2)/(1-calc4)
    return round(calc,2)



if __name__ == '__main__':
    
    # uncomment to test
    # Before sbmitting to the Autograder: 
    # Make sure to comment the code for plotting graph in P4 and also the import of matplotlib on the top of this file
    # You can use that code to make the graph on your system and test but comment it before the submission

    # problem 1
    # data = get_data("", "family.txt")
    # print(data)
    # print(has_children('0')) #true
    # print(has_children('7')) #false
    # print(get_child('6'))
    # print(get_parent('g'))
    # print(siblings('7','A')) #true
    # print(siblings('2','7')) #false
    # print(grandparent('0','3')) #true
    # print(grandparent('0','7')) #false
    # print(get_all())
    # print(cousins('3','6')) #true
    # print(cousins('3','5')) #false


    #problem 2
    n = 6
    v = [1,2,3]
    print(tiles(n,v,[[i] for i in v]))
    for i in tiles(n,v,[[i] for i in v]):
        print(sum(i), end="")
    n = 4
    v = [1,2]
    print(tiles(n,v,[[i] for i in v]))
    for i in tiles(n,v,[[i] for i in v]):
        print(sum(i), end="")    

    #problem 3
    # data = [[5,1,4,1,5],[5,6,2,4],[4,5,1,1],[1,5,10,4,1],[1,1,1,1,1]]
    # for d in data:
    #     print(max_adjacent(d))

    #problem 4

    # data6 = get_data_1("provide path", "payrollwins.txt")
    # m_hat, b_hat, R_sq  = std_linear_regression(data6)
    # print(m_hat,b_hat,R_sq)
    
    # Comment the code for plotting (and the import of matplotlib up top) before you submit to the Autograder.
    # You can test as much as you want on your system but before the submission - please comment the code for
    # plotting.
    # plt.plot([x for x,_ in data6],[y for _,y in data6],'ro')
    # plt.plot([x for x,_ in data6],[m_hat*x + b_hat for x,_ in data6],'b')
    # plt.xlabel("$M Payroll")
    # plt.ylabel("Season Wins")
    # plt.title(f"Least Squares: m = {m_hat}, b = {b_hat}, R^2 = {R_sq} ")
    # plt.ylabel("Y")
    # plt.show()

    # #problem 5
    # name = "fish_data.txt"
    # X,Y = get_fish_data("provide path", name)
    # data5 = [[i,j] for i,j in zip(X,Y)]
    # print(data5)
      
    # plt.plot(X,Y,'ro')
    # xp = np.linspace(1,14,10)
    # degree = 3
    # p3 = make_function(X,Y,degree)
    # plt.plot(xp,p3(xp),'b')
    # plt.xlabel("Age (years)")
    # plt.ylabel("Length (inches)")
    # plt.title("Rock Bass Otolith")
    # plt.show()

    #problem 6
    # data = ["aaaba", "abcba", "abbcde","aaabbbaaaaaac","abcdeffg"]
    # for d in data:
    #     for i in range(1,7):
    #         print(f"{d} with {i} max is\n {max_n(d,i)}")
    
    
    #problem 7
    # model_parameters = (2,.6,4) #starting amount, probablity of win, goal
    # print(simulation(model_parameters,100000))
    
    print()