import requests

response = requests.get("https://gitlab.com/api/v4/users/pblgllgs/projects")

my_projects = response.json()

for project in my_projects:
    print(f"Project name: {project['name']}, URL: {project['http_url_to_repo']}")

