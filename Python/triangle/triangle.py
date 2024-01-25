"""Check Triangle Inequality"""

def equilateral(sides):
    # Check For Equilaterals
    a, b, c = sides[0], sides[1], sides[2]
    if a is b is c and a is not 0:
        return True
    return False


def isosceles(sides):
    # Check For Isosceles
    a, b, c = sides[0], sides[1], sides[2]
    if a is b and a is 1 or b is c and b is 1 or a is c and c is 1:
        return False
    elif a is b is c and a is not 0 or b is c and a is not 0:
        return True
    elif a is b and b is not c or a is c and a is not b:
        return True
    elif c is max(sides):
        return False
    return False
    


def scalene(sides):
    # Check For Scalenes
    a, b, c = sides[0], sides[1], sides[2]
    if a is c or c is not max(sides):
        return False
    elif a is not b is not c:
        return True
    return False