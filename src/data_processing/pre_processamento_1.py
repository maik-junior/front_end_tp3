#==> Importando bibliotecas
import pandas as pd
from openpyxl import load_workbook

#==> Definindo funcao
def pre_processamento(nome_arquivo: str, nome_saida: str):
    '''
    Funcao:
    - Faz leitura de arquivo .xlsx
    - Renomeia colunas
    - Substitui dados
    
    Retorna: Nada
    '''
    df = pd.read_excel(f'../file/{nome_arquivo}.xlsx')[5:].dropna().reset_index(drop=True)
    df.columns = ['Perfil_Turista', 'Brasil','Rio_de_Janeiro','Sao_Paulo','Porto_Alegre']
    df.replace('...', 0, inplace=True)
    df.to_csv(f'../file/{nome_saida}.csv', index=False)
    

