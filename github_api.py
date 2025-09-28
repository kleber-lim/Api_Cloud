import requests

# URL da API do GitHub para o repositório
url = "https://api.github.com/repos/kleber-lim/python-cloud-trabalho"

# Faz a requisição GET
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    print(f"Nome do repositório: {data['name']}")
    print(f"Descrição: {data['description']}")
    print(f"Estrelas: {data['stargazers_count']}")
else:
    print(f"Erro ao acessar a API: {response.status_code}")
