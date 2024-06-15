"""
HTTP AND API
-------------------------------------------------------
HTTTP - Hypertext Transfer Protocol

It is a set of rules that the network uses to fetch 
a resouce over the internet. It also enables the communication
between a server and a client.
Any time you type a website address into a browser you
are making an HTTP request. Here the browser is the client
making request a server somewhere else and getting a response
that it translates into webpage(s).
HTTP works in a request - response cycle.
A browser is simply an agent.

https://www.facbook.com - this is a URI. The URI has different components

HTTP Verbs
-------------------------------------------------------
GET Method - is used to make request, where the
resource is sent over the URI.
POST Method - with this the HTTP makes a send a request/data, where the
request/data is stored in the body of the HTTP request.
PUT Method - used to send data to a server to update a record on the server..
PATCH Method - used to send data/request that makes a partial update in the server.
DELETE - with this the HTTP makes a delete request.


API - Application Progamming Interface
---------------------------------------------------------------
An API is simple an interface or an end-point that a user uses
to interact with a resource on the internet. JSON Object

JSON - JavaScript Object Notation
"""
import requests
from requests.exceptions import HTTPError

{
    'userId': 1,
    'name': 'Paul',
    'age': 57,
    'vaccinated': True
}

"""
To install a package into your system, you will use
python -m pip install requests
"""

# Making Request to a server using the GET Method
response = requests.get("https://jsonplaceholder.typicode.com/todos")
# we can access the response of the request that we made
# we can do something like checking the status of the request to know if it was successful or not
# there are plenty HTTP status code with their respective meaning
# they are usually grouped into families
# for example 200 are for request status. So 200 is when a request was successful
response.status_code

if response.status_code == 200:
    print("Successful")
elif response.status_code == 404:
    print("Not Found")


if response:
    print("Ok")
else:
    raise Exception(f"Request was not successful {response.status_code}")


urls = ["https://api.github.com", "https://api.github.com/invalid"]
"""
# CLASSWORK
-------------------------------------------------------------------------------
Write a program that visits both of the urls. Since you have a list of urls, 
you can use a loop here. Make use of the try-except
block in the program. Catch an exception called HTTPError and print the following
"An HTTP error occured" and also catch any other exception and print
"Some other error occured", then handle the situation where even if the error occurs
or not you will print "Me I will still print no matter what"
"""
def sanbox_test():
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as err:
            print(f"An HTTP error occured: {err}")
        except Exception as e:
            print(f"Some other error occured: {e}")
        finally:
            print("Me I will still print no matter what")

# to view the string version of your response
response.text

# give you the content in bytes
response.content

# to view a json version of your response
response.json()

# you can inspect the headers sent with the response
"""
The headers give very useful information, such as the content type
that came with the response payload. Headers usually come in the
form of a dictionary.
"""
# view the content type of the response headers
response.headers['Content-type']
# view the date of the transaction
response.headers['Date']

# Customize our get request
# Query parameters
"""
A query is an additional information that can is attached to the
URL and is used to assign values to specific parameters.
"""
# Example
url = "https://example.com/dadjokes?name=rowyourboot&age=18"
"""
So from the above URL, the query string is everything after
the ?. The & is used to specify more than 1 query string.
"""
def req_query():
    response = requests.get(
        "https://api.github.com/search/repositories",
        params={"q": "language:python", "sort": "stars", "order": "desc"}
    )
    return response

# call the function to make the request
res = req_query()

# we can inspect the response
res_json = res.json()
repos = res_json["items"]
for repo in repos[:4]:
    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print("-------------------------------------")


# Customizing get request by passing headers
def req_headers(url, params, headers):
    response = requests.get(
        url=url,
        params=params,
        headers=headers,
    )
    return response

urll = "https://api.github.com/search/repositories"
paramss = {"q": "language:python", "sort": "stars", "order": "desc"}
headerss = {"Accept": "application/vnd.github.text-match+json"}

res_header = req_headers(urll, paramss, headerss)
print(res_header.status_code)

# Inspect the response from request header call
try:
    res_header_json = res_header.json()
    # print(res_header_json) # an error here to be checked
    first_rep = res_header_json['items'][0]
    print(first_rep['text_matches'][0]["matches"])
except Exception as e:
    print('Error but we move')


# Other HTTP METHODS - POST
"""
The POST HTTP method is used to submit data to a server.
post - https://httpbin.org/post
put - https://httpbin.org/put
patch - https://httpbin.org/patch
"""
post_url = "https://httpbin.org/post"
post_data = {"color": "red", "race": "black"}
post_res = requests.post(
    url=post_url,
    data=post_data
)

print(post_res.status_code)

completed_user = {}
todos = response.json() # this will give us a list
for todo in todos:
    if todo['completed']:
        # add the user to completed_user dictionary
        try:
            completed_user[todo['userId']] += 1
        except KeyError:
            # the userId does not exist
            completed_user[todo['userId']] = 1
