import requests

user_input = input("let me tell you a joke. Give me a topic: ")


url = "https://icanhazdadjoke.com/search"  # can pass it into a variable or directly into requests.get
# '/ search' cos otherwise it wont do the search. it'd pick a random joke

response = requests.get(
    url, 
    headers={"Accept": "application/json"}, 
    params={"term": user_input, "limit": 1} # limit limits the joke to 1
)  # headers is a keyword argument. the use of {} enables us pass as many headers as we want
# params is how we send the query string

data = response.json()  # brings out a single line of joke in readable form

number = data["total_jokes"] # to access the total number of jokes. can also only pass it after json() has been specified

if data["total_jokes"] == 0:
    print(f"I don't have any jokes about {user_input} ") 
elif data["total_jokes"] == 1:
    print(f"I've got one joke about {user_input}. Here it is ")
else:
    print(f"I've got {number} jokes about {user_input}. Here's one: ")

# used a conditional to differentiate no joke, one joke and many jokes

print(data["results"]) #data is a dict and you're trying to access just the results part. if you leave it sans result, it would show a lot





