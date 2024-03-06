###########################################################
# factorial
###########################################################

def factorial(n):
    """
    Recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def tail_factorial(n, a=1):
    """
    Tail-recursive function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n==0:
        return a
    else:
        return tail_factorial(n-1,a=a*n)

d = {}
def memo_factorial(n):
    """
    Memoized function to calculate the factorial of n

    Input:
        n (an integer)
    Returns:
        n! = n*(n-1)*...*2*1
    """
    if n not in d.keys():
        if n == 0:
            d[n]=1
        else:
            d[n] = n*memo_factorial(n-1)
    return d[n]

###########################################################
# only_ints
###########################################################

def only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if not xlist:
        return []
    else:
        if type(int) == xlist:
            return xlist
        else:
            xlist = xlist[1:]
            return xlist

def tail_only_ints(xlist, a=[]):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    if xlist == a:
        return a
    else:
        if type(int) == xlist:
            return xlist
        else:
            xlist = xlist[1:]
            return xlist

d = {}
def memo_only_ints(xlist):
    """
    Recursive function to return a list with all non-ints taken
    out of it.

    Input:
        xlist - a list of elements
    Returns:
        xlist, but with only the 'int'-type elements kept.

    """
    xtup = tuple(xlist)
    if xtup not in d.keys():
        if xlist ==[]:
            d[xtup]=[]
        elif type(xlist[0]) != int:
            d[xtup]=memo_only_ints(xlist[1:])
        else:
            d[xtup] = [xlist[0]]+memo_only_ints(xlist[1:])
    return d[xtup]
                

if __name__ == "__main__":
    # Write your own print statements here
    # to briefly test your code
    x=5
    print(factorial(x))
    print(tail_factorial(x))
    print(memo_factorial(x))

    lst = ["1",2,3,2,2]
    print(only_ints(lst))
    print(tail_only_ints(lst))
    print(memo_only_ints(lst))