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


# Question-> 
"""
4. https://jsonplaceholder.typicode.com/users
   se sab users fetch karo —
   sirf naam aur email print karo har user ka
"""
# Soltuion-> 
print("---------------------------")
try:
    response3 = requests.get("https://jsonplaceholder.typicode.com/users",timeout=5)
    response3.raise_for_status()
    print(f"status code : {response3.status_code}")
    print("-" * 20)

    user_json = response3.json()

   #  print(f"json data : {user_json}")
   #  print("-" * 20)

    print(f"json data 1 : {user_json[0]}")
    print("-" * 20)

    for user in user_json:
      print(f"name : {user['name']} ")
      print("-" * 20)

      print(f"email id : {user['email']}")
      print("-" * 20)

except requests.exceptions.RequestException as e:
    print(f"Error : {e}") 


# Question-> 
"""
5. https://jsonplaceholder.typicode.com/posts
   se GET karo — sirf pehle 5 posts ka 
   title print karo (slice ya loop se)
"""
# Soltuion-> 
print("---------------------------")
try:
   response4 =requests.get("https://jsonplaceholder.typicode.com/posts",timeout=5)
   response4.raise_for_status()

   print(f"status code : {response4.status_code}")
   print("-" * 20)
   json_post = response4.json()
   # print(f"json data : {json_post}")
   print("-" * 20)

   print(f"first 5 post titles : [ ")
   for post in json_post[:5]:
      print(f"  {post['title']},")

   # for i in range(5):
   #    print(f"  {json_post[i]['title']},")
   print(" ] ")
   print("-" * 20)
   # print("-" * 20)
   # print("-" * 20)

except requests.exceptions.RequestException as e:
   print(f"Error : {e}")


# Question-> 
"""
6. https://jsonplaceholder.typicode.com/posts/1
   pe PUT request karo —
   {"title": "updated", "body": "new body", "userId": 1}
   Response print karo
"""
# Soltuion-> 
print("---------------------------")
try:
   post_data = {"title": "updated", "body": "new body", "userId": 1}
   response5 = requests.put("https://jsonplaceholder.typicode.com/posts/1",json=post_data,timeout=10)

   response5.raise_for_status()

   print(f"status code : {response5.status_code}")
   print("-" * 20)

   json_post_data = response5.json()

   print(f"json data : {json_post_data}")
   print("-" * 20)

except requests.exceptions.RequestException as e:
   print(f"Error : {e}")


# Question-> 
"""
7. 3 alag endpoints simultaneously fetch karo 
   threading use karke:
   - /posts/1
   - /users/1  
   - /todos/1
   Har ek ka title/name/title print karo
"""
# Soltuion-> 
print("---------------------------")
import threading

trs = [None,None,None]

def fetch(url,ind):
   try:
      t1 = requests.get(url,timeout=5)
      t1.raise_for_status()
      print(f"status code : {t1.status_code}")

      trs[ind] = t1.json()
   except requests.exceptions.RequestException as e:
      # print(f"Error in {trs[ind] =}  {str[e]}")
      trs[ind] = {"Error : ",str(e)}

urls = [
   "https://jsonplaceholder.typicode.com/posts/1",
   "https://jsonplaceholder.typicode.com/users/1",
   "https://jsonplaceholder.typicode.com/todos/1",
]

Threads = []

for i , url in enumerate(urls):
   t2 = threading.Thread(target=fetch,args=(url,i))
   Threads.append(t2)
   t2.start()

for t in Threads:
   t.join()

post,user,todos = trs

if all(trs):
   print(f"post title : {post['title']}")
   print(f"user name : {user['name']}")
   print(f"todos title : {todos['title']}")

else:
   print(f"Something fails : {trs}")


# Question-> 
"""
8. Ek function banao get_data(url) jo:
   - Request kare
   - Timeout handle kare
   - 4xx/5xx handle kare
   - Connection error handle kare
   - Success pe JSON return kare
   — phir 3 alag URLs pe call karo
"""
# Soltuion-> 
print("---------------------------")

def get_data(url,ind):
   try:
      response8 = requests.get(url,timeout=5)
      response8.raise_for_status()

      print(f"status code {url}:{ind} :: {response8.status_code}")

      json_success = response8.json()

      return json_success
      # print(f"json data : {json_success}")

   except requests.exceptions.ConnectionError as e:
      print(f"Connection error {url}:{ind} :: {e}")
      return None


   except requests.exceptions.Timeout as e:
      print(f"Timout error {url}:{ind} :: {e}")
      return None


   except requests.exceptions.HTTPError as e:
      print(f"Http (4xx, 5xx) error {url}:{ind} :: {e}")
      return None



   except requests.exceptions.RequestException as e:
      print(f"Error {url}:{ind} :: {e}")
      return None

   
   

for ind,url in enumerate(urls):  
   print(get_data(url,ind))

# api.py






#  wrong 

   # import threading
   # try:
   #    Threads = []
   #    response6 = requests.get("https://jsonplaceholder.typicode.com/posts/1",timeout=5)
   #    response7 = requests.get("https://jsonplaceholder.typicode.com/users/1",timeout=5)
   #    response8 = requests.get("https://jsonplaceholder.typicode.com/todos/1",timeout=5)

   #    # print(f"json : {response6.json()}")
   #    # print(f"json : {response7.json()}")
   #    # print(f"json : {response8.json()}")

   #    put_list = [response6,response7,response8]

   #    def showpostusertodos(v):
   #       for i in v:
   #          print(f"title : {i['title']} \ name : {i['name']} \ title : {i['title']}")
            
   #    # for tr in put_list:
   #    trds =  threading.Thread(target=showpostusertodos,args=(put_list,))


   #    Threads.append(trds)

      
   #    trds.start()

   #    trds.join()
   #    for t in Threads :
   #       t.join()
   #       print(f"title : {t['title']}")

   # except requests.exceptions.RequestException as e:
   #    print(f"Error : {e}")