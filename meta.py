import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Configuração da página deve ser a primeira chamada
st.set_page_config(layout='wide')

# Configura o auto-refresh a cada 5 segundos (5000 milissegundos)
st_autorefresh(interval=5 * 1000, key="auto_refresh")

# URL do iframe que você deseja exibir
iframe_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRz00dW2oP24--Se7nDtOs2NyOkcY-5Pi70JB36UmA885elN5_jGR9tzOeSxW6hD7Q18QRamuyKjm87/pubchart?oid=1606736902&format=interactive"

# HTML e JavaScript para aumentar o zoom do iframe
st.markdown(f'''
    <div style="position: relative; width: 100%; height: 600px; overflow: hidden;">
        <iframe id="myIframe" src="{iframe_url}" width="100%" height="100%" frameborder="0"></iframe>
    </div>
    <button onclick="zoomIn()">Aumentar Zoom</button>
    <script>
        function zoomIn() {{
            var iframe = document.getElementById('myIframe');
            for (var i = 0; i < 5; i++) {{
                iframe.style.transform = 'scale(' + (1 + (i * 0.1)) + ')';
                iframe.style.transformOrigin = 'top left';
            }}
        }}
    </script>
''', unsafe_allow_html=True)
