import streamlit as st
import pandas as pd
import numpy as np
 
st.set_page_config(page_title="Currículo Carolina", layout="wide")
 
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
 
# Caminho para o seu arquivo CSS
css_file = "scss/style.css"
 
# Carregar e aplicar o CSS
load_css(css_file)
 
col1, col2, col3 = st.columns([0.4, 0.1, 0.5])
col1.image("images/Foto.jpeg")
 
col3.title("Carolina Cavalli Machado")
# Colunas com informacoes
with col3:
    st.markdown(f"""
        <div class="container">
            <div class="container-item">
                <div>Butantã, Zona Oeste - SP</div>
                <div>•</div>
                <div>
                    <a href='mailto:cavm.carolina@gmail.com'>cavm.carolina@gmail.com</a>
                </div>
            </div>
            <div class="container-item">
                <div>•</div>
                <div>
                    <a href="">LinkedIn</a>
                </div>
                <div>•</div>
                <div>
                    <a href="">GitHub</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

col3.markdown("#### Engenharia de Software")
col3.write("aduahsudh")


st.markdown("## Experiência Acadêmica:")