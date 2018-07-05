Question regarding to API

1. What's the character length limit on username and password?
2. What's the limit of character being used for username and password? (E.g. Is chinese character supported?)
3. How's the auth token get created?  Does it created after auth request or created during user account creation?
4. Follow up question from #3, how does user profile api verify the token is valid?
5. Follow up queston from #3, if the token is created after auth request, what is the expiration time of the token?
6. What is the request limit for each session for both apis before throttling to prevent DDoS attack or system overloaded?
7. Is there an api for resetting password?  If there is, it will be ideal to create auth request test right after password reset.
8. Similiar to quetion #7, is there an api for editing user profile?
9. Is there exponential backoff mechanic behind the apis?  If there is, a test that verify the trigger and backoff timing will be created.
10. How quickly the "followers_count" from profile api get updated when there is a new follower?


Required python libraries:

unittests2
hypothesis
pytest
requests

How to run the unittest and api test:

Run "pytest" at the root of the project directory