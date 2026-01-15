import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("Error: Unable to fetch users")
            return None

        users = response.json()

        
        count = min(num_users, len(users))

        for i in range(count):
            user = users[i]

            name = user.get("name")
            email = user.get("email")
            city = user.get("address", {}).get("city")

            print("Name :", name)
            print("Email:", email)
            print("City :", city)
            print("-" * 20)

    except requests.exceptions.RequestException:
        print("Error: Network problem occurred")
        return None


fetch_and_display_users(3)
fetch_and_display_users(15)

