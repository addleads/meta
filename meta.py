import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Configuração da página deve ser a primeira chamada
st.set_page_config(layout='wide')

# Configura o auto-refresh a cada 5 segundos (5000 milissegundos)
st_autorefresh(interval=5 * 1000, key="auto_refresh")

# URL do Google Sheets que você deseja exibir
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRz00dW2oP24--Se7nDtOs2NyOkcY-5Pi70JB36UmA885elN5_jGR9tzOeSxW6hD7Q18QRamuyKjm87/pubchart?oid=1606736902&format=interactive"

# Exibe o iframe na aplicação Streamlit
st.markdown(f'''
    <iframe src="{sheet_url}" width="100%" height="1000" frameborder="0" style="overflow:hidden;"></iframe>
''', unsafe_allow_html=True)
