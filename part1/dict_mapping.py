def dict_mapping():
    '''
    Returns a dictionary mapping integers to their 2.5th root for all integers
    from 2 up to 100 (including 100). Hint: 2.5th root of number 2 is 1.319507
    '''
    
    result = {}

    for i in xrange(2, 101):
        result[i] = i**(1/float(2.5))

    return result