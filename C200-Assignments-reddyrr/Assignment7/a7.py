import numpy as np
import random as rn
import csv
import math
# import matplotlib
# import matplotlib.pyplot as plt
import os 
import csv
from sklearn.linear_model import LinearRegression


# Problem 1
# Input: data in the file payrollwins.txt
# Output: slope, intercept, R^2 and the model

# Please remeber the basics of File I/O form the labs and lectures.
# For testing you code in VSC, you have to use path that works on your system.
# Although, it's not a good practise but even using a hard-coded path would work, but
# before submitting to the Autograder, you should keep path as "", because Autograder has 
# it's own OS and it's own FileSystem, and the path which works on your system may not be valid on the Autograder. 
# Please remember to comment out all code for plotting (and the import of matplotlib) before submitting to the Autograder.


# Input: path and filename
# Output: the data in the format as expected by the LinearRegression function of sklearn
# CONSTRAINT use csv reader
# file containig payroll data
def get_data(path, filename):
    with open(path+filename, 'r') as fileToWrite:
        lst = []
        for i,j in list(csv.reader(fileToWrite)):
            lst.append([int(i), int(j)])
        return lst


#input data for univariate regression
# Output: slope, intercept, R^2 and the model object returned by sklearn
def my_scikit_LR(data6):
    x = np.array([[x_vals] for x_vals,y_vals in data6])
    y = np.array([[y_vals] for x_vals,y_vals in data6])
    reg = LinearRegression().fit(x,y)
    R_2 = reg.score(x,y)
    slope = reg.coef_[0]
    intercept = reg.intercept_
    model = reg.predict
    return (slope,intercept,R_2,model)



# Problem 2
# The recursive version of the functions is give by us
# You need to complete the tail_recursive, while and generator version

#recursive functions

def p(n):
    if n:
        return p(n-1) + 0.02*p(n-1)
    else:
        return 10000

#MUST be implemented with tail recursion
def p_t(n, acc=10000):
    if n==0:
        return acc
    else:
        return p_t(n-1,1.02*acc)

#MUST be implemented with a WHILE LOOP
def p_w(n, acc=10000):
    if n == 0:
        return acc
    while n>0:
        acc = acc + .02 *acc
        n-=1
    return acc

#MUST be implemented with generator
def p_g():
   acc = 10000
   n=0
   while True:
       yield acc
       n+=1
       acc = 1.02*acc


def c(n):
    if n > 1:
        return 9*c(n-1) + 10**(n-1) - c(n-1)
    else:
        return 9

#MUST be implemented with tail recursion
def c_t(n, acc1=9, acc2=0):
    if n>1:
        return c_t(n-1,(8*acc1) + (10**((acc2+1))), acc2+1)
    else:
        return acc1
        
#MUST be implemented with a WHILE LOOP
def c_w(n, acc1=9, acc2=0):
    while n>1:
        n,acc1,acc2 = n-1,8*acc1+10**(acc2+1),acc2+1
    return acc1

#MUST be implemented with generator
def c_g():
    acc1 = 9
    acc2 = 0
    n = 1
    while True:
        yield acc1
        n+=1
        value = 9*acc1+10**(n-1) - acc1
        vaue2 = acc1
        acc1 = value



def d(n):
    if n:
        return 3*d(n-1) + 1
    else:
        return 1

#MUST be implemented with tail recursion
def d_t(n, acc=1):
    if n == 0:
        return acc
    else:
        value = 3*acc+1
        return d_t(n-1,value)

#MUST be implemented with a WHILE LOOP 
def d_w(n, acc=1):
    if n==0:
        return acc
    while n>0:
        acc=3*acc+1
        n-=1
    return acc

#MUST be implemented with generator
def d_g():
    acc = 1
    n=0
    while True:
        yield acc
        acc = 3*acc+1



# Problem 3
def c_2(n, m):
    if m == 0 or n == m:
        return 1
    else:
        return c_2(n-1, m) + c_2(n-1, m-1)

def B(n):
    s=0
    if n == 0:
        return 1
    else:
        cons = -1/(n+1)
        for k in range(n):
            s+=c_2(n+1,k)*B(k)
        return s*cons



# problem 4
# input function and epsilon
# output lambda expression (derivative)
def derivative(f, epsilon):
    return lambda x: (float(f(x+epsilon) - f(x-epsilon)))/float(2*epsilon)
    
def f(x):
    return x**2 - 3*x



# Problem 5
# INPUT path and file name
# OUTPUT two lists of incomes and happiness 
# from income_data.csv
# use scikit-learn_LR 
def get_data_2(path, name):
    with open(path+name, 'r') as fileToWrite:
        lst=[]
        file=csv.reader(fileToWrite)
        h=next(file)
        for i,j in file:
            lst.append((float(i),float(j))) 
    return lst





# problem 6 

# INPUTS ith candle, starting value of x, default width, and the four critical values: open, close, max_p, min_p.
# RETURN three tuples: The first being the data of the rectangle I.E. point, width, height, and color. 
# Next tuple should be the topline. And lastly the last tuple should be the bottom line.  
# (point, width, height, color), topline, bottomline
# point: coordinates of the lower left point of the rectangle, width of rectangle, height of rectangle and color of rectangle 
# topline ((xt0, yt0),(xt1, yt1)) coordinates of the line from max to top middle of box
# bottomline ((xb0, yb0),(xb1, yb1)) coordinates of the line from min to bottom middle of box

