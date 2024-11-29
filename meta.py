import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Configuração da página deve ser a primeira chamada
st.set_page_config(layout='wide')

# Configura o auto-refresh a cada 5 segundos (5000 milissegundos)
st_autorefresh(interval=5 * 1000, key="auto_refresh")

# URL do iframe que você deseja exibir
iframe_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRz00dW2oP24--Se7nDtOs2NyOkcY-5Pi70JB36UmA885elN5_jGR9tzOeSxW6hD7Q18QRamuyKjm87/pubchart?oid=1606736902&format=interactive"

# Define a escala desejada (80%)
scale_factor = 0.8

# Calcula as novas dimensões do iframe
original_width = 2000  # Largura original em pixels (ajuste conforme necessário)
original_height = 1600   # Altura original em pixels (ajuste conforme necessário)

scaled_width = int(original_width * scale_factor)
scaled_height = int(original_height * scale_factor)

# Exibe o iframe na aplicação Streamlit com as novas dimensões
st.markdown(f'''
    <iframe src="{iframe_url}" width="{scaled_width}" height="{scaled_height}" frameborder="0"></iframe>
''', unsafe_allow_html=True)
