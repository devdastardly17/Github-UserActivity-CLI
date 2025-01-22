import requests

# Take name and get url 
username = input("github-activity ")
url = f"https://api.github.com/users/{username}/events"   
response = requests.get(url)

try :
    if response.status_code == 200 :
        events = response.json()
        for event in events :
            print(f"{event['type']}, {event['repo']['name']}")
    if response.status_code == 404 :
        raise Exception("User does not exist")

except Exception as e:
    print(f"Error code:{e}")

