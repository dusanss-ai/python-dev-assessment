import requests


def fetch_and_display_users(num_users):
    try:

        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        users = response.json()

        for user in users[:num_users]:
            name = user['name']
            email = user['email']
            city = user['address']['city']
            print(f"Name: {name} | Email: {email} | City: {city}")
        
    except requests.RequestException:   
        print("Network issues")
        return None
    except (KeyError, TypeError):
        print("The API returned an unexpected structure.")
        return None



fetch_and_display_users(4)
fetch_and_display_users(16)
