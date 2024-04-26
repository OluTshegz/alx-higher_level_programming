#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID
based on given credentials (username and password).
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication (personal access token
  as `password`) to access the ID info."""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth_ = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth_)
    print(r.json().get("id"))

# import sys
# import requests


# if __name__ == "__main__":
#     username = sys.argv[1]
#     password = sys.argv[2]

#     url = 'https://api.github.com/user'
#     response = requests.get(url, auth=(username, password))

#     if response.status_code == 200:
#         user_data = response.json()
#         user_id = user_data.get('id')
#         print(user_id)
#     else:
#         print(None)
