#==> Importando bibliotecas.
import pandas as pd

#==> Definindo funcao
def convert_csv(conjunto: pd.DataFrame, nome_arquivo: str):
    """
    Converte um DataFrame em um arquivo CSV.

    Parâmetros:
    conjunto (DataFrame): O conjunto de dados a ser convertido.
    nome_arquivo (str): O nome do arquivo CSV a ser salvo.

    Retorno:
    Nenhum.
    """
    #==> Salva o DataFrame como um arquivo CSV    
    conjunto.to_csv(f'../file/{nome_arquivo}.csv', index=False)