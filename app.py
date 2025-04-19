import pandas as pd
import numpy as np
import streamlit as st
import joblib
from sklearn.preprocessing import LabelEncoder

st.set_page_config(
     page_title="Previsão de diabetes",
     page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpV47Ex87eKgJKz83f_A74cPCGJeO01ul29g&s",
     layout="wide",
)

modelo_diabetes = joblib.load(r"C:\Users\Victor Hugo\Downloads\archive\regressao_diabetes.joblib")

st.title('🧠 Modelo Preditivo para Diagnóstico de Diabetes')

genero = st.selectbox(
    "Qual seu gênero?:",
    ["Feminino", "Masculino", "Outros"]
)

st.write(f"Você escolheu: {genero}")

idade = st.number_input("Quantos anos você tem?", min_value=0, max_value=120, step=1)

st.write(f"Você informou que tem {int(idade)} anos.")

hipertensao = st.selectbox(
    "Você tem hipertensão (Pressão alta)??:",
    ["Yes", "No"]
)
st.write(f"Você escolheu: {hipertensao}")

doenca_car = st.selectbox(
    "Você tem alguma doença cardiovascular?:",
    ["Yes", "No"]
)
st.write(f"Você escolheu: {doenca_car}")

fumo = st.selectbox(
    "Qual é a frequência de uso de cigarro?",
    ["Nunca fumei", "Parei de fumar", "Fumo normalmente", "Parei recentemente", "Fumo com alta frequência", 'Preciso não optar (pode interferir na previsão)']
)
st.write(f"Você escolheu: {fumo}")

peso = st.number_input("Quantos Quilosgramas (KG) você tem?", min_value=30.0, step=0.1)

st.write(f"Você informou que tem {float(peso)} Quilos.")

altura = st.number_input("Qual é sua altura em metros?", min_value=1.10, step=0.01)

st.write(f"Você informou que tem {float(altura)} de altura.")

IMC = peso/(altura ** 2)

st.markdown(f"<h3>Você tem {float(IMC):.2f} de IMC.</h3>", unsafe_allow_html=True)

if IMC < 16:
    st.write("Você está no grau de Magreza GRAVE!")
elif IMC > 16 and IMC < 17:
    st.write("Você está no grau de Magreza MODERADA! Mais cuidado!")
elif IMC > 17 and IMC < 18.5:
    st.write("Você está no grau de Magreza LEVE! Cuidado!")
elif IMC > 18.5 and IMC < 25:
    st.write("Você está no grau de SAUDÁVEL! Mantenha assim!")
elif IMC > 25 and IMC < 30:
    st.write("Você está no grau de SOBREPESO! Cuidado!")
elif IMC > 30 and IMC < 35:
    st.write("Você está no grau de OBESIDADE GRAU I! Muito Cuidado!")
elif IMC > 35 and IMC < 40:
    st.write("Você está no grau de OBESIDADE GRAU II! BASTANTE CUIDADO!")
elif IMC > 40:
    st.write("Você está no grau de OBESIDADE GRAU III!")

hemoglobina = st.number_input("Qual o seu nivel de hba1c (Hemoglobina glicada)? ", min_value=0.0, step=0.01)
st.write(f"Você informou que tem {float(hemoglobina)}% de Hemoglobina glicada.")

glicose = st.number_input("Qual o seu nivel de glicose?", min_value=0.0, step=0.01)
st.write(f"Você informou que tem {float(glicose)} de glicose.")

if hipertensao == "Yes":
    hipertensao_num = 1
else:
    hipertensao_num = 0

if genero == 'Masculino':
    genero_num = 1
elif genero == 'Feminino':
    genero_num = 0
else:
    genero_num = 2

if fumo == 'Nunca fumei':
    fumo_num = 4
elif fumo == 'Parei de fumar':
    fumo_num = 3
elif fumo == 'Fumo normalmente':
    fumo_num = 1
elif fumo == 'Parei recentemente':
    fumo_num = 5
elif fumo == 'Fumo com alta frequência':
    fumo_num = 2
else:
    fumo_num = 0

if doenca_car == 'Yes':
    doenca_car_num = 1  
else:
    doenca_car_num = 0

if st.button("Fazer previsão"):
    entrada = np.array([[genero_num, idade, hipertensao_num, doenca_car_num, fumo_num, IMC, hemoglobina, glicose]])
    previsao = modelo_diabetes.predict(entrada)
    
    if previsao[0] == 0:
        st.success("✅ O modelo prevê que a pessoa **NÃO TEM diabetes**.")
    else:
        st.error("🚨 O modelo prevê que a pessoa **TEM diabetes**.")

    
