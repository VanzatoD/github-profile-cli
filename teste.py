import requests
import json

login = input("GitHub user: ")

url = f"https://api.github.com/users/{login}"
res = requests.get(url)

if res.status_code == 200:
    data = res.json()

    print("\n === PROFILE ===")
    print("Name:", data.get("name") or "Anonymous")
    print("Username: ", data.get("login"))
    print("Email: ", data.get("email") or "Private")
    print("Bio: ", data.get("bio") or "no bio")
    print("Public repos: ", data.get("public_repos") or 0)
    print("Followers: ", data.get("followers") or 0)
    print("Following: ", data.get("following") or 0)

    print("\n === REPOSITORIES ===")

    repos = requests.get(data["repos_url"]).json()

    for repo in repos:
        print("\n Name: ", repo.get("name"))
        print("Language: ", repo.get("language") or "N/A")
        print("Stars: ", repo.get("stargazers_count") or 0)

else:
    print("User not found.")