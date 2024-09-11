import requests
import argparse

def get_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    
    if response.status_code == 200:
        events = response.json()
        for event in events:
            print(f"Event Type: {event['type']}")
            print(f"Repository: {event['repo']['name']}")
            print(f"Date: {event['created_at']}")
            print("-" * 40)
    else:
        print(f"Failed to retrieve data: {response.status_code}")

def main():
    parser = argparse.ArgumentParser(description="Query GitHub activity for a given username.")
    parser.add_argument('username', type=str, help='GitHub username to query')
    args = parser.parse_args()
    
    get_github_activity(args.username)

if __name__ == "__main__":
    main()