def make(i, start, width_default, d):
    open = d[0]
    close = d[1]
    xmax = d[2]
    xmin = d[3]
    color = ""
    if open>close:
        color = "red"
    else:
        color = "green"
    h = abs(close-open)
    bottom = (start,min(open,close))
    x_tt = (start+(i+1)*width_default)/2
    x_tb = (start+(i+1)*width_default)/2
    x_bt = (start+(i+1)*width_default)/2
    x_bb = (start+(i+1)*width_default)/2
    y_tb = min(open,close) + h
    y_tt = xmax
    y_bt = min(open,close)
    y_bb = xmin
    topline = ((x_tt,y_tt),(x_tb,y_tb))
    bottomline = ((x_bt,y_bt),(x_bb,y_bb))
    return ((bottom, width_default,h,color),topline,bottomline)






if __name__ == "__main__":
    
    
    # Problem 1
    # Please revisit (if need be) the basics of File I/O from the labs and lectures.
    # For testing you code in VSC, you have to use path that works on your system.
    # For submitting to the Autograder, you should keep path as "", because Autograder has 
    # it's own OS and it's own FileSystem, and the path which works on your system may not be valid on the Autograder.
    
    # Please remember to comment out all code for plotting (and the import of matplotlib) before submitting to the Autograder.
    # You can uncomment it for testing on your system and VSC. 
    
    # data6 = get_data("Assignment7/", "payrollwins.txt")
    # print(f"Model built from parameters applied to 10: {(lambda x:0.1250*x + 67.498)(10)}")
    # plt.plot([x for x,_ in data6],[y for _,y in data6],'ro')
    # m_hat, b_hat, R_sq, model = my_scikit_LR(data6)
    # print(f"m_hat: {m_hat}, b_hat: {b_hat}, R^2: {R_sq}")
    # plt.plot([x for x,_ in data6],model(np.array([[x] for x,_ in data6])),'b')
    # print(f"Scikit Model applied to 10: {model(np.array([[10]]))[0][0]}")
    # plt.xlabel("$M cost")
    # plt.ylabel("Wins")
    # plt.title(f"Wins as function of $M cost R^2 = {round(R_sq,3)}")
    # plt.show()
    
    
    
    # Problem 2 
    # for i,j in zip(range(5),p_g()):
    #     print(p(i),p_t(i),p_w(i),j)
    
    # 10000 10000 10000 10000
    # 10200.0 10200.0 10200.0 10200.0
    # 10404.0 10404.0 10404.0 10404.0
    # 10612.08 10612.08 10612.08 10612.08        
    # 10824.3216 10824.3216 10824.3216 10824.3216
    
    # for i,j in zip(range(1,7),c_g()):
    #     print(c(i),c_t(i),c_w(i),j)
    
    # # 9 9 9 9
    # # 82 82 82 82
    # # 756 756 756 756
    # # 7048 7048 7048 7048
    # # 66384 66384 66384 66384
    # # 631072 631072 631072 631072
    
    
    # for i,j in zip(range(5),d_g()):
    #     print(d(i),d_t(i),d_w(i),j)
    # # 1 1 1 1
    # # 4 4 4 4
    # # 13 13 13 13
    # # 40 40 40 40
    # # 121 121 121 121

    
    # Problem 3
    # for i in range(6):
    #     print(f"B({i}) = {B(i)}")
    # # B(0) = 1
    # # B(1) = -0.5
    # # B(2) = 0.16666666666666666
    # # B(3) = -0.0
    # # B(4) = -0.033333333333333305
    # # B(5) = -7.401486830834377e-17
    
    
    # Problem 4
    # data = 2 
    # epsilon = 10e-8
    # print((derivative(f,epsilon)(data)))
    # f_prime = derivative((lambda x:x**2-3*x),epsilon)
    # print(f_prime(data))
    
    
    # problem 5
    
    # Please revisit (if need be) the basics of File I/O form the labs and lectures.
    # For testing you code in VSC, you have to use path that works on your system.
    # But, before submitting to the Autograder, you should keep the path as "", because Autograder has 
    # it's own OS and it's own FileSystem, and the path which works on your system may not be valid on the Autograder.
    
    # Please remember to comment out all code for plotting (and the import of matplotlib) before submitting to the Autograder.
    # You can uncomment it for testing on your system and VSC.
    
    # path,name = "Assignment7/", "income_data.csv"
    # data4 = get_data_2(path,name)      
    # plt.plot([x for x,_ in data4],[y for _,y in data4],'ro')
    # m_hat, b_hat, R_sq, model = my_scikit_LR(data4)
    # print(f"m_hat: {m_hat}, b_hat: {b_hat}, R^2: {R_sq}")
    # plt.plot([x for x,_ in data4],model(np.array([[x] for x,_ in data4])),'b')
    # plt.xlabel("$M cost")
    # plt.ylabel("Wins")
    # plt.title(f"Wins as function of $M cost R^2 = {round(R_sq,3)}")
    # plt.show()
    
    
    #problem 6
    
    # data5 = [[20,15,32,10],[10,14,15,9],[22,23,27,9],[15,16,16,15],[26,12,30,2],[5,30,40,4]]
    
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # start = 0
    
    # default_width = 10
    
    # for i in range(len(data5)):
    #     candle_box,top_line,bottom_line = make(i, start, default_width, data5[i])
    #     print(candle_box)
    #     ax.add_patch(matplotlib.patches.Rectangle(*candle_box[0:3],color = candle_box[3]))
    #     plt.plot([x for x,_ in top_line],[y for _,y in top_line],'black')
    #     plt.plot([x for x,_ in bottom_line],[y for _,y in bottom_line],'black')
    #     start += default_width


    # plt.xlabel("time (hour)")
    # plt.ylabel("Stock X price")
    # plt.title("Candlestick for Stock X mm/dd/yyyy")  
    # plt.xlim([0, 60])
    # plt.ylim([0, 35])
  
    # plt.show()
    
    print()