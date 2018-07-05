def list_of_integers():
    '''
    Returns a list of integers from 23 to 100 that are evenly divisible by 7.
    '''
    
    return [i for i in xrange(23, 101) if i % 7 == 0]