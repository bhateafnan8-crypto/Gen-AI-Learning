import requests
# Question-> 
"""
1. https://jsonplaceholder.typicode.com/posts/1
   se GET request karo aur 
   title aur body print karo
"""
# Soltuion-> 
print("---------------------------")

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1",timeout=5)
    response.raise_for_status()
    print(f"get status : {response.status_code}")
    print("-" * 20)

    print(f"json data : {response.json()}")
    print("-" * 20)

    json_data = response.json()
    print(f"title : {json_data['title']}")
    print("-" * 20)

    print(f"body : {json_data['body']}")
    
   #  print(f"title : {response['title']}")
   #  print(f"body : {response['body']}")
except requests.exceptions.RequestException as e:
    print(f"Error : {e}")


# Question-> 
"""
2. https://jsonplaceholder.typicode.com/posts
   pe POST request karo — 
   {"title": "test", "body": "hello", "userId": 1}
   Response status code aur id print karo
"""
# Soltuion-> 
print("---------------------------")

try:
   data_post = {"title": "test", "body": "hello", "userId": 1}
   response1 = requests.post("https://jsonplaceholder.typicode.com/posts",json=data_post,timeout=10)
   response1.raise_for_status()
   print(f"status code : {response1.status_code}")
   print("-" * 20)

   print(f"json data : {response1.json()}")
   print("-" * 20)

   post_data = response1.json()
   print(f"id : {post_data['id']}")

except requests.exceptions.RequestException as e:
    print(f"Error : {e}")


# Question-> 
"""
3. https://jsonplaceholder.typicode.com/posts/999
   fetch karo — 404 handle karo 
   raise_for_status() se
"""
# Soltuion-> 
print("---------------------------")

try:
    response2 = requests.get("https://jsonplaceholder.typicode.com/posts/999",timeout=5)
    response2.raise_for_status()
    json_fetch = response2.json()
    print(f"status code : {response2.status_code}")
    print(f"json data : {json_fetch}")
    print("-" * 20)

    print(f"title : {json_data['title']}")
    print("-" * 20)

except requests.exceptions.RequestException as e:
   print(f"Error : {e}")


# api.py