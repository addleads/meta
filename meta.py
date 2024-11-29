import streamlit as st

# URL do iframe que você deseja exibir
iframe_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRz00dW2oP24--Se7nDtOs2NyOkcY-5Pi70JB36UmA885elN5_jGR9tzOeSxW6hD7Q18QRamuyKjm87/pubchart?oid=1606736902&format=interactive"

# Define o estilo do iframe para ocupar toda a tela
st.markdown(
    f"""
    <style>
        .iframe-container {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }}
    </style>
    <div class="iframe-container">
        <iframe src="{iframe_url}" width="100%" height="100%" frameborder="0"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# Adiciona um auto-refresh a cada 5 segundos
st.experimental_rerun()

