import streamlit as st

st.set_page_config(page_title="Cursos", layout="wide", page_icon="images/icon.png")
st.logo("images/icon.png")

# Função para aplicar o css :)
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_file = "scss/style.css"
load_css(css_file)

st.header("Cursos Complementares:")
st.divider()
st.markdown("#### Power BI Básico")