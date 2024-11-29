import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Configura o auto-refresh a cada 5 segundos (5000 milissegundos)
st_autorefresh(interval=5 * 1000, key="auto_refresh")

# URL do iframe que você deseja exibir
iframe_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRz00dW2oP24--Se7nDtOs2NyOkcY-5Pi70JB36UmA885elN5_jGR9tzOeSxW6hD7Q18QRamuyKjm87/pubchart?oid=1606736902&format=interactive"

# Exibe o iframe na aplicação Streamlit
st.markdown(f'<iframe src="{iframe_url}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)
