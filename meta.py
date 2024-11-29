import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Attempt to import pyautogui
try:
    import pyautogui
    import time
    import threading
except ImportError as e:
    st.error("PyAutoGUI could not be imported. This functionality may not work in this environment.")
    pyautogui = None  # Set to None or handle accordingly

# Function to simulate keypresses
def simulate_keypress():
    if pyautogui is not None:
        time.sleep(5)  # Wait for 5 seconds after loading the page
        for _ in range(5):
            pyautogui.hotkey('ctrl', '+')  # Simulate Ctrl + +
            time.sleep(0.1)  # Short pause between presses

# Start thread for keypress simulation if pyautogui is available
if pyautogui is not None:
    threading.Thread(target=simulate_keypress, daemon=True).start()

# Streamlit application setup
st.set_page_config(layout='wide')
st_autorefresh(interval=5 * 1000, key="auto_refresh")

# URL of Google Sheets to display
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRz00dW2oP24--Se7nDtOs2NyOkcY-5Pi70JB36UmA885elN5_jGR9tzOeSxW6hD7Q18QRamuyKjm87/pubchart?oid=1606736902&format=interactive"

# Display iframe in Streamlit app
st.markdown(f'''
    <iframe src="{sheet_url}" width="100%" height="1000" frameborder="0" style="overflow:hidden;"></iframe>
''', unsafe_allow_html=True)
