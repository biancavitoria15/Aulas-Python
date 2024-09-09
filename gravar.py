import requests

url = "https://tdspm---python-default-rtdb.firebaseio.com/contatos.json"

contato = {"nome": "Alberto Santos", 
           "telefone":"(11) 4444-4444",
           "email": "alberto@santos.com"}

response = requests.post(url, json=contato)
print(response)           