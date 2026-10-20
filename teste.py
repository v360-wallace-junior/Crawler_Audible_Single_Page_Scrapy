import requests

url = "https://www.audible.com.br/search"

session = requests.Session()

home = session.get(
    "https://www.audible.com.br/",
    timeout=20,
)

print("Home:", home.status_code)

search = session.get(
    url,
    timeout=20,
)

print("Pesquisa:", search.status_code)
print("Tipo de conteúdo:", search.headers.get("Content-Type"))
print("Título da resposta:", search.text[:300])

print("\nCabeçalhos enviados pelo requests:")
for nome, valor in search.request.headers.items():
    print(f"{nome}: {valor}")