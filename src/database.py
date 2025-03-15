from sqlalchemy import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

# Cria a classe base para as tabelas
Base = declarative_base()

# Cria a classe para a tabela crypto_prices
class Crypto(Base):
    __tablename__ = "crypto_prices"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cripto = Column(String(50), nullable=False)
    valor = Column(Float, nullable=False)
    moeda = Column(String(10), nullable=False)
    data_atual = Column(DateTime, default=datetime.now)
