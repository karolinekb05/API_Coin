import streamlit as st
import json
import pandas as pd
import plotly.graph_objects as go
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

# Converter valor para float e timestamp para datetime
df['valor'] = df['valor'].astype(float)
if 'data_atual' in df.columns:
    df['data_atual'] = pd.to_datetime(df['data_atual'], unit='s')

# Métricas principais
col1, col2, col3 = st.columns(3)

with col1:
    ultimo_valor = df['valor'].iloc[-1]
    st.metric(
        label="Último Valor",
        value=f"${ultimo_valor:,.2f}",
        delta=f"{df['valor'].iloc[-1] - df['valor'].iloc[-2]:,.2f}"
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

# Gráfico de linha com Plotly
st.subheader("Histórico de Preços")

# Criar figura do Plotly
fig = go.Figure()

# Adicionar linha
fig.add_trace(
    go.Scatter(
        x=df.index if 'data_atual' not in df.columns else df['data_atual'],
        y=df['valor'],
        mode='lines+markers',
        name='Valor BTC',
        hovertemplate='<b>Valor:</b> $%{y:,.2f}<extra></extra>'
    )
)

# Configurar layout
fig.update_layout(
    yaxis=dict(
        title='Valor em USD',
        tickformat='$,.2f',
        gridcolor='rgba(211,211,211,0.3)',
    ),
    xaxis=dict(
        title='Tempo',
        gridcolor='rgba(211,211,211,0.3)',
    ),
    plot_bgcolor='white',
    hovermode='x unified',
    showlegend=False,
    height=500
)

# Exibir gráfico
st.plotly_chart(fig, use_container_width=True)

# Estatísticas adicionais
st.subheader("Estatísticas")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Valor Máximo",
        f"${df['valor'].max():,.2f}"
    )

with col2:
    st.metric(
        "Valor Mínimo",
        f"${df['valor'].min():,.2f}"
    )

with col3:
    st.metric(
        "Média",
        f"${df['valor'].mean():,.2f}"
    )

with col4:
    st.metric(
        "Variação Total",
        f"${df['valor'].max() - df['valor'].min():,.2f}"
    )

# Tabela de dados
st.subheader("Dados Detalhados")
df_display = df.copy()
df_display['valor'] = df_display['valor'].apply(lambda x: f'${x:,.2f}')
st.dataframe(df_display, use_container_width=True) 