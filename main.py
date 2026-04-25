import requests
import json
import os

login = input("GitHub user: ")


os.makedirs('outputs', exist_ok=True)
filename = os.path.join('outputs', f'output_{login}.json')

if os.path.exists(filename):
    #debug
    print(f"\nloading local memory...")
    with open(filename, "r") as f:
        output = json.load(f)
else:
     #debug
    print(f"\nloading github api...")

    url = f"https://api.github.com/users/{login}"
    res = requests.get(url)

    if res.status_code != 200:
        print("User not found.")
        exit()

    data = res.json()
    output = {
        "profile": {
            "username": data.get("login"),
            "name": data.get("name") or "Anonymous",
            "email": data.get("email") or "Private",
            "bio": data.get("bio") or "No bio",
            "public_repos": data.get("public_repos") or 0,
            "followers": data.get("followers")or 0,
            "following": data.get("following")or 0
        },
        "repos": [],
        "followers": [],
        "following": []
    }

    repos_res = requests.get(data["repos_url"])

    if repos_res.status_code == 200:
        repos = repos_res.json()
    else:
            repos = []

    for repo in repos:
        repo_data = {
            "name": repo.get("name"),
            "language": repo.get("language"),
            "stars": repo.get("stargazers_count")
        }
        output["repos"].append(repo_data)

    # saving output_{login}.json:
    with open(filename, "w") as f:
        json.dump(output, f, indent=4)

# printing results:
print("\n === PROFILE ===")
for key, value in output["profile"].items():
    print(f"{key}: {value}")

print("\n === REPOSITORIES ===")
for repo in output["repos"]:
    for key, value in repo.items():
        print(f"{key}: {value}")
    print("---")

print(f"\nSaved/loaded from {filename}")
