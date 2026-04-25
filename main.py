import requests
import json

login = input("GitHub user: ")

url = f"https://api.github.com/users/{login}"
res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    output = {
        "profile": {
            "login": data.get("login"),
            "name": data.get("name"),
            "email": data.get("email"),
            "bio": data.get("bio"),
            "public_repos": data.get("public_repos"),
            "followers": data.get("followers"),
            "following": data.get("following"),
        },
        "repos": [],
        "followers": [],
        "following": []
    }
    
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
        output["repos"].append({
            "name": repo.get("name"),
            "language": repo.get("language"),
            "stars": repo.get("stargazers_count")
        })

        print("\n Name: ", repo.get("name"))
        print("Language: ", repo.get("language") or "N/A")
        print("Stars: ", repo.get("stargazers_count") or 0)
    
    filename = f"output_{login}.json"

    with open(filename, "w") as f:
        json.dump(output, f, indent=4)
    print(f"\nSaved to {filename}")

else:
    print("User not found.")