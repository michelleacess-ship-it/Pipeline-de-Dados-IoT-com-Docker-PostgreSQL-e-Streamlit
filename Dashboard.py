import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:1234@localhost:5432/iot")

def load_data(view):
    return pd.read_sql(f"SELECT * FROM {view}", engine)

st.title("Dashboard IoT")

df_avg = load_data("avg_temp_por_dispositivo")
st.plotly_chart(px.bar(df_avg, x="device_id", y="avg_temp"))

df_hora = load_data("leituras_por_hora")
st.plotly_chart(px.line(df_hora, x="hora", y="contagem"))