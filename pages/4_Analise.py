import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *

st.set_page_config(page_title="Análise Fontes Renováveis", layout="wide", page_icon="images/icon.png")
st.logo("images/icon.png")

# Função para aplicar o css :)
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_file = "scss/style.css"
load_css(css_file)

if "data" not in st.session_state:
    st.session_state["data"] = pd.read_csv("data/Global Solution.csv")

df = st.session_state["data"]

colunas_numericas = ["hidraulica", "termica", "eolica", "solar", "total"]

for coluna in colunas_numericas:
    if coluna in df.columns:
        df[coluna] = pd.to_numeric(df[coluna].astype(str).str.replace(",", "."), errors="coerce")

pages = st.sidebar.selectbox("Escolha o nível da Análise", [
    "Introdução",
    "Análise Inicial",
    "Distribuições",
    "Planilha dos Dados",
    "Dashboard Power BI"
])

# Função para exibir gráfico Plotly
def plot_distribution(x, y, title, xlabel, ylabel):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
    st.plotly_chart(fig)

if pages == "Introdução":
    st.header("Apresentação dos Dados:")
    st.write("O conjunto de dados utilizado neste estudo foi extraído do site da Operador Nacional do Sistema Elétrico (ONS) e se referem à produção semanal de energia renovável em cada uma das regiões do Brasil.")
    st.write("As fontes consideradas incluem aquelas que fazem parte da matriz sustentável do país, como hidrelétrica, eólica, térmica e solar. Os valores apresentados são expressos em megawatts médios (MWmed), uma métrica que reflete a potência média gerada ao longo do período analisado.")

    st.write(df)
    st.divider()

    st.header("Identificação das Variáveis:")
    st.markdown(f"""
        <ul>
            <li>
                <div class="flex">
                    <p class="negrito">Ano</p>
                    <p>= Representa o ano em que a produção foi registrada.</p>
                </div>
                <p class="tipo">Variável do Tipo: Discreta</p>
            </li>
            <li>
                <div class="flex">
                    <p class="negrito">Semana</p>
                    <p>= Indica a semana específica do ano em que os dados foram coletados.</p>
                </div>
                <p class="tipo">Variável do Tipo: Discreta</p>
            </li> 
            <li>
                <div class="flex">
                    <p class="negrito">Região</p>
                    <p>= Refere-se à região do Brasil onde ocorreu a produção de energia.</p>
                </div> 
                <p class="tipo">Variável do Tipo: Nominal</p>
            </li> 
            <li>
                <div class="flex">
                    <p class="negrito">Hidráulica</p>
                    <p>= Quantidade de energia gerada a partir de usinas hidrelétricas (MWmed).</p>
                </div>
                <p class="tipo">Variável do Tipo: Contínua</p>
            </li> 
            <li>
                <div class="flex">
                    <p class="negrito">Térmica</p>
                    <p>= Energia gerada por fontes térmicas renováveis (MWmed).</p>
                </div>
                <p class="tipo">Variável do Tipo: Contínua</p>
            </li>
            <li>
                <div class="flex">
                    <p class="negrito">Eólica</p>
                    <p>= Produção de energia proveniente de parques eólicos (MWmed).</p>
                </div> 
                <p class="tipo">Variável do Tipo: Contínua</p>
            </li> 
            <li>
                <div class="flex">
                    <p class="negrito">Solar</p>
                    <p>= Energia gerada por painéis solares fotovoltaicos (MWmed).</p>
                </div>
                <p class="tipo">Variável do Tipo: Contínua</p>
            </li>
            <li>
                <div class="flex">
                    <p class="negrito">Total</p>
                    <p>= Soma da produção de todas as fontes renováveis no período correspondente (MWmed).</p>
                </div> 
                <p class="tipo">Variável do Tipo: Contínua</p>
            </li>
        </ul>
    """, unsafe_allow_html=True)

    st.divider()

    st.header("Perguntas Iniciais para a Análise:")
    st.write("A análise foi feita com base nas seguintes perguntas:")
    st.markdown(f"""
        <div class="flex">
            <p class="negrito">1 - </p>
            <p>Qual fonte de energia renovável teve maior crescimento ao longo do tempo no Brasil?</p>
        </div>
        <div class="flex">
            <p class="negrito">2 - </p>
            <p>Qual fonte de energia renovável produz mais em um ano? E a que produz menos?</p>
        </div>
        <div class="flex">
            <p class="negrito">3 - </p>
            <p>Qual fonte de energia renovável tem a produção mais previsível? E a mais imprevisível?</p>
        </div>
        <div class="flex">
            <p class="negrito">4 - </p>
            <p>Existe alguma correlação visível entre as variações na produção das diferentes fontes renováveis?</p>
        </div>
    """, unsafe_allow_html=True)

