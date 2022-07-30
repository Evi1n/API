from urllib import response
import requests


# Respond and store API call
url='https://api.github.com/search/repositories?q=langugage:python&sort=stars'
headers= {'Accept': 'application/vnd.github.v3+json'}
r= requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store the API response in a variable.
response_dict= r.json()
print(f"Total repositories: {response_dict['total_count']}")  # python depolarının toplam sayısını temsil eden total_count u ekrana yazdırdık.

# view information about repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")  # listing top-ranked repositories
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"STars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
    

# ilk depoyu incele
# repo_dict = repo_dicts[0]

print(f"\nKeys: {len(repo_dict)}")
#for key in sorted(repo_dict.keys()):
 #   print(key)

# Sonuçları işle
# print(response_dict.keys())