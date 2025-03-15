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
- Docker para containerização

## ⚙️ Configuração do Ambiente

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Docker (opcional)

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
1. Copie o arquivo `.env.example` para `.env`
2. Configure as variáveis de ambiente necessárias:
```
API_KEY=sua_chave_api
DATABASE_URL=sua_url_banco
```

## 📊 Uso
1. Execute a extração de dados históricos:
```bash
python src/extract_historical.py
```

2. Inicie o monitoramento em tempo real:
```bash
python src/realtime_monitor.py
```

## 📁 Estrutura do Projeto
```
api-coin/
├── src/
│   ├── extract/
│   ├── transform/
│   └── load/
├── tests/
├── data/
├── notebooks/
├── requirements.txt
└── README.md
```

## 📈 Exemplos de Análises
- Análise de tendências de preço
- Indicadores técnicos
- Volatilidade do mercado
- Volume de negociação

## 🤝 Contribuição
1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙏 Agradecimentos
- [CoinGecko API](https://www.coingecko.com/en/api) - Dados de mercado
- [Binance API](https://binance-docs.github.io/apidocs/) - Dados em tempo real