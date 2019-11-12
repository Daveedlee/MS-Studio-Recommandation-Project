def convert(s):
    """
    changes fractions in string into floats. 
    """
    try:
        return float(s)
    except ValueError:
        num, denom = s.split('/')
        return float(num) / float(denom)
    
def isFloat(string):
    """
    returns a boolean value for floats in string form.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False