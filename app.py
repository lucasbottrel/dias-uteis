import streamlit as st
from datetime import datetime, timedelta
import json

def calcular_data_util(data_inicial, num_dias, holidays):
    data_atual = datetime.strptime(data_inicial.strftime("%Y-%m-%d"), "%Y-%m-%d")
    dias_uteis = 0

    while dias_uteis < num_dias:
        data_atual += timedelta(days=1)

        if data_atual.weekday() >= 5 or data_atual.strftime("%Y-%m-%d") in holidays:
            continue
        dias_uteis += 1

    return data_atual
    
def load_holidays_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        holidays = json.load(f)
    return holidays

def main():
  st.sidebar.header("🗓️ Lista de Feriados 2024")

  holidays = load_holidays_from_json("feriados2024.json")
  for holiday in holidays:
    st.sidebar.write(f"Data: {holiday['data']}: {holiday['feriado']}")

  st.header("⌚ Calculadora de Dias Úteis 2024")

  data_inicial = st.date_input("Data inicial")

  num_dias = st.number_input("Número de dias a serem somados", min_value=1)

  data_final = calcular_data_util(data_inicial, num_dias, holidays)

  st.subheader("Data Após Somar Dias Úteis")
  st.write(data_final.strftime("%d/%m/%Y"))

if __name__ == "__main__":
    main()