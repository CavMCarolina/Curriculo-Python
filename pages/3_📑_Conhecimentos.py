import streamlit as st

st.set_page_config(page_title="Conhecimentos", layout="wide", page_icon="images/icon.png")
st.logo("images/icon.png")

# Função para aplicar o css :)
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_file = "scss/style.css"
load_css(css_file)

st.sidebar.markdown("Carolina Cavalli Machado")
st.sidebar.markdown(f"""<a href="https://www.linkedin.com/in/carolinacavallimachado">Linkedin</a> • <a href="https://github.com/CavMCarolina">GitHub</a>""", unsafe_allow_html=True)

st.header("Conhecimento Em:")
st.divider()

col1, col2, col3 = st.columns([0.4, 0.2, 0.4])
col1.markdown("#### Análise de Dados:")
col1.markdown(f"""
    <ul>
        <li>Python;</li>
        <li>Estatística;</li>
    </ul>
""", unsafe_allow_html = True)
col1.write("Bibliotecas:")
col1.markdown(f"""
    <ul>
        <li>Streamlit;</li>
        <li>Numpy;</li>
        <li>Pandas;</li>
        <li>Matplotlib;</li>
        <li>Plotly;</li>
        <li>Plotnine;</li>
        <li>Scikit learning;</li>
        <li>Openpyxl;</li>
    </ul>
""", unsafe_allow_html = True)
col1.divider()

col3.markdown("#### Front-End:")
col3.markdown(f"""
    <ul>
        <li>HTML;</li>
        <li>CSS;</li>
        <li>JavaScript;</li>
        <li>React.js;</li>
    </ul>
""", unsafe_allow_html = True)
col3.write("Frameworks:")
col3.markdown(f"""
    <ul>
        <li>Tailwind;</li>
        <li>Bootstrap;</li>
        <li>SASS/SCSS;</li>
    </ul>
""", unsafe_allow_html = True)
col3.divider()


col1.markdown("#### Soft Skills:")
col1.markdown(f"""
    <ul>
        <li>Resolução de Problemas;</li>
        <li>Aprendizado Rápido;</li>
        <li>Comunicação;</li>
        <li>Trabalho em Equipe;</li>
    </ul>
""", unsafe_allow_html = True)
col1.divider()

col3.markdown("#### Outros:")
col3.markdown(f"""
    <ul>
        <li>Git/GitHub;</li>
        <li>Scrum;</li>
        <li>Modelagem de Dados;</li>
        <li>Java;</li>
        <hr class="sumir">
    </ul>
""", unsafe_allow_html = True)
