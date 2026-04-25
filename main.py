import requests
import json

login = input("GitHub user: ")

url = f"https://api.github.com/users/{login}"
res = requests.get(url)
print(res)

if res.status_code == 200:
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
    
    # 
    # print("Name:", data.get("name") or "Anonymous")
    # print("Username: ", data.get("login"))
    # print("Email: ", data.get("email") or "Private")
    # print("Bio: ", data.get("bio") or "no bio")
    # print("Public repos: ", data.get("public_repos") or 0)
    # print("Followers: ", data.get("followers") or 0)
    # print("Following: ", data.get("following") or 0)

    # 

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

        # print("\n Name: ", repo.get("name"))
        # print("Language: ", repo.get("language") or "N/A")
        # print("Stars: ", repo.get("stargazers_count") or 0)
    
    filename = f"output_{login}.json"

    with open(filename, "w") as f:
        json.dump(output, f, indent=4)
    
    print("\n === PROFILE ===")
    for key, value in output["profile"].items():
        print(f"{key}: {value}")

    print("\n === REPOSITORIES ===")
    for repo in output["repos"]:
        for key, value in repo.items():
            print(f"{key}: {value}")
        print("---")

    print(f"\nSaved to {filename}")

else:
    print("User not found.")