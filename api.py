""" import requests

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Send GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print("Fetched Posts:\n")
    
    # Display first 5 posts
    for post in data[:5]:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}") """


""" import requests
import json

url = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"

response = requests.get(url)
print(response.json())

for data in response.json()['items']:
    print("*" * 20)
    print(data['title'])
    print(data['view_count'])

    
print(len(response.json()["items"])) """


""" import requests 
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for f in data:
        print(f"userId: {f['userId']}")
        print(f"id: {f['id']}")
        print(f"title: {f['title']}")
        print(f"body: {f['body']}")
        print() """



""" import requests

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "My New Post",
    "body": "This is the body of the new post.",
    "userId": 1
}

response = requests.post(url, json=new_post)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
 """


""" import requests 

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        #print("Data retrieved!")
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("failed to retireve data {response.status_code}")

Pokemon_name = "typhlosion"
Pokemon_info = get_pokemon_info(Pokemon_name)

if Pokemon_info:
    print(f"Name: {Pokemon_info["name"].capitalize()}")
    print(f"Id: {Pokemon_info["id"]}")
    print(f"Height: {Pokemon_info["height"]}")
    print(f"Weight: {Pokemon_info["weight"]}") """



import requests

base_url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(base_url)

if response.status_code == 200:
    data = response.json()
    print(data)

new_data = {
    "bname" : "Shaurya",
    "game" : "Hollow knight"
} # id auto generated

response = requests.post(base_url, new_data)

print(response.json())
