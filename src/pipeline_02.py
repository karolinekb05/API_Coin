import requests
import pprint
import psycopg2
from datetime import datetime
import time
from typing import Dict
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
import logging

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('crypto_pipeline.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('crypto_pipeline')

load_dotenv()

# Configurações do banco de dados
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

url = "https://api.coinbase.com/v2/prices/spot"

def get_db_connection():
    """
    Cria uma conexão com o banco de dados PostgreSQL
    """
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        logger.info("Conexão com o banco de dados estabelecida com sucesso")
        return conn
    except Exception as e:
        logger.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

def create_table():
    """
    Cria a tabela se ela não existir
    """
    logger.info("Iniciando criação da tabela crypto_prices")
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS crypto_prices (
                        id SERIAL PRIMARY KEY,
                        valor DECIMAL,
                        moeda VARCHAR(10),
                        cripto VARCHAR(10),
                        data_atual TIMESTAMP
                    )
                """)
                conn.commit()
                logger.info("Tabela crypto_prices criada/verificada com sucesso")
        except Exception as e:
            logger.error(f"Erro ao criar tabela: {e}")
        finally:
            conn.close()
            logger.debug("Conexão fechada após criação/verificação da tabela")

def extract_data(url: str) -> Dict:
    """
    Extrai dados da URL fornecida
    """
    logger.info(f"Iniciando extração de dados da URL: {url}")
    response = requests.get(url)
    data = response.json()
    logger.debug(f"Dados extraídos com sucesso: {data}")
    return data

def transform_data(data: Dict) -> Dict:
    """
    Transforma os dados
    """
    logger.info("Iniciando transformação dos dados")
    valor = float(data["data"]["amount"])
    moeda = data["data"]["currency"]
    cripto = data["data"]["base"]
    data_atual = datetime.now()

    dados_transformados = {
        "valor": valor,
        "moeda": moeda,
        "cripto": cripto,
        "data_atual": data_atual
    }
    logger.debug(f"Dados transformados: {dados_transformados}")
    return dados_transformados

def load_data(dados_transformados: Dict) -> None:
    """
    Carrega os dados no PostgreSQL
    """
    logger.info("Iniciando carregamento dos dados no PostgreSQL")
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO crypto_prices (valor, moeda, cripto, data_atual)
                    VALUES (%s, %s, %s, %s)
                """, (
                    dados_transformados['valor'],
                    dados_transformados['moeda'],
                    dados_transformados['cripto'],
                    dados_transformados['data_atual']
                ))
                conn.commit()
                logger.info(f"Dados salvos com sucesso: Valor: {dados_transformados['valor']}, Moeda: {dados_transformados['moeda']}, Cripto: {dados_transformados['cripto']}")
        except Exception as e:
            logger.error(f"Erro ao inserir dados: {e}")
        finally:
            conn.close()
            logger.debug("Conexão fechada após inserção dos dados")

if __name__ == "__main__":
    logger.info("Iniciando pipeline de dados de criptomoedas")
    create_table()
    
    while True:
        try:
            data = extract_data(url)
            dados_transformados = transform_data(data)
            load_data(dados_transformados)
            logger.info("Ciclo de pipeline completado com sucesso")
            time.sleep(10)
        except Exception as e:
            logger.error(f"Erro durante a execução do pipeline: {e}")
            time.sleep(10)  # Continua tentando mesmo em caso de erro 