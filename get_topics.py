from github import Github

from my_token import token

g = Github(token)

repo = g.get_repo("adafruit/Adafruit_CircuitPython_Display_Text")

repo_topics = repo.get_topics()

print(repo_topics)
