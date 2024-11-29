import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Configuração da página deve ser a primeira chamada
st.set_page_config(layout='wide')

# Configura o auto-refresh a cada 5 segundos (5000 milissegundos)
st_autorefresh(interval=5 * 1000, key="auto_refresh")

# URL do iframe que você deseja exibir
iframe_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRz00dW2oP24--Se7nDtOs2NyOkcY-5Pi70JB36UmA885elN5_jGR9tzOeSxW6hD7Q18QRamuyKjm87/pubchart?oid=1606736902&format=interactive"

# Exibe o iframe na aplicação Streamlit com zoom de 80%
st.markdown(f'''
    <style>
        .iframe-container {{
            transform: scale(0.8); /* Reduz o tamanho para 80% */
            transform-origin: top left; /* Define a origem da transformação */
            width: 125%; /* Ajusta a largura para compensar o zoom */
            height: 125%; /* Ajusta a altura para compensar o zoom */
            overflow: hidden; /* Oculta qualquer conteúdo que exceda o contêiner */
        }}
    </style>
    <div class="iframe-container">
        <iframe src="{iframe_url}" width="100%" height="600" frameborder="0"></iframe>
    </div>
''', unsafe_allow_html=True)
