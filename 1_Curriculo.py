import streamlit as st
import base64
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Currículo Carolina", layout="wide", page_icon="images/icon.png")
st.logo("images/icon.png")

# Função para aplicar o css :)
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_file = "scss/style.css"
load_css(css_file)

st.sidebar.markdown("Carolina Cavalli Machado")
st.sidebar.markdown(f"""<a href="">Linkedin</a> • <a href="">GitHub</a>""", unsafe_allow_html=True)

# Definindo colunas
col1, col2, col3 = st.columns([0.4, 0.1, 0.5])
col1.image("images/Foto.png")

col3.title("Carolina Cavalli Machado")

# Colunas com informacoes
with col3:
    # Função para pegar o logo da pasta pq por algum motivo colocar o caminho no src nao vai
    def get_base64_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    logo_github = get_base64_image("images/github.png")

    st.markdown(f"""
        <div class="container">
            <div class="linha">
                <div class="item">Zona Oeste - SP</div>
                <div class="item dot1">•</div>
                <div class="item"><a href="mailto:cavm.carolina@gmail.com">cavm.carolina@gmail.com</a></div>
                <div class="item dot2">•</div>
            </div>
            <div class="linha">
                <div class="item">
                    <a href="https://www.linkedin.com/in/carolinacavallimachado" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/2048px-LinkedIn_icon.svg.png" width="30"/>
                    </a>
                </div>
                <div class="item dot3">•</div>
                <div class="item">
                    <a href="https://github.com/CavMCarolina" target="_blank">
                        <img src="data:image/png;base64,{logo_github}" width="32"/>
                    </a>
                </div>
            </div>
    """, unsafe_allow_html=True)
    st.divider()

    st.markdown("#### Estagiária em Análise de Dados")
    st.write("Estou no segundo ano de Engenharia de Software, em busca de um estágio para aplicar meus conhecimentos em projetos reais, contribuir para o desenvolvimento da empresa e aprimorar minhas habilidades profissionais.")

st.divider()

col1, col2 = st.columns([0.7, 0.3])
col1.markdown("## Formação Acadêmica:")
col1.markdown("#### Engenharia de Software")
col1.markdown(f"""
    <div class="flex">
        <div>FIAP (Faculdade de Informática e Administração Paulista)</div>
        <div>•</div>
        <div>2023 - 2027</div>
    </div>
""", unsafe_allow_html=True)
col1.divider()

col1.markdown("## Idiomas:")
col1.markdown(f"""
    <li>Português - Nativo; Fluente</li>
    <li>Inglês - Nível B2; Intermediário</li>
""", unsafe_allow_html = True)
st.divider()