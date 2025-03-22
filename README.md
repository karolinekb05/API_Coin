# 🪙 API Coin - ETL de Dados Bitcoin

## 📝 Descrição
Este projeto implementa um pipeline ETL (Extract, Transform, Load) para coletar, processar e armazenar dados históricos e em tempo real do Bitcoin utilizando APIs públicas de criptomoedas.

## 🚀 Funcionalidades
- Extração de dados históricos do preço do Bitcoin
- Coleta em tempo real de dados de mercado
- Transformação e limpeza dos dados
- Armazenamento em banco de dados
- Análises básicas e visualizações

## 🛠️ Tecnologias Utilizadas
- Python 3.8+
- Pandas para manipulação de dados
- Requests para chamadas de API
- SQLAlchemy para persistência de dados
- Plotly para visualizações

## ⚙️ Configuração do Ambiente

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/karolinekb05/API_Coin.git
cd api_coin
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🔧 Configuração
1. Configure as variáveis de ambiente necessárias:
```
API_KEY=sua_chave_api
DATABASE_URL=sua_url_banco
```
