import math
# import matplotlib.pyplot as plt



###########################################################################
# Functions for Problem 1
###########################################################################
#INPUT dlst = [day, month, year]
#RETURN string corresponding to the day of the week (i.e. "Mon", "Sun", etc)
week = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thu", 5:"Fri", 6:"Sat", 7:"Sun"}
def a(dlst):
    [d,m,y] = dlst
    fun = y-((14-m)/12)
    return fun

def b(dlst):
    x = a(dlst) + (a(dlst)/4) - (a(dlst)/100) + (a(dlst)/400)
    return math.floor(x)

def c(dlst):
    [d,m,y] = dlst
    return m + (12*((14-m)/12)) - 2

def day(dlst):
    [d,m,y] = dlst
    return week.get((d + b(dlst) + (31*(c(dlst)/12)))%7)


###########################################################################
# Functions for Problem 2
###########################################################################
#INPUT t = (a,b,c)
#RETURN return complex or real roots
def q(t):
    (a,b,c) = t
    d = (b**2)-(4*a*c)
    if d>=0:
        r1 = round((-b + math.sqrt(d)) / (2*a),2)
        r2 = round((-b - math.sqrt(d)) / (2*a),2)
        if r1<r2:
            return (r1,r2)
        else:
            return (r2,r1)
    else:
        r = -b/(2*a)
        r1 = math.sqrt(-d)/(2*a)
        r2 = -math.sqrt(-d)/(2*a)
        rround = round(r,2)
        ir = round(r1,2)
        i2r = round(r2,2)
        return complex(rround,ir), complex(rround,i2r)



###########################################################################
# Functions for Problem 3
###########################################################################
#INPUT a nested list of people encoded as 0's and 1's. v0 and v1 are the respective lists respresenting the people pairs.
# You'll be comparing the smallest degree of difference between each sublist representing each person.
# RETURN person pair with the smallest degree (smallest degree of difference between the person pair lists)
def inner_prod(v0,v1):
    sum = 0
    for i in range(len(v0)):
        sum += v0[i] * v1[i]
    return sum

def mag(v):
    return math.sqrt(inner_prod(v,v))

def angle(v0,v1):
    return round((180/math.pi)*math.acos(inner_prod(v0,v1)/(mag(v0)*mag(v1))),2)
    
def match(people):
    new = []
    for i in range(len(people)):
        for j in range(i+1,len(people)):
            new.append([people[i],people[j],angle(people[i],people[j])])

    return new
    
def best_match(scores):
    small = 360
    for i in scores:
        if small > i[2]:
            small = i[2]
            lst = (i[0], i[1], i[2])
    return lst



###########################################################################
# Functions for Problem 4
###########################################################################
#INPUT tuple of quadratic (ax^2 + bx + c)
#RETURN tuple (m,n) cofficients for real solutions a(x+m)^2 + n = 0
#CONSTRAINT round to 2 places
def c_s(coefficients):
    (a,b,c) = coefficients
    m = b/(2*a)
    n = c-((b**2)/(4*a))
    real = b**2+4*a*c
    return round(m,2),round(n,2)



#INPUT coefficients for quadratic ax^2 + bx + c 
#RETURN return real roots uses c_s
def q_(coefficients):
    m,n = c_s(coefficients)
    roots = round(-m-math.sqrt(-n),2), round(-m+math.sqrt(-n),2)
    return roots



###########################################################################
# Functions for Problem 5
###########################################################################
# INPUT List of numbers
# RETURN Various means
def mean(lst):
    sumlst = 0
    for i in lst:
        sumlst += i
    return round(sumlst/len(lst),2)


def var(lst):
    mu = mean(lst)
    summu = 0
    for i in lst:
        summu += (i-mu)**2
    return round(summu/len(lst),2)

def std(lst):
    return round(math.sqrt(var(lst)),2)

def mean_centered(lst):
    newlst = []
    m=mean(lst)
    for i in lst:
        newlst.append(i-m)
    return newlst



###########################################################################
# Functions for Problem 6
###########################################################################
# INPUT supply and demand coefficients
# RETURN solution of quadratic equations
def equi(s,d):
    a1 = s[0]
    a2 = d[0]
    b1 = s[1]
    b2 = d[1]
    c1 = s[2]
    c2 = d[2]
    newa = a1-a2
    newb = b1-b2
    newc = c1-c2
    t = (newa, newb, newc)
    r1,r2 = q(t)
    if r1 > r2:
        return r1,r2
    else:
        return r2,r1



###########################################################################
# Functions for Problem 7
###########################################################################
#INPUT parameters to LV model
#OUTPUT two lists history_rabbit, history_fox of populations
def rabbit_fox(br,dr,df,bf,rabbit,fox,time_limit):
    i = 0
    history_rabbit=[rabbit]
    history_fox=[fox]
    while i <= time_limit:
        rab = math.ceil(rabbit+(rabbit*br)-(rabbit*fox*dr))
        fo = math.ceil(fox+(fox*bf*rabbit*dr)-(fox*df))
        history_rabbit.append(rab)
        history_fox.append(fo)       
        rabbit = rab
        fox = fo
        i+=1
    return history_rabbit[:time_limit],history_fox[:time_limit]




