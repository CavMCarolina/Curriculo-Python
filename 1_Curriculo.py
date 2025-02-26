import streamlit as st
import pandas as pd
import numpy as np
import base64

st.set_page_config(page_title="Currículo Carolina", layout="wide")

col1, col2, col3 = st.columns([0.4, 0.1, 0.5])
col1.image("images/Foto.png")

col3.title("Carolina Cavalli Machado")
# Colunas com informacoes
with col3:
    col3_1, col3_2, col3_3, col3_4, col3_5, col3_6, col3_7 = st.columns([2, 0.1, 2, 0.1, 1, 0.1, 1])
    
    # Usando css para estilizar mais as coisinhas do streamlit :)
    with col3_1:
        st.markdown("<div style='text-align: center;'>Butantã, Zona Oeste - SP</div>", unsafe_allow_html=True)
    with col3_2:
        st.markdown("<div style='text-align: center;'>•</div>", unsafe_allow_html=True) 
    with col3_3:
        st.markdown("<div style='text-align: center;'><a href='mailto:cavm.carolina@gmail.com'>cavm.carolina@gmail.com</a></div>", unsafe_allow_html=True)
    with col3_4:
        st.markdown("""
        <style>
            @media (min-width: 641px) and (max-width: 1600px) {
                .mobile {
                    display: none !important;
                }
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<div class='mobile' style='text-align: center;'>•</div>", unsafe_allow_html=True)  
    with col3_5:
        st.markdown("""
        <a href="https://www.linkedin.com/in/carolinacavallimachado" target="_blank" style="display: block; text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/2048px-LinkedIn_icon.svg.png" width="30"/>
        </a>
    """, unsafe_allow_html=True)
    with col3_6:
        st.markdown("<div style='text-align: center;'>•</div>", unsafe_allow_html=True) 
    with col3_7:
        # Função para pegar o logo da pasta pq por algum motivo colocar o url no src nao vai 
        def get_base64_image(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()

        logo_github = get_base64_image("images/github.png")

        st.markdown(f"""
        <a href="https://github.com/CavMCarolina" target="_blank" style="display: block; text-align: center;">
            <img src="data:image/png;base64,{logo_github}" width="32"/>
        </a>
    """, unsafe_allow_html=True)
       
col3.markdown("<hr style='margin: 5px 2px;'>", unsafe_allow_html=True)
col3.markdown("#### Engenharia de Software")
col3.write("aduahsudh")