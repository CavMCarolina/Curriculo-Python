import streamlit as st
import pandas as pd
import numpy as np
import os
 
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
                <div>•</div>
            </div>
            <div>
                <div></div>
                <div></div>
                <div></div>
                <div></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
 
    # col3_1, col3_2, col3_3, col3_4, col3_5, col3_6, col3_7 = st.columns([2, 0.1, 2, 0.1, 0.7, 0.1, 0.7])
   
    # # Usando css para estilizar mais as coisinhas do streamlit :)
    # with col3_1:
    #     st.markdown("<div style='text-align: center;'>Butantã, Zona Oeste - SP</div>", unsafe_allow_html=True)
    # with col3_2:
    #     st.write("|")
    # with col3_3:
    #     st.markdown("<div style='text-align: center;'><a href='mailto:cavm.carolina@gmail.com'>cavm.carolina@gmail.com</a></div>", unsafe_allow_html=True)
    # with col3_4:
    #     st.write("|")  
    # with col3_5:
    #     st.markdown("""
    #     <a href="https://www.linkedin.com/in/carolinacavallimachado" target="_blank" style="display: block; text-align: center;">
    #         <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/2048px-LinkedIn_icon.svg.png" width="30" style="margin-right: 10px;" />
    #     </a>
    # """, unsafe_allow_html=True)
    # with col3_6:
    #     st.write("|")
    # with col3_7:
    #     st.markdown("""
    #     <a href="https://github.com/CavMCarolina" target="_blank" style="display: block; text-align: center;">
    #         <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="30" />
    #     </a>
    # """, unsafe_allow_html=True)
       
col3.markdown("<hr style='margin: 5px 0;'>", unsafe_allow_html=True)
col3.markdown("#### Engenharia de Software")
col3.write("aduahsudh")