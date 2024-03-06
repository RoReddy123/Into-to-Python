import math

#problem 1
#input real number
#return real number
def g(x):
    if (x == 0):
       return 1
    else:
        return x+2 


#problem 2
#input year 1977-1997
#return percent income or "YearError: year" if year 
#is outside range
def f(t):
    if (t >= 1977 and t<=1984):
        return (2/7)*(t-1977) + 12
    elif (t > 1984 and t<= 1987):
        return (t-1977)+7
    elif (t>1987 and t<= 1997):
        return (3/5)*(t-1977)+11
    else:
        return "YearError:" + str(t)
        


#problem 3
# input t years = 0, 1, then 2
# output dollars or error in the format YearError: t
def h(t):
    
    def h_0(t):
        h0 = round(110/((1/2)*t+1), 2)
        return h0

    def h_1(t):
        h1 = round(26 * (((1/4) * (t**2) - 1)**2) + 52, 2)
        return h1

    if (t >=0 and t <=2):
        result = round(h_0(t) - h_1(t), 2)
        return "$" + str(result)
    else: return "YearError: " + str(t)



#problem 4
#input tuple (a,b,c) coefficients
#output tuple roots (x_1, x_2) where x_1 >= x_2
def q(coefficients):
    (a,b,c) = coefficients
    x1 = (-b + (((b**2) - (4*a*c)) ** .5))/(2*a)
    x2 = (-b - (((b**2) - (4*a*c)) ** .5))/(2*a)
    if (x1.real >= x2.real): return (x1,x2)
    else: return (x2,x1)


#problem 5
#input [arg1,op,arg2,ans]
#output boolean (True or False) depending on the result of arg1 op arg2 == ans
def eq(lst):
    [arg1,op,arg2,answer] = lst
    if (op == "*"):
        newanswermulti = arg1 * arg2
        if (newanswermulti == answer): return True
        else: return False
    elif (op == "**"):
        newanswerexp = arg1 ** arg2
        if (newanswerexp == answer): return True
        else: return False
    elif (op == "+"):
        newansweradd = arg1 + arg2
        if (newansweradd == answer): return True
        else: return False
    elif (op == "-"):
        newanswerminus = arg1 - arg2
        if (newanswerminus == answer): return True
        else: return False
    elif (op == "/"):
        newanswerdivide = arg1 / arg2
        if (newanswerdivide == answer): return True
        else:return False
    else:return False
    

        



#problem 6
#input string of COVID symptoms "ABC", "ACB",...,"CBA"
#output 'very likely', 'likely', 'somewhat likely' based on severity
def covid(symptoms):
    symptom = symptoms
    if (symptom == "ABC" or symptom == "ACB"):
        return "very likely"
    if (symptom == "BAC" or symptom == "BCA"):
        return "likely"
    if (symptom == "CAB" or symptom == "CBA"):
        return "somewhat likely"




#problem 7
#INPUT two numbers
#RETURN maximum of the two
#You cannot use Python's max() function
#You must use if, elif, else (or some combination)
def max2d(x,y):
    if (x > y):
        return x
    else:
        return y



# #INPUT 3 numbers
# #RETURN maximum of the three
# #You must use your max2D function
def max3d(x,y,z):
    return max2d(x,max2d(y,z))




#problem 8
#INPUT [name0,name1, votes] where votes is a non-empty list of 0,1
#RETURN a tuple (name, c, t) where name is the winner, c is the number of winning votes
#t is the total votes cast 

def decision(data):
    [name0, name1, votes] = data
    count0 = 0
    count1 = 0
    for item in votes:
        if (item == 0):
            count0 += 1
        if (item == 1):
            count1 += 1

    sumvotes = len(votes)
    if (count0 > count1):return (name0, count0, sumvotes)
    elif (count0 == count1):
        tie = "tie"
        return (tie, count0, sumvotes)
    else: return (name1, count1, sumvotes)




#problem 9 
#INPUT three values: all have values or two have values and the remain has None
#OUTPUT for two values, return the computed None variable
#for three values return True or False using isclose(x,y,abs_tol = 0.001)
#remember to convert degrees to radians
def solve(theta, opposite, adjacent):
    if (opposite is None):
        oppnone = (math.tan(math.radians(theta))) * adjacent
        return oppnone
    elif (theta is None):
        thetanone = math.degrees(math.atan(opposite/adjacent))
        return thetanone
    elif (adjacent is None):
        adjnone = opposite / (math.tan(math.radians(theta)))
        return adjnone
    else:
        left,right = math.tan(math.radians(theta)),opposite/adjacent
        return math.isclose(left, right, abs_tol = 0.001)
        
      



# problem 10
def future(A, r):
    
    return round((20/100)*A*(r/12) / (((1+(r/12))**(12*2))-1) , 2)
    

if __name__ == "__main__":
    """
    The code in "__main__" is not being graded, but a tool for you to test 
    your code outside of the unit testing Feel free to add print statements. 
    You should uncomment *after* you've completed the function
    """

    #problem 1 
    print(g(0))
    print(g(1))
    print(g(1.01))

    #problem 2
    print(f(1976))
    print(f(1977))
    print(f(1985))
    print(f(1988))
    print(f(2000))

    #problem 3
    print(h(0))
    print(h(1))
    print(h(1.5))
    print(h(2))
    print(h(3))

    #problem 4 
    print(q((1,0,-1)))
    print(q((6,-1,-35)))
    print(q((1,-7,-7)))

    #problem 5 
    print(eq([14, "/",2, 7]))
    print(eq([20, "*",19, 381]))
    print(eq([20, "*",19, 380]))
    print(eq([2,"**",3,8]))
    print(eq([1.1,'-',1,.1])) #saw in class this doesn't work! (will return False)

    #problem 6 
    print(covid('ABC'),covid('ACB'))
    print(covid('BAC'),covid('BCA'))
    print(covid('CAB'),covid('CBA'))

    #problem 7
    print(max3d(1,2,3))
    print(max3d(1,3,2))
    print(max3d(3,2,1))

    #problem 8 
    data0 = ['B','Z',[0,1,1,0,1,0,0]]
    print(decision(data0))
    data1 = ['B', 'Z',[1,0,1]]
    print(decision(data1))
    data2 = ['B', 'Z',[1,0,1,0,1,1,0,0]]
    print(decision(data2))


    #problem 9 
    print(solve(5,None,105600))
    print(solve(None,9238.9,105600))
    print(solve(5,9238.8,None))
    print(solve(5,9238.8,105600))
    print(solve(5,9100,105600))

    #problem 10 
    home_price, rate = 54478, 0.13
    t,n = 2,12                         #years, monthly
    payment = future(home_price,rate)
    print(f"{n} payments yearly for {t} years requires ${payment}")
    #confirm this achieves 50000
    A = round(payment*((1 + rate/n)**(t*n)-1)/(rate/n),2)
    print(A)
