# GitHub Profile CLI 
A command-line tool that fetches and displays GitHub user data using the GitHub API. 

## Features

* Fetch user profile data (name, bio, followers, etc.)
* List public repositories
* Display repository language and stars
* Clean terminal output

## Installation

```
git clone https://github.com/VanzatoD/github-profile-cli.git
cd github-profile-cli

pip install -r requirements.txt
```

## Usage

```
python main.py
```

Then enter a GitHub username when prompted.


## Planned Features

* [x] Export data to JSON files
* [ ] Turn into a proper CLI tool
* [ ] Add search history
* [ ] Improve error handling
* [ ] Better terminal UX

## How it works?
The tool consumes the GitHub REST API and processes the JSON response to display structured data in the terminal.

---

*P.s:This project is actively being improved as part of my learning journey.*
