import requests

# --- GET request ---
try:
    response = requests.get("https://api.github.com", timeout=5)
    response.raise_for_status()
    print("GET status:", response.status_code)
    print("GET data:", response.json())
except requests.exceptions.RequestException as e:
    print(f"GET Error: {e}")

print("-" * 50)

# --- POST request ---
try:
    data = {"name": "Afnan"}
    response = requests.post("https://httpbin.org/post", json=data, timeout=10)
    response.raise_for_status()
    print("POST status:", response.status_code)
    print("POST data:", response.json())
except requests.exceptions.RequestException as e:
    print(f"POST Error: {e}")

print("-" * 50)

# --- Headers example ---
try:
    headers = {"Authorization": "Bearer token123"}
    # Replace with a real endpoint that accepts this header
    response = requests.get("https://httpbin.org/headers", headers=headers, timeout=5)
    response.raise_for_status()
    print("Headers response:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Headers Error: {e}")



# galat hai pura..


    # # GET request
    # response = requests.get("https://api.github.com")
    # print(response.status_code)  # 200
    # print(response.json())       # JSON data

    # # POST request
    # data = {"name": "Afnan"}
    # response = requests.post("https://httpbin.org/post", json=data)
    # print(response.json())

    # # Headers
    # headers = {"Authorization": "Bearer token123"}
    # response = requests.get("url", headers=headers)

    # # Error handling
    # try:
    #     response = requests.get("https://api.example.com", timeout=5)
    #     response.raise_for_status()  # 4xx/5xx pe exception
    # except requests.exceptions.RequestException as e:
    #     print(f"Error: {e}")



# api-concepts.py