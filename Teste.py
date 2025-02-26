import streamlit as st
import pandas as pd
import numpy as np
import base64
from streamlit_extras.app_style import add_css

# Carregar CSS de um arquivo externo
add_css("styles.css")

st.set_page_config(page_title="Currículo Carolina", layout="wide")

col1, col2, col3 = st.columns([0.4, 0.1, 0.5])
col1.image("images/Foto1.png")

col3.title("Carolina Cavalli Machado")

with col3:
    st.markdown("""
        <style>
            /* Container flex para as colunas */
            .container {
                display: flex;
                flex-wrap: wrap;
            }

            .item {
                align-content: center;
            }

            .linha {
                display: flex;
                justify-content: space-between;
                gap: 10px;
            }
            
            @media (max-width: 1600px) {
                .mobile {
                    display: none !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    logo_github = get_base64_image("images/github.png")

    st.markdown(f"""
        <div class="container">
            <div class="linha">
                <div class="item">Butantã, Zona Oeste - SP</div>
                <div class="item">•</div>
                <div class="item"><a href="mailto:cavm.carolina@gmail.com">cavm.carolina@gmail.com</a></div>
                <div class="item mobile">•</div>
            </div>
            <div class="linha">
                <div class="item"><a href="https://www.linkedin.com/in/carolinacavallimachado" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/2048px-LinkedIn_icon.svg.png" width="30"/></a></div>
                <div class="item">•</div>
                <div class="item">
                    <a href="https://github.com/CavMCarolina" target="_blank">
                        <img src="data:image/png;base64,{logo_github}" width="32"/>
                    </a>
                </div>
            </div>
    """, unsafe_allow_html=True)
    # st.markdown('<div class="info-container">', unsafe_allow_html=True)

    # st.markdown('<div class="info-item">Butantã, Zona Oeste - SP</div>', unsafe_allow_html=True)
    # st.markdown('<div class="info-item">•</div>', unsafe_allow_html=True)
    # st.markdown('<div class="info-item"><a href="mailto:cavm.carolina@gmail.com">cavm.carolina@gmail.com</a></div>', unsafe_allow_html=True)

    # # Bolinha que desaparece entre 641px e 1600px
    # st.markdown('<div class="info-item mobile">•</div>', unsafe_allow_html=True)

    # st.markdown('<div class="info-item"><a href="https://www.linkedin.com/in/carolinacavallimachado" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/2048px-LinkedIn_icon.svg.png" width="30"/></a></div>', unsafe_allow_html=True)
    # st.markdown('<div class="info-item">•</div>', unsafe_allow_html=True)

    # # Imagem do GitHub carregada localmente
    # def get_base64_image(image_path):
    #     with open(image_path, "rb") as img_file:
    #         return base64.b64encode(img_file.read()).decode()

    # logo_github = get_base64_image("images/github.png")

    # st.markdown(f"""
    # <div class="info-item">
    #     <a href="https://github.com/CavMCarolina" target="_blank">
    #         <img src="data:image/png;base64,{logo_github}" width="32"/>
    #     </a>
    # </div>
    # """, unsafe_allow_html=True)

    # st.markdown('</div>', unsafe_allow_html=True)  # Fecha o container
