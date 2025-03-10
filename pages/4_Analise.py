import streamlit as st
import pandas as pd
import numpy as np

if "data" not in st.session_state:
    st.session_state["data"] = pd.read_csv("data/Global Solution.csv")

df = st.session_state["data"]

colunas_numericas = ["hidraulica", "termica", "eolica", "solar", "total"]

for coluna in colunas_numericas:
    if coluna in df.columns:
        df[coluna] = pd.to_numeric(df[coluna].astype(str).str.replace(",", "."), errors="coerce")

pages = st.sidebar.selectbox("", [
    "Introdução",
    "Análise Inicial",
    "Distribuições",
    "Planilha dos Dados",
    "Dashboard Power BI"
])

st.write(df.head())

# Função para exibir gráfico Plotly
def plot_distribution(x, y, title, xlabel, ylabel):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
    st.plotly_chart(fig)

if pages == "Introdução":
    st.header("Apresentação dos Dados:")
    st.write("Os dados são referentes a produção de cada fonte renovável (em WMed) em cada região do Brasil.... contextualizacao dos dados")
    # imagem de planilha

    st.divider()
    
    st.header("Identificação das Variáveis:")

    st.divider()
    st.header("Principais Perguntas para a Análise:")

elif pages == "Análise Inicial":
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

    colunas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
    if colunas_numericas:
        coluna_escolhida = st.selectbox("Escolha uma coluna numérica:", colunas_numericas)
        
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
    # df = st.session_state["data"]

    # tipos='Todos'
    # tipos = np.append(tipos, df["hidraulica"].unique())
    # tipo = st.sidebar.selectbox("Fonte Renovável", tipos)

    # if tipo == 'Todos':
    #     df_filtered = df
    # else:
    #     df_filtered = df[(df["Fonte"]==tipo)]

    df = st.session_state["data"]

    df_agrupado = df.groupby("ano", as_index=False).sum()
    fontes = ["Todas"] 
        
    fontes += [col for col in df.columns if col not in ["ano", "semana", "regiao"]]
    
    df_long = df.melt(id_vars=["ano"], var_name="Fonte Renovável", value_name="Geração (MW)")

    fonte_selecionada = st.sidebar.selectbox("Selecione a fonte de energia", fontes)

    if fonte_selecionada == "Todas":
        df_filtered = df_long
    else:
        df_filtered = df_long[df_long["Fonte Renovável"] == fonte_selecionada]

    st.dataframe(
        df_filtered,
        column_config={
            "Geração (MW)": st.column_config.ProgressColumn(
                "Geração (MW)", format="%f", min_value=0, max_value=int(df_filtered["Geração (MW)"].max())
            )
        }
    )




elif pages == "Dashboard Power BI":
    st.header("Dashboard Fontes Renováveis")