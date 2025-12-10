import requests
cep = input("Digite o cep para colsultar:  ")
if len(cep) != 8:
    print("Tamanho do cep inválido")
else:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    dados = requests.get(url)
    
    if dados.status_code == 200:
        resposta = dados.json()
        
        print(f"CEP: {resposta['cep']}")
        print(f"LOGRADOURO: {resposta['logradouro']}")
        print(f"COMPLEMENTO: {resposta['complemento']}")
        print(f"BAIRRO: {resposta['bairro']}")
        print(f"LOCALIDADE: {resposta['localidade']}")
        print(f"UF: {resposta['uf']}")