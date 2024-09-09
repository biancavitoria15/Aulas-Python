import requests

url = "https://tdspm---python-default-rtdb.firebaseio.com/contatos.json"
response = requests.get(url)
texto = response.text
print("response:", response)
print("Corpo:", response.text)
contatos = json.loads (texto)
print("Chaves dos contatos:")
# for chave in contatos.keys():
#     print(chave)
for contato in contatos.values():
    print(f"Nome: {contato['nome']}\tEmail: {contato['email']}")