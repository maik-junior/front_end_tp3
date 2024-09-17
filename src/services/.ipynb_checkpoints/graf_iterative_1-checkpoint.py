#==> Funcao gera graficos iterativos
import pandas as pd
import streamlit as st

def iteratividade_graf():   
    #==> Selecionar colunas
    selected_df = st.multiselect(
        'Selecione o tabela desejada: ',
        options=['Rio_de_Janeiro','Sao_Paulo','Porto_alegre'],key='5')
    
    #==> Exibindo e filtrando dataset com recurso de <@st.cache>
    @st.cache_data
    def exibe_dataframe(nome):
        try:
            df = pd.read_csv(f'../file/{nome}.csv')
            return df
        except FileNotFoundError:
            st.error(f"Arquivo {nome}.csv não encontrado.")
            return None
    
    #==> Definindo ordenacao
    ordenar = st.radio('Ordenar os dados:', ('Ordem crescente', 'Ordem decrescente'),key='3')
    
    #==> Exibe o conjunto selecionado
    if selected_df:
        for tabela in selected_df:
            df = exibe_dataframe(tabela)
    
            if df is not None:
                #==> Selecionar coluna para ordenacao
                coluna_para_ordenar = st.selectbox(f'Selecione a coluna para ordenar em {tabela}:', df.columns)
    
                #==> Ordenar conforme a selecao
                if ordenar == 'Ordem crescente':
                    df = df.sort_values(by=coluna_para_ordenar, ascending=True)
                elif ordenar == 'Ordem decrescente':
                    df = df.sort_values(by=coluna_para_ordenar, ascending=False)
    
                #==> Exibir conjunto
                st.dataframe(df)
    else:
        st.write('Nenhuma tabela selecionada.')