elif pages == "Análise Inicial":
    # Formatacao "inversa", para nao perder o resto do código
    mapeamento_nomes = {
    "Hidráulica": "hidraulica",
    "Térmica": "termica",
    "Eólica": "eolica",
    "Solar": "solar",
    "Total": "total"
    }

    # Criando selectbox com as keys 
    opcoes_formatadas = list(mapeamento_nomes.keys())
    coluna_escolhida_formatada = st.selectbox("Escolha uma coluna numérica:", opcoes_formatadas)

    # Convertendo para o nome original antes de buscar no DataFrame
    coluna_escolhida = mapeamento_nomes[coluna_escolhida_formatada]

    if coluna_escolhida:
        st.write("Distribuição dos dados:")
        st.write(df[coluna_escolhida].describe())

    st.header("Medidas Centrais:")
    st.divider()

    st.header("Medidas de Dispersão:")
    st.divider()

    st.header("Correlação:")
    st.divider()

    st.header("Conclusão da Análise Inicial:")
    st.divider()

elif pages == "Distribuições":
    st.header("Distribuições")

    # Formatacao "inversa", para nao perder o resto do código
    mapeamento_nomes = {
    "Hidráulica": "hidraulica",
    "Térmica": "termica",
    "Eólica": "eolica",
    "Solar": "solar",
    "Total": "total"
    }

    # Criando selectbox com as keys 
    opcoes_formatadas = list(mapeamento_nomes.keys())
    coluna_escolhida_formatada = st.selectbox("Escolha uma coluna numérica:", opcoes_formatadas)

    # Convertendo para o nome original antes de buscar no DataFrame
    coluna_escolhida = mapeamento_nomes[coluna_escolhida_formatada]

    if coluna_escolhida:
        st.write("Distribuição dos dados:")
        st.write(df[coluna_escolhida].describe())
        dist = st.selectbox("Escolha a distribuição para análise:", ["Poisson", "Normal", "Binomial"])

        if dist == "Poisson":
            col1, col2 = st.columns([0.3,0.7])
            
            lambda_est = df[coluna_escolhida].mean()

            x_min = col1.number_input("Número mínimo de eventos",value=0)
            x_max = col1.number_input("Número máximo de eventos desejado",value=2*lambda_est)
            
            x = np.arange(x_min, x_max)
            y = stats.poisson.pmf(x, lambda_est)
            y_cdf = stats.poisson.cdf(x,lambda_est)

            df_poisson = pd.DataFrame({"X": x, "P(X)": y, "P(X ≤ k) (Acumulado)": np.cumsum(y),"P(X > k) (Acumulado Cauda Direita)": 1-np.cumsum(y)}).set_index("X")

            col2.write("Tabela de probabilidades:")
            col2.write(df_poisson)
            
            st.subheader(f"Estimativa de λ (Taxa média de Ocorrência): {lambda_est:.2f}")
            prob_acum = st.toggle("Probabilidade Acumulada")
            if prob_acum:
                st.write("Probabilidades 'somadas' desde a origem!")
                y_selec = y_cdf
                fig = go.Figure(data=[go.Line(x=x, y=y_selec)])
                fig.update_layout(title="Distribuição de Poisson Acumulada", xaxis_title="Número de eventos", yaxis_title="Probabilidade Acumulada")
                st.plotly_chart(fig)
            else:
                y_selec = y
                plot_distribution(x, y_selec, "Distribuição de Poisson", "Número de eventos", "Probabilidade")
                            


                            
        elif dist == "Normal":
            
            n = df[coluna_escolhida].count()
            mu_est = df[coluna_escolhida].mean()
            sigma_est = df[coluna_escolhida].std()
            st.subheader(f"Estimativa de μ: {mu_est:.2f}, σ: {sigma_est:.2f}")


            # Create distplot with custom bin_size
            #colunas_categoricas = df.select_dtypes(include=[np.character]).#columns.tolist()
            
            #st.selectbox("Escolha uma variável qualitativa",colunas_categoricas)


            hist_data = [df[coluna_escolhida].dropna().tolist()]
            group_labels=['distplot']
            b_size = st.number_input("Largura de Classe - Histograma",min_value=0.1,value=5.0)

            fig = ff.create_distplot(
                hist_data, group_labels, bin_size=b_size)
            
            teorica = st.checkbox("Curva teórica")
            if teorica:

                # Adicionando a curva da distribuição normal teórica com média e desvio padrão da amostra
                x = np.linspace(mu_est - 4*sigma_est, mu_est + 4*sigma_est, 100)
                y = stats.norm.pdf(x, mu_est, sigma_est)

                # Criando um trace da curva normal
                fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Curva Normal', line=dict(color='red')))
            
            st.plotly_chart(fig)

            p = ggplot(df, aes(sample=coluna_escolhida)) + geom_qq(size=3,colour='red',alpha=0.7) + geom_qq_line()+theme_bw()+labs(x="Quantis Teóricos",y = "Quantis Amostrais", title="Gráfico QQPlot")
            st.pyplot(ggplot.draw(p))

elif pages == "Planilha dos Dados":
    st.header("Planilha dos Dados:")
    # Carregando dados
    df = st.session_state["data"]

    # Agrupar os valores por ano, somando todas as semanas
    df_agrupado = df.groupby("ano", as_index=False).sum()

    # Mapeando os nomes para ficar bonitinho no front :)
    mapeamento_nomes = {
        "hidraulica": "Hidráulica",
        "termica": "Térmica",
        "eolica": "Eólica",
        "solar": "Solar"
    }

    # Criar lista de opções do selectbox com os nomes formatados
    fontes = ["Todas"] + [mapeamento_nomes.get(col, col.capitalize()) for col in df_agrupado.columns if col not in ["ano", "total", "semana", "regiao"]]


    df_long = df_agrupado.melt(id_vars=["ano"], var_name="Fonte Renovável", value_name="Geração (MWmed)")

    # Criar o selectbox
    fonte_selecionada = st.selectbox("Selecione a fonte de energia", fontes)

    fonte_real = [k for k, v in mapeamento_nomes.items() if v == fonte_selecionada]
    fonte_real = fonte_real[0] if fonte_real else fonte_selecionada.lower()

    # Filtrar os dados
    if fonte_selecionada == "Todas":
        df_filtered = df_long[df_long["Fonte Renovável"] == "total"]
    else:
        df_filtered = df_long[df_long["Fonte Renovável"] == fonte_real]

    # Remover a coluna "Fonte Renovável"
    df_filtered = df_filtered.drop(columns=["Fonte Renovável"])

    # Deixar bonito no front
    df_filtered = df_filtered.rename(columns={"ano": "Ano"})

    # Exibir a tabela
    st.dataframe(
        df_filtered,
        column_config={
            "Geração (MWmed)": st.column_config.ProgressColumn(
                "Geração (MWmed)", 
                format="%.2f",  # Formato com duas casas decimais
                min_value=int(df_filtered["Geração (MWmed)"].min()),  
                max_value=int(df_filtered["Geração (MWmed)"].max()),  
                width="medium"  # Ajusta a largura da barra
            )
        }
    )

    # st.write("A planilha é uma ótima forma de visualizar os dados, uma vez que deixa nítido, por meio das barras, qual fonte de energia renovável teve maior crescimento e quando.")





elif pages == "Dashboard Power BI":
    st.header("Dashboard Fontes Renováveis")


st.sidebar.divider()
st.sidebar.markdown("Carolina Cavalli Machado")
st.sidebar.markdown(f"""<a href="https://www.linkedin.com/in/carolinacavallimachado">Linkedin</a> • <a href="https://github.com/CavMCarolina">GitHub</a>""", unsafe_allow_html=True)