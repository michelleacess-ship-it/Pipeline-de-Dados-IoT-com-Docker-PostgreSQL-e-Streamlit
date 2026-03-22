import pandas as pd
from sqlalchemy import create_engine

# conexão
engine = create_engine("postgresql://postgres:1234@localhost:5432/iot")

# caminho
file_path = "../data/temperature_readings.csv"

# leitura do dataset
df = pd.read_csv(file_path)

# visualização rápida (opcional)
print(df.head())

df.to_sql(
    "temperature_readings",
    engine,
    if_exists="replace",
    index=False
)

print("Dados inseridos com sucesso no PostgreSQL!")