###########################################################################
# Functions for Problem 8
###########################################################################
# INPUT container, sample size n
# OUTPUT random selection of size n in any order
# CONSTRAINT uses random 
# This is with replacement
def sub_strings(str,cnt):
    for i in range(len(str)):
        for j in range(i+1, len(str)+1):
            substring = str[i:j]
            cnt[substring] = cnt.get(substring,0)+1
    return cnt

    



###########################################################################
# Functions for Problem 9
###########################################################################
#INPUT values for annuity
#OUTPUT deposit amount needed
def deposit(S,i,n):
    return round((S*i) / (((1+i)**n)-1) ,2)



#INPUT sinking fund values except deposit
#OUTPUT a list of period, deposit, interest, accrued total fund
def sinking_fund(final_amt, r, m, y):
    i=r/m
    n = y * m
    R = deposit(final_amt,i,n)

    payment_schedule = [[0,R,0,R]]
    total_fund = 0

    for j in range(1,n):
        lastTotal = payment_schedule[j-1][3]
        interest = round(lastTotal*i, 2)
        total_fund = round(lastTotal + interest + R, 2)
        payment_schedule.append([j, R, interest, total_fund])
    return payment_schedule




###########################################################################
# Functions for Problem 10
###########################################################################
#INPUT list of numbers
#OUTPUT Boolean if geometric series
def is_geometric_sequence(lst):
    if (len(lst) <= 2):
        return 0
    for i in range(2,len(lst)):
        if (lst[i]/lst[i-1] != lst[1]/lst[0]):
            return False
    return True



###########################################################################
# Functions for Problem 11
###########################################################################
#INPUT portfolio of stock price, shares, market
#OUTPUT current total value
def value(portfolio, market):
     pass





if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.

    You **do not** have to put anything here
    """

    # #problem 1  
    # print(day([14,2,2000]))
    # print(day([14,2,1963]))
    # print(day([14,2,1972]))

    # # #problem 2   
    # print(q((3,4,2)))
    # print(q((1,3,-4)))
    # print(q((1,-2,-4)))

    # # #problem 3
    # people0 = [[0,1,1],[1,0,0],[1,1,1]]
    # print(match(people0))
    # print(best_match(match(people0)))

    # people1 = [[0,1,1,0,0,0,1],
    #            [1,1,0,1,1,1,0],
    #            [1,0,1,1,0,1,1],
    #            [1,0,0,1,1,0,0],
    #            [1,1,1,0,0,1,0]]
    # print(best_match(match(people1)))
    # # #output is ([1, 1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 1, 0, 0], 39.23)

    # v0,v1 = (2,3,-1), (1,-3,5)
    # print(angle(v0,v1)) #122.83

    # v0,v1 = (3,4,-1),(2,-1,1)
    # print(angle(v0,v1)) #85.41

    # v0,v1 = (5,-1,1),(1,1,-1)
    # print(angle(v0,v1)) #70.53


    # # #problem 4    
    print(q((1,-4,-8)), q_((1,-4,-8)))
    print(q((1,3,-4)),q_((1,3,-4)))
   
    
    # # #problem 5
    # lst = [1,3,3,2,9,10]

    # print(mean(lst))
    # print(var(lst))
    # print(std(lst))
    # print(mean(mean_centered(lst)))

    # # #problem 6 
    # s = (-.025,-.5,60)
    # d = (0.02,.6,20)
    # print(equi(s,d))
    
    # s = (5,7,-350)
    # d = (4,-8,1000)

    # print(equi(s,d))

    # #problem 7 not done
    # br = 0.03
    # dr = 0.0004
    # df = 0.25
    # bf = 0.11
    # rabbit = 3000  #initial population size
    # fox = 200  #initial population size
    # time_limit = 2000
    # history_rabbit, history_fox = rabbit_fox(br,dr,df,bf,rabbit,fox, time_limit)

    # # # #uncomment to see time, rabbit, fox populations
    # for j in range(0,2000,200):
    #     print(j, history_rabbit[j], history_fox[j])


    # plt.plot(list(range(0,time_limit)),history_rabbit)
    # plt.plot(list(range(0,time_limit)),history_fox)
    # plt.xlabel("Time")
    # plt.ylabel("Population Size")
    # plt.legend(["Rabbit","Fox"])
    # plt.title("Lotka-Volterra Model for Rabbit & Fox")
    # plt.show()

    
    # #problem 8   
    # data = ["abcabc","ccccc",""]
    # for d in data:
    #     cnt = {}
    #     sub_strings(d,cnt)
    #     print(cnt)

    # # #problem 9 
    # S = 30000
    # m = 4
    # r = 10/100
    # y = 2
    # for i in sinking_fund(S,r,m,y):
    #     print(i)


    #problem 10
    # data = [[1,2,4,6],[2,4,8,16],[10,30,90,270,810,2430]]
    # for d in data:
    #     print(is_geometric_sequence(d))


    # #problem 11  not done
    # portfolios =  {'A':{'stock':{'x':(41.45,45),'y':(22.20,1000)}},
    # 'B':{'stock':{'x':(33.45,15),'y':(12.20,400)}}}
    # market = {'x':43.00, 'y':22.50}


    # for name, portfolio in portfolios.items():
    #     print(f"{name} {value(portfolio,market)}")
