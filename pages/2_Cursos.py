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

col1, col2 = st.columns([0.4, 0.7])
col1.markdown("#### Data Visualization")
col1.write("FIAP • Em Andamento...")
col1.divider()

col1.markdown("#### Python")
col1.write("FIAP • 2025")
col1.divider()

col1.markdown("#### Power BI Básico")
col1.write("Tetra Educação • 2025")
col1.divider()

col1.markdown("#### Gestão de Infraestrutura de TI")
col1.write("FIAP • 2024")
col1.divider()

col1.markdown("#### Formação Social e Sustentabilidade")
col1.write("FIAP • 2024")
col1.divider()

col1.markdown("#### Design Thinking - Process")
col1.write("FIAP • 2023")
col1.divider()

col1.markdown("#### Microsoft Excel Avançado")
col1.write("Fundação Bradesco • 2023")
st.divider()