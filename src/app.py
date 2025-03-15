import streamlit as st
import json
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Monitoramento de Criptomoedas",
    page_icon="📈",
    layout="wide"
)

# Título do aplicativo
st.title("📊 Dashboard de Criptomoedas")

# Carregar dados do arquivo JSON
def carregar_dados():
    with open('dados_cripto.json', 'r') as file:
        data = json.load(file)
        # Converter dados para formato de lista
        records = []
        for key, value in data['_default'].items():
            records.append(value)
        return pd.DataFrame(records)

# Carregar dados em um DataFrame
df = carregar_dados()

# Converter timestamp para datetime se existir
if 'data_atual' in df.columns:
    df['data_atual'] = pd.to_datetime(df['data_atual'], unit='s')

# Métricas principais
col1, col2, col3 = st.columns(3)

with col1:
    ultimo_valor = float(df['valor'].iloc[-1])
    st.metric(
        label="Último Valor",
        value=f"${ultimo_valor:,.2f}",
        delta=f"{float(df['valor'].iloc[-1]) - float(df['valor'].iloc[-2]):,.2f}"
    )

with col2:
    st.metric(
        label="Moeda",
        value=df['moeda'].iloc[-1]
    )

with col3:
    st.metric(
        label="Criptomoeda",
        value=df['cripto'].iloc[-1]
    )

# Gráfico de linha
st.subheader("Histórico de Preços")
fig_data = pd.DataFrame({
    'Valor': df['valor'].astype(float)
})

st.line_chart(fig_data)

# Tabela de dados
st.subheader("Dados Detalhados")
st.dataframe(df.style.format({'valor': '${:,.2f}'})) 