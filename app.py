import streamlit as st
from SmartCheck import smartcheck_interface
from SmartRound import smartround_interface

# Configuração de página
st.set_page_config(page_title='SmartRound', layout='centered')

st.sidebar.title('SmartRound')
option = st.sidebar.selectbox('Escolha uma função:', ['SmartCheck', 'SmartRound'])

if option == 'SmartCheck':
    smartcheck_interface()
elif option == 'SmartRound':
    smartround_interface()
