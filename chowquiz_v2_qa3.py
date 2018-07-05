'''
Using Python 2.7 or 3.3+ syntax/semantics, please fill out the bodies of
the included functions to include implementations of what is described in the
docstrings.
'''

def list_of_integers():
    '''
    Returns a list of integers from 23 to 100 that are evenly divisible by 7.
    '''
    pass

def dict_mapping():
    '''
    Returns a dictionary mapping integers to their 2.5th root for all integers
    from 2 up to 100 (including 100). Hint: 2.5th root of number 2 is 1.319507
    '''
    pass

def find_ips(inp):
    '''
    Returns a list of valid IPv4 addresses of the form 'x.x.x.x' 
    that are in the input string (separated by at least some whitespace).
    >>> find_ips('this has one ip address 127.0.0.1 not two192.168.1.1 addresses')
    ['127.0.0.1']
    '''
    pass

def generate_cubes_until(modulus):
    '''
    Generates the cubes of integers greater than 0 until the next cube is evenly
    divisible by provided argument (reminder of the division of the cube
    and the argument is zero).
    >>> list(generate_cubes_until(25))
    [1, 8, 27, 64]
    '''
    pass

  
####################################################################### CLASS

"""

Following Python best practices, define a class structure for a Circle
with static methods, class methods, instance methods, and properties
via instance methods. The class must:
1. inherit from object,
2. include a base initializer that stores a radius and optional color,
3. provide a method to validate if a color is "red", "green", or "blue",
   returning True when a color is valid, and False in all other cases
4. provide a method for creating a circle instance from a radius,
5. provide a method for creating a circle instance rom a circumference, 
6. provide a method for calculating a circumference from a radius, 
7. provide a method to return circumference of the circle,
8. provide a method to return area of the circle,
9. provide a method to return the area of a circle scaled by provided factor
   (area of a circle which radius has been scaled by provided factor).
10. implement the following Circle method:
def area_scale_dict(self):
   '''
   Return a dictionary of circle radiuses mapped to area of the Circle from 10% 
   of the radius up to 100% (the radius), incrementing by 5% with each step.
   '''

"""


####################################################################### API

"""

1. Write automated API tests for the API endpoints defined below.

a) Login API definition:

This API serves purpose of authenticating users. The endpoint handles POST method
only. All request parameters are required. Upon successful authentication
the endpoint will return so called auth token. The token needs to be used
with all other API endpoints.

Endpoint: https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/auth
Headers:
Content-Type: application/json,
Accept: application/json

Payload:
{
  "identity": "username or email as string",
  "credentials" : "password as string"
}

Successful response:
Status 200
{
  "token" : "auth token as string"
}

Error response:
A meaningful REST API status and the following JSON:
{
  "error" : {
    "code" : 400,
    "message" : "a message describing this specific error case"
  }
}

Our mock supports the following to requests. Note the extra header triggering a specific response.

curl -v -XPOST -H "X-Mock-Response-Code: 200" https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/auth
curl -v -XPOST -H "X-Mock-Response-Code: 400" https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/auth

b) User profile API definition

This API serves purpose of retrieving authenticated user profile.
It requires auth token to be sent as X-API-token HTTP header.
The endpoint supports GET method only.

Endpoint: https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/users/current
Headers:
Content-Type: application/json,
Accept: application/json
X-Auth-Token: token-returned-by-login-request

Successful response to GET request:
{
  "user_id" : "user id as string",
  "date_of_birth : "1985-11-28",
  "avatar_url : "URL to an image or null",
  "followers_count" : 123
}

Our mock supports the following to requests. Note the extra header triggering a specific response.

curl -v -H "X-Mock-Response-Code: 200" https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/users/current
curl -v -H "X-Mock-Response-Code: 401" https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/users/current
    
"""

"""

2. For the above API endpoint, write questions you would like to ask an engineer
and a product manager in order to define good range of automated tests
to be written.

"""

