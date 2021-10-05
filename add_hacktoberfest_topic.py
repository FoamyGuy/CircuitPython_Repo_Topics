from github import Github

from my_token import token

g = Github(token)

repo = g.get_repo("adafruit/Adafruit_CircuitPython_Display_Text")
#repo = g.get_repo("FoamyGuy/missing_type_issue_maker")


print(repo.url)
repo_topics = repo.get_topics()
print("before")
print(repo_topics)
if "hacktoberfest" not in repo_topics:
    repo_topics.append("hacktoberfest")
    repo.replace_topics(repo_topics)
    print("after")
    print(repo.get_topics())
