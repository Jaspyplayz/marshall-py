# Lesson 39

def gcd(x, y):

    if y == 0:
        return x
    
    return gcd(y, x % y)

        
