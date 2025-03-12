import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *

# Configurações da Página
st.set_page_config(page_title="Análise Fontes Renováveis", layout="wide", page_icon="images/icon.png")
st.logo("images/icon.png")

# Função para aplicar o css :)
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_file = "scss/style.css"
load_css(css_file)

# Deixar o arquivo na memória
if "data" not in st.session_state:
    st.session_state["data"] = pd.read_csv("data/Global Solution.csv")

df = st.session_state["data"]

# Transformando tudo em numerico pra nao ter erro
colunas_numericas = ["hidraulica", "termica", "eolica", "solar", "total"]
for coluna in colunas_numericas:
    if coluna in df.columns:
        df[coluna] = pd.to_numeric(df[coluna].astype(str).str.replace(",", "."), errors="coerce")

# Páginas dentro da Análise
pages = st.sidebar.selectbox("Escolha o nível da Análise", [
    "Introdução",
    "Análise Inicial",
    "Distribuições",
    "Planilha dos Dados"
])

# Introdução
if pages == "Introdução":
    # Função para deixar o df bonito
    def formatar_df(df):
        """Formata apenas as colunas numéricas para 2 casas decimais, 
        troca pontos por vírgulas e adiciona separador de milhar.
        Mantém colunas 'ano' e 'semana' sem formatação."""
    
        df_formatado = df.copy()  # Copia o DataFrame original
        
        for coluna in df_formatado.select_dtypes(include=['float64', 'int64']):
            if coluna in ['ano', 'semana']:  
                df_formatado[coluna] = df_formatado[coluna].astype(str)  # Mantém como string sem formatação
            else:
                df_formatado[coluna] = df_formatado[coluna].apply(
                    lambda x: "{:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", ".")
                )
        
        return df_formatado

    # Apresentação dos Dados
    st.header("Apresentação dos Dados:")
    st.write("Os dados utilizados neste estudo foram extraídos do site da Operador Nacional do Sistema Elétrico (ONS) e se referem à produção semanal de energia renovável em cada uma das regiões do Brasil.")
    st.write("As fontes consideradas incluem aquelas que fazem parte da matriz sustentável do país, como hidrelétrica, eólica, térmica e solar. Os valores apresentados são expressos em megawatts médios (MWmed), uma métrica que reflete a potência média gerada ao longo do período analisado.")
   
    # Aplicando a estilizacao
    df_estilizado = formatar_df(df)
    # Exibindo o df
    st.dataframe(df_estilizado, use_container_width=True)

    st.divider()

    # Identificação das Variáveis
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

    # Perguntas
    st.header("Perguntas Iniciais para a Análise:")
    st.write("A análise foi feita com base nas seguintes perguntas:")
    st.markdown(f"""
        <div class="flex">
            <p class="negrito">1 - </p>
            <p>Qual fonte de energia renovável teve maior crescimento ao longo do tempo no Brasil?</p>
        </div>
        <div class="flex">
            <p class="negrito">2 - </p>
            <p>Qual fonte de energia renovável produz mais em um ano?</p>
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

# Página da Análise Inicial
elif pages == "Análise Inicial":
    # Definição das fontes renováveis
    fontes_renovaveis = ["hidraulica", "termica", "eolica", "solar"]

    # Funcao para deixar as tabelas bonitas
    def formatar_tabela(tabela):
        """Formata os valores para 2 casas decimais, troca pontos por vírgulas e adiciona separador de milhar corretamente."""
        return tabela.applymap(lambda x: "{:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", "."))

    # funcoes dos calculos
    def calcular_medidas_centrais(df):
        """Calcula média, mediana e moda."""
        return pd.DataFrame({
            "Média": df[fontes_renovaveis].mean(),
            "Mediana": df[fontes_renovaveis].median(),
            "Moda": df[fontes_renovaveis].mode().iloc[0]  # Pegando a primeira moda caso existam múltiplas
        })

    def calcular_desvio_medio(df):
        """Calcula o desvio médio manualmente de forma correta."""
        medias = df[fontes_renovaveis].mean()  # Calcula a média de cada coluna
        return df[fontes_renovaveis].apply(lambda x: (abs(x - medias[x.name])).mean())  # Desvio médio correto

    def calcular_medidas_dispersao(df):
        """Calcula desvio padrão, amplitude, coeficiente de variação, desvio médio e variância."""
        return pd.DataFrame({
            "Desvio Padrão": df[fontes_renovaveis].std(),
            "Mínimo": df[fontes_renovaveis].min(),
            "Máximo": df[fontes_renovaveis].max(),
            "Amplitude": df[fontes_renovaveis].max() - df[fontes_renovaveis].min(),
            "Coef. de Variação (%)": (df[fontes_renovaveis].std() / df[fontes_renovaveis].mean()) * 100,
            "Q1": df[fontes_renovaveis].quantile(0.25),
            "Q3": df[fontes_renovaveis].quantile(0.75),   
            "Desvio Médio": calcular_desvio_medio(df),
        })

    # Criando tabelas
    medidas_centrais = calcular_medidas_centrais(df)
    medidas_dispersao = calcular_medidas_dispersao(df)

    # Formatando os valores
    medidas_centrais = formatar_tabela(medidas_centrais)
    medidas_dispersao = formatar_tabela(medidas_dispersao)

    # Renomear para o Front
    medidas_centrais.index = ["Hidráulica", "Térmica", "Eólica", "Solar"]
    medidas_dispersao.index = ["Hidráulica", "Térmica", "Eólica", "Solar"]

    # Medidas Centrais
    st.header("Medidas Centrais:")
    st.table(medidas_centrais)
    st.markdown(f"""
        <h4>Hidráulica:</h4>
        <p>Apresenta a maior média, mediana e moda, o que indica que é a fonte de energia com maior produção constante ao longo do período analisado.</p>
        <h4>Térmica:</h4>
        <p>Possui a segunda maior média e mediana, sugerindo que pode ser a segunda fonte mais utilizada.</p>
        <h4>Eólica:</h4>
        <p>Apresenta uma média de 2301 MWmed e mediana de apenas 363 MWmed, o que mostra que sua produção ainda não era tão significativa no período, mas tinha potencial de crescimento. Além disso, sua moda é 0 MWmed, indicando que em muitos momentos a produção foi nula, o que pode significar que estava em fase de implantação.</p>
        <h4>Solar:</h4>
        <p>Tem os menores valores de média e mediana, além da moda ser 0 MWmed, reforçando a ideia de que sua participação na matriz energética era ainda pequena e possivelmente em crescimento inicial.</p>
    """, unsafe_allow_html=True)

    st.divider()

    # Medidas de Dispersão
    st.header("Medidas de Dispersão:")
    st.table(medidas_dispersao)
    st.markdown(f"""
        <h4>Hidráulica:</h4>
        <p>Apresenta o menor coeficiente de variação, o que indica que sua produção é a mais estável. Além disso, tem os maiores valores de mínimo, máximo, Q1 e Q3, confirmando que é a fonte com menor oscilação ao longo do tempo.</p>
        <h4>Térmica:</h4>
        <p>Seu coeficiente de variação é de 94%, mostrando mais variação do que a hidráulica, mas ainda com certa estabilidade em comparação às fontes renováveis mais recentes. Sua amplitude indica uma variação significativa na produção.</p>
        <h4>Eólica:</h4>
        <p>Apresenta um coeficiente de variação muito alto, além de um desvio padrão elevado, o que mostra grande oscilação na produção. O fato de o Q1 ser apenas 18 MWmed reforça que sua produção foi baixa em boa parte do tempo, mas seu máximo ser 16038 MWmed indica um grande crescimento em determinados momentos.</p>
        <h4>Solar:</h4>
        <p>É a fonte com maior coeficiente de variação, o que indica a maior oscilação entre todas. Seu desvio padrão é proporcionalmente alto em relação à média, e seu Q1 sendo 0 MWmed mostra que em muitos momentos não havia geração significativa de energia solar. Isso reforça a ideia de que essa fonte estava em forte crescimento, mas ainda com produção instável. Dessa forma, se tornando a fonte renovável mais imprevisível.</p>
    """, unsafe_allow_html=True)

    # CSS para centralizar os textos
    st.markdown(
        """
        <style>
            table {
                width: 100%;
            }
            th, td {
                text-align: center !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Correlação
    # Configuracoes Grafico 1
    df_long = pd.melt(df, id_vars=['regiao', 'ano', 'semana'],
                    value_vars=['hidraulica', 'termica', 'eolica', 'solar'],
                    var_name='energia', value_name='valor')

    # Corrigindo tipos de dados
    df_long['ano'] = pd.to_numeric(df_long['ano'], errors='coerce')
    df_long['semana'] = pd.to_numeric(df_long['semana'], errors='coerce')

    # Criando a coluna 'data' no formato de data
    df_long['data'] = pd.to_datetime(df_long['ano'].astype(str) + '-' + df_long['semana'].astype(str) + '-1', format='%Y-%W-%w', errors='coerce')

    df_long = df_long.sort_values('data')

    # Agrupando os dados
    df_total_energy = df_long.groupby(['data', 'energia'])['valor'].sum().reset_index()

    # Criando a figura interativa
    fig1 = go.Figure()

    # Adicionando cada fonte de energia ao gráfico
    for energy_source in df_total_energy['energia'].unique():
        subset = df_total_energy[df_total_energy['energia'] == energy_source]
        fig1.add_trace(go.Scatter(
            x=subset['data'], 
            y=subset['valor'], 
            mode='lines', 
            name=energy_source
        ))

    # Personalizando o layout
    fig1.update_layout(
        title='Total de Energia por Fonte ao Longo do Tempo (Todas as Regiões)',
        xaxis_title='Data',
        yaxis_title='Valor Total da Energia',
        hovermode='x unified',
        template='plotly_dark', 
        legend_title='Fonte de Energia'
    )

    # Configuracoes Grafico 2
    pivot_df = df_total_energy.pivot(index='data', columns='energia', values='valor')

    # Selecionando as colunas para a correlação
    selected_columns = ['hidraulica', 'termica', 'eolica']
    correlation_matrix = pivot_df[selected_columns].corr()

    # Formatando os valores para duas casas decimais
    z_text = [[f"{val:.2f}" for val in row] for row in correlation_matrix.values]

    # Gerando o heatmap interativo com Plotly
    fig2 = ff.create_annotated_heatmap(
        z=correlation_matrix.values,  
        x=correlation_matrix.columns.tolist(),  
        y=correlation_matrix.index.tolist(),  
        annotation_text=z_text,  
        colorscale='Purples',  
        showscale=True,  
        colorbar_title='Correlação', 
    )

    # Personalizando o layout
    fig2.update_layout(
        title={
            'text': 'Correlação: Hidráulica, Térmica e Eólica',
            'x': 0.0,  
            'xanchor': 'left',
            'y': 0.95 
        },
        xaxis_title='Fonte de Energia',
        yaxis_title='Fonte de Energia',
        annotations=[dict(font=dict(size=16))],  
        margin=dict(t=100),
    )

    # Exibição na Página
    st.header("Correlação:")
    st.write("O gráfico temporal apresenta a geração média de cada fonte renovável ao longo do tempo em MWmed, considerando todas as regiões do Brasil. Ele permite visualizar as variações na produção de energia e possíveis padrões sazonais.")    
    # Grafico Temporal
    st.plotly_chart(fig1)

    col1, col2, col3 = st.columns([0.3, 0.1, 0.5])
    col1.write("""
        Dentre as fontes analisadas, a hidráulica segue um ciclo anual bem definido, iniciando com alta geração e diminuindo progressivamente até o final do ano. Esse comportamento influencia diretamente outras fontes, como a térmica e a eólica.
             
        Para explorar essas relações, foi elaborado um gráfico de correlação, que compara a variação das diferentes fontes de energia. A fonte solar não foi incluída nessa análise, pois seus valores foram frequentemente insignificantes ou nulos ao longo do período observado.
    """)
    # Grafico de Correlacao
    col3.plotly_chart(fig2)
    st.write("Os cálculos do coeficiente de correlação (r) confirmam a relação inversa entre a geração hidráulica e as demais fontes: r = -0.41 entre hidráulica e eólica, e r = -0.66 entre hidráulica e térmica. Isso indica que, quando a geração hidráulica está alta, essas fontes tendem a apresentar uma redução, e vice-versa.")

    st.divider()

    # Conclusao
    st.header("Conclusão da Análise Inicial:")
    st.markdown(f"""
        <div class="flex">
            <p class="negrito">Hidráulica </p>
            <p>= É a mais estável e amplamente utilizada, sem grandes variações. Possui ciclos anuais e correlação inversa com a Térmica e a Eólica</p>
        </div>
        <div class="flex">
            <p class="negrito">Térmica </p>
            <p>= Tem uma produção considerável, com variação moderada.</p> 
        </div>
        <div class="flex">
            <p class="negrito">Eólica </p>
            <p>= Estava em crescimento no período analisado, mas com produção instável e alto coeficiente de variação.</p> 
        </div>
        <div class="flex">
            <p class="negrito">Solar </p>
            <p>= Apresentou a maior oscilação, possivelmente devido à sua implementação mais recente.</p>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

# Página de Distribuições
elif pages == "Distribuições":
    st.header("Distribuições")

    # Função para exibir gráfico Plotly
    def plot_distribution(x, y, title, xlabel, ylabel):
        fig = go.Figure(data=[go.Bar(x=x, y=y)])
        fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
        st.plotly_chart(fig)

    mapeamento_nomes = {
    "Hidráulica": "hidraulica",
    "Térmica": "termica",
    "Eólica": "eolica",
    "Solar": "solar"
    }

    col1, col2, col3 = st.columns([0.3, 0.2, 0.5])
    # Criando selectbox com as keys 
    opcoes_formatadas = list(mapeamento_nomes.keys())
    coluna_escolhida_formatada = col1.selectbox("Escolha uma fonte renovável:", opcoes_formatadas)

    # Convertendo para o nome original antes de buscar no DataFrame
    coluna_escolhida = mapeamento_nomes[coluna_escolhida_formatada]

    if coluna_escolhida:
        col3.write("Distribuição dos dados:")
       # Descrever a coluna escolhida
        descricao = df[coluna_escolhida].describe()

        # Remover o 'count'
        descricao_sem_count = descricao.drop('count')

        # Formatar os valores
        descricao_formatada = descricao_sem_count.apply(lambda x: "{:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", "."))

        # Transpor para ter as estatísticas como colunas
        descricao_transposta = descricao_formatada.to_frame().transpose()

        # Exibir no Streamlit
        col3.write(descricao_transposta)

        # Escolha da distribuicao
        dist = st.selectbox("Escolha a distribuição para análise:", ["Poisson", "Normal"])

        if dist == "Poisson":
            # Explicação da Distribuição
            st.header("Distribução de Poisson:")
            st.write("""A distribuição de Poisson é utilizada para modelar o número de ocorrências de um evento em um intervalo de tempo ou espaço fixo, onde os eventos são independentes entre si e ocorrem a uma taxa constante. É uma boa ferramenta para entender a variabilidade e as probabilidades de ocorrência desses eventos. Ao usar essa distribuição, você pode obter insights sobre o comportamento de sistemas e processos em que os eventos não seguem um padrão previsível, mas têm uma taxa constante de ocorrência. Ela é caracterizada por um único parâmetro:""")
            st.markdown("""
                <ul>
                    <li>λ (taxa média de ocorrência): Representa a média de eventos que ocorrem em um intervalo de tempo ou espaço.</li>
                </ul>
                <h4>Sugestões de Input:</h4>
                <p>Número Mínimo e Máximo de Eventos: Esses parâmetros controlam o intervalo de valores possíveis para os eventos a serem analisados. O número mínimo pode ser 0, pois é improvável que ocorra um valor negativo, mas, se a taxa média for muito grande (como é o caso), pode ser mais próximo. O número máximo pode ser determinado com base na taxa média de ocorrência (λ) ou ser ajustado dinamicamente para observar diferentes intervalos.</p>
                <hr>
            """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns([0.3, 0.2, 0.5])
            
            lambda_est = df[coluna_escolhida].mean()

            x_min = col1.number_input("Número mínimo de eventos",value=0)
            x_max = col1.number_input("Número máximo de eventos desejado",value=2*lambda_est)
            
            x = np.arange(x_min, x_max)
            y = stats.poisson.pmf(x, lambda_est)
            y_cdf = stats.poisson.cdf(x,lambda_est)

            df_poisson = pd.DataFrame({"X": x, "P(X)": y, "P(X ≤ k) (Acumulado)": np.cumsum(y),"P(X > k) (Acumulado Cauda Direita)": 1-np.cumsum(y)}).set_index("X")

            col3.write("Tabela de probabilidades:")
            col3.write(df_poisson)
            
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
            # Explicação da Distribuição
            st.header("Distribução Normal:")
            st.write("""A distribuição normal é caracterizada pela forma de "sino", onde a maioria dos dados se agrupa em torno da média, e a probabilidade diminui à medida que nos afastamos dessa média, ela é muito útil para prever ou entender o comportamento de um conjunto de dados. A distribuição normal é definida por dois parâmetros principais:""")
            st.markdown("""
                <ul>
                    <li>μ (média): A posição do centro da distribuição.</li>
                    <li>σ (desvio padrão): A medida de dispersão ou variabilidade dos dados em torno da média.</li>
                </ul>
                <h4>Sugestões de Input:</h4>
                <p>A largura de classe é a espessura de cada "barra" no histograma. Você pode ajustar a granularidade da visualização. Uma largura de classe muito pequena pode resultar em muito "ruído" (ou variação aleatória), enquanto uma largura muito grande pode esconder detalhes importantes da distribuição.</p>
                <p>Sugiro definir a largura de classe perto da média, a distribuição do histograma pode refletir de forma mais fiel a densidade dos dados ao redor da média, sem exagerar na dispersão. Outra opção seria colocar um valor que é um pequeno múltiplo da média ou do desvio padrão. Por exemplo, um valor como 1x, 2x ou 3x da média ou do desvio padrão</p>
                <hr>
            """, unsafe_allow_html=True)

            n = df[coluna_escolhida].count()
            mu_est = df[coluna_escolhida].mean()
            sigma_est = df[coluna_escolhida].std()
            st.subheader(f"Estimativa de μ: {mu_est:.2f}, σ: {sigma_est:.2f}")

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
            st.header("Verificar se os dados seguem a Distribuição Normal:")
            st.pyplot(ggplot.draw(p))

# Página das Planilhas
elif pages == "Planilha dos Dados":
    st.header("Planilha dos Dados:")

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

    # Formatar a coluna 'Ano' para garantir que não tenha separador de milhar
    df_filtered['Ano'] = df_filtered['Ano'].apply(lambda x: str(int(x)))  # Convertendo para string sem ponto de milhar

    # Exibir a tabela com barras de progresso
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
        },
        use_container_width=True  # Largura total da tela
    )

    st.header("Conclusão:")
    st.write("""
        Ao analisar o total de energia produzida por ano, observa-se que a hidráulica continua sendo a principal fonte, com a maior produção. No entanto, seu crescimento ao longo do tempo não é significativo, o que reforça sua estabilidade e previsibilidade.

        A térmica apresentou uma leve redução na produção ao longo dos anos, mas sem grandes variações, sendo a segunda fonte mais previsível.

        O gráfico indica que a eólica teve uma produção expressiva desde 2020. Isso sugere que a moda em 0 MWmed pode não estar necessariamente relacionada ao início da implementação, mas sim à sua dependência de fatores climáticos. Como a geração eólica varia conforme as condições do vento, há períodos com baixa produção e outros com alta geração, tornando essa fonte menos previsível.

        Por outro lado, a solar apresenta fortes indícios de estar em fase de implantação, sendo a fonte com maior crescimento desde o início da produção. A planilha criada deixa essa análise ainda mais evidente, com as barras coloridas destacando visualmente a evolução de cada fonte ao longo do tempo. Essa representação gráfica complementa os dados numéricos e reforça as tendências observadas, tornando a interpretação mais intuitiva e acessível.
    """)


# Configurações sidebar
st.sidebar.divider()
st.sidebar.markdown("Carolina Cavalli Machado")
st.sidebar.markdown(f"""<a href="https://www.linkedin.com/in/carolinacavallimachado">Linkedin</a> • <a href="https://github.com/CavMCarolina">GitHub</a>""", unsafe_allow_html=True)