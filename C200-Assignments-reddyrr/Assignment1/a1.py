# We have added import math
# It's only needed once
import math

# Problem 1
#input radius r, height h
#return volume
def c(r,h):
    volume = (1/3)*math.pi*(r**2)*h # calculate
    volume = round(volume,2)   #round the value
    return volume   #return value
    
# Problem 2
#input t days
#output oxygen content percent of its normal level
def f(t):
    oxygen = 100*(((t**2)+10*t+100)/((t**2)+20*t+100))   # calculate
    oxygen = round(oxygen,2)   #round the value
    return oxygen   #return value

# Problem 3
#input t hours
#return percent watching tv
def P(t):
    watching_TV = (.01354*(t**4))-.49375*(t**3) +2.58333*(t**2)+3.8*t+31.60704# calculate
    watching_TV = round(watching_TV, 2)   #round the value
    return watching_TV   #return value


# problem 4
#input x percent
#return millions of dollars
def cost(x):
    dollars = (.5*x)/(100-x)# calculate
    dollars = round(dollars,2)   #round the value
    return dollars   #return value


# Problem 5
#input dosage a mg and years t
#return child dosage mg
def D(t,a):
    dosage = ((t+1)/24)*a    # calculate
    dosage = round(dosage,2)   #round the value
    return dosage   #return value
 
# Problem 6
#input number of susceptible, but healthy children
#output number of the infected children
# use math.ceil() before returning your final answer.
def I(S):
    infected = 192*math.log((S/762),2)-S+763   # calculate
    infected = math.ceil(infected)   #round up the value
    return infected    #return value


# Problem 7
#input number of items 
#output total cost 
# q > 0
def C(q):
    cost = .01*(q**3)-.6*(q**2)+13*q+1000   # calculate
    cost = round(cost,2)   #round the value
    return cost   #return value

#input number of items
#output average cost
def A(q):
    cost = C(q)/q   # calculate
    cost = round(cost,2)   #round the value
    return cost   #return value

# Problem 8
#input months t=0,...,11
#output items sold x 1000
def hh(t):
    items = (532)/(1+869*(math.exp((-1.33*t))))   # calculate
    items = math.floor(items)   #round down the value
    return items   #return value

# Problem 9
#input time seconds
#output feet
def height(t):
    height = -16*(t**2)+64*t+80   # calculate
    height = round(height,2)   #round the value
    return height   #return value

# Problem 10
#input t hours
#output percent treatment
def B(t):
    treatment = (0.44*(t**4)+700)/(.1*(t**4)+7)   # calculate
    treatment = round(treatment,2)   #round the value
    return treatment   #return value

# Problem 11
#input coefficients for quadratic and value
#output True if value is root, False otherwise
def quad(a,b,c,x):
    quadratic = a*(x**2)+b*x+c   # calculate
    root = bool(quadratic == 0)   #true or false 
    return root   #return value


#input P principle, n times per year, t years, r rate
#output dollars
def R(P,r,n,t):
    formula = P*(((1+(r/n))**(n*t)-1)/(r/n))   # calculate
    formula = round(formula,2)   #round the value
    return formula   #return value

#input dimensions w,l,h for width, length, height of a 
# rectangular solid
#output total surface area
def S(w,l,h):
    area = 2*(w*l)+ 2*(h*l)+2*(h*w)   # calculate
    return area   #return value



if __name__ == "__main__":
    """
    If you want to do some of your own testing in this file, 
    please put any print statements you want to try in 
    this if statement.
    """

    #problem 1
    #volume of cone
    # print(c(2,5)) 
    # print(c(3,7))

    #problem 2
    #oxygen content
    # print(f(0))
    # print(f(10))

    #problem 3
    #tv watching
    # print(P(0))
    # print(P(3))
    # print(P(8))

    #problem 4
    #toxic waste
    # print(cost(50))
    # print(cost(70))
    # print(cost(90))

    #problem 5
    # cowling's rule
    # print(D(4,500))
    
    #problem 6
    #flu outbreak
     #S = 100
    # print(I(100))
     #S = 300
    # print(I(300)) 

    #problem 7
    # average cost
    # make your own inputs/outputs
    # print(C(101))
    # print(A(101))
    
    #problem 8
    print(hh(0))
    print(hh(5))
    print(hh(10))

    #problem 9
    print(height(5))
   
    #problem 10        
    #make your own inputs/outputs
    print(B(10))


    #problem 11
    #quadratic roots
    print(quad(2,5,-12,-4))
    print(quad(2,5,-12,3/2))
    print(quad(2,5,-12,1))

    # problem 12
     #Sinking Fund
    P = 22000
    n = 1
    t = 7
    r = 6/100
    print(R(P,r,n,t))
    P = 500
    n = 12
    t = 20
    r = 4/100
    print(R(P,r,n,t))
    P = 1200
    n = 4
    t = 10
    r = 8/100
    print(R(P,r,n,t))

    #problem 13
    #make your own inputs/outputs
    print(S(5,2,1))