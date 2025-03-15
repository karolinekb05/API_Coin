import requests
import pprint
from tinydb import TinyDB
from datetime import datetime, time

url = "https://api.coinbase.com/v2/prices/spot"

def extract_data(url: str) -> dict:
    """
    Extract data from the given URL
    """
    response = requests.get(url)
    data = response.json()
    return data

data = extract_data(url)
pprint.pprint(data["data"])

def transform_data(data: dict) -> dict:
    """
    Transform the data
    """
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    valor = data["data"]["amount"]
    moeda = data["data"]["currency"]
    cripto = data["data"]["base"]
    data_atual = datetime.now().timestamp()

    dados_transformados = {
        "valor": valor,
        "moeda": moeda,
        "cripto": cripto,
        "data_atual": data_atual
    }
    return dados_transformados

dados_transformados = transform_data(data)
print(dados_transformados)

def load_data(dados_transformados: dict) -> None:
    """
    Load the data
    """
    print(f"Valor: {dados_transformados['valor']}, Moeda: {dados_transformados['moeda']}, Cripto: {dados_transformados['cripto']}")

    # Cria ou abre o banco de dados
    db = TinyDB('dados_cripto.json')
    
    # Insere os dados transformados no banco
    db.insert(dados_transformados)
    
    
    
    # Imprime mensagem de confirmação
    print("Dados salvos com sucesso no banco TinyDB")

load_data(dados_transformados)

if __name__ == "__main__":
    while True:
        data = extract_data(url)
        dados_transformados = transform_data(data)
        load_data(dados_transformados)
        time.sleep(10)
