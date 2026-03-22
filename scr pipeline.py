import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:1234@localhost:5432/iot")

df = pd.read_csv("../data/temperature_readings.csv")

df.to_sql("temperature_readings", engine, if_exists="replace", index=False)

print("Dados inseridos!")