#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

# import requests
# import sys

# if __name__ == "__main__":
#     repository_name = sys.argv[1]
#     owner_name = sys.argv[2]

#     url = f'https://api.github.com/repos/{owner_name}/{repository_name}'
#     response = requests.get(url)

#     if response.status_code == 200:
#         repository_data = response.json()
#         try:
#             for i in range(10):
#                 print("{}: {}".format(
#                     commits[i].get("sha"),
#                     commits[i].get("commit").get("author").get("name")))
#         except IndexError:
#             pass
#     else:
#         print("Error:", response.status_code)
