
import streamlit as st
from SmartCheck import smartcheck_interface
from SmartRound import smartround_interface

# Configuração de página
st.set_page_config(page_title="SmartRound", layout="wide", initial_sidebar_state="expanded")

# CSS personalizado para rodapé
st.markdown(
    '''
    <style>
    footer {
        visibility: hidden;
    }
    .css-1v0mbdj.eknhn3m4 {
        visibility: hidden;
    }
    .footer-custom {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #111111;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer-custom">
        By Sebastião Almeida
    </div>
    ''',
    unsafe_allow_html=True,
)

# Barra lateral de navegação
st.sidebar.title("SmartRound")
opcao = st.sidebar.radio("Selecione uma função:", ["SmartCheck", "SmartRound"])

# Carrega a página conforme escolha
if opcao == "SmartCheck":
    smartcheck_interface()
elif opcao == "SmartRound":
    smartround_interface()
