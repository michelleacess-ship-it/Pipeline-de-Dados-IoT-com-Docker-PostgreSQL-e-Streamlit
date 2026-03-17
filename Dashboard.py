import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Conexão com o banco PostgreSQL
engine = create_engine("postgresql://postgres:1234@localhost:5432/iot")

# Função para carregar dados das views
def load_data(view_name):
    query = f"SELECT * FROM {view_name}"
    return pd.read_sql(query, engine)

# Título do dashboard
st.title("Dashboard de Temperaturas IoT")

st.header("Média de Temperatura por Dispositivo")

df_avg = load_data("avg_temp_por_dispositivo")

fig1 = px.bar(
    df_avg,
    x="device_id",
    y="avg_temp",
    labels={
        "device_id": "Dispositivo",
        "avg_temp": "Temperatura Média (°C)"
    }
)

st.plotly_chart(fig1)


st.header("Leituras por Hora do Dia")

df_hora = load_data("leituras_por_hora")

fig2 = px.line(
    df_hora,
    x="hora",
    y="contagem",
    labels={
        "hora": "Hora do Dia",
        "contagem": "Quantidade de Leituras"
    }
)

st.plotly_chart(fig2)
