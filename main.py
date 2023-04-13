import pandas as pd
from time import sleep
import os, openpyxl

def fix_cpf_mask(cpf):
    cpf = ''.join(filter(str.isdigit, str(cpf)))  # Keep only numeric characters
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"  # Format CPF

def openCSV(file):
    if(not os.path.exists(file)):
        print('Arquivo não encontrado! certifique-se que o arquivo está na mesma pasta do programa')
        sleep(5)
        exit()
    return pd.read_csv(file, sep=',', encoding='utf-8')

def repeatedCPF(df):
    # Find the CPF column header
    cpf_column = None
    for col in df.columns:
        if 'CPF' in col:
            cpf_column = col
            break

    if cpf_column is None:
        print("coluna CPF não encontrada")
        return pd.DataFrame()

    # Fix the CPF mask for the CPF column
    df[cpf_column] = df[cpf_column].apply(fix_cpf_mask)
    
    # Find rows with repeated CPF values
    repeated_cpf = df[df.duplicated(subset=cpf_column, keep=False)]
    return repeated_cpf



def saveExcel(df, file):
    if os.path.exists(file + '.xlsx'):
        os.remove(file + '.xlsx')  # Add the correct file extension here
        print('Arquivo já existente, removendo arquivo antigo...')
    df.to_excel(file + '.xlsx', index=False)
    print('Arquivo salvo com sucesso! \n' + file + '.xlsx')



if __name__ == '__main__':
    nomeArquivo = input('Digite o nome do arquivo: ')
    df = openCSV(nomeArquivo)
    repeated_cpf = repeatedCPF(df)
    saveExcel(repeated_cpf,  nomeArquivo.removesuffix('.csv') + '_cpf_repetidos')
    sleep(5)
    

    