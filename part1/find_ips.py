import re

def find_ips(inp):
    '''
    Returns a list of valid IPv4 addresses of the form 'x.x.x.x' 
    that are in the input string (separated by at least some whitespace).
    >>> find_ips('this has one ip address 127.0.0.1 not two192.168.1.1 addresses')
    ['127.0.0.1']
    '''
    
    if not inp:
        return []

    pattern = r"(?<!\S)(((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))(?!\S)"
    match = re.findall(pattern, inp, re.MULTILINE)
    return [a[0] for a in match]