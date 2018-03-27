#Newton's, method

def Newton(x,g,accuracy = 0.001):
    """
    implement a solution to Newton's method for finding square roots,
    which is a little different than Heron's method.

    the two values that need to bu inputed is the number that's root we are finding
    ,and a guess of any number
    """
    


    while abs(((g**2)- x)) > accuracy:
        g = g - (((g**2)-x)/(2*g))

    return g

                 
#i personally think that Newton's method would be a more efficient method
#mainly because it is able to find cube roots and not just square roots like
#heron's method.
