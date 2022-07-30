from urllib import response
import requests


# API çağrısına yanıt ver sakla

url='https://api.github.com/search/repositories?q=langugage:python&sort=stars'
headers= {'Accept': 'application/vnd.github.v3+json'}
r= requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# API yanıtını bir değişkende sakla.
response_dict= r.json()
print(f"Total repositories: {response_dict['total_count']}")  # python depolarının toplam sayısını temsil eden total_count u ekrana yazdırdık.

# depolar hakkındaki bilgileri incele
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")  # en üst sıralardaki depoları listelemek.
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