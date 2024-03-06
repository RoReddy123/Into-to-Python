import math

# Problem 1
#input percent_decrease as positive integer, r as float
#output hours as float
def next_injection(percent_decrease,r):
    c = int(abs(percent_decrease))
    rate = float(r)
    hours = float(math.log(c/100) / (-rate))
    return round(hours,3)

#input hours as float
#output tuple (x,y) where x hours, y minutes
def convert_HM(hours):
    hours = float(hours)
    hours_whole = math.floor(hours)
    min_dec = (hours - hours_whole) * 60
    min = math.floor(min_dec)
    return hours_whole, min

# Problem 2
#input x number and possibly empty list of numbers
#output number, sum of list, list where sum list is <= x
def m(x,lst):
    def sumlst(lst):
        return sum(lst)
     
    max = []
    for i in range(len(lst)):
        if sumlst(lst[:i+1]) <= x:
            max = lst[:i+1]
        else:
            break
    
    return (x, sumlst(max), max)


if __name__ == "__main__":

       ## Problem 1
    data = [[50, 0.2],[35, 0.44],[20,.01]]

    for d in data:
        hours = next_injection(*d)
        h_, m_ = convert_HM(hours)
        print(hours, h_,m_ , math.isclose(hours,h_ + m_/60,abs_tol = .1))

    ## Problem 2
    data = [[0,[0,0,1]],[1,[0,0,0]],[2,[1,0,1,0,2]],
                [1,[2,1,0]],[4,[1,0,2,0,.5,.1,0,5]],
                [5,[5,5]],[2,[-1,2,0,1,-1]],[1,[]]]

    for d in data:
        print(m(*d))