import pandas as pd
from time import sleep
import os, openpyxl

def fix_cpf_mask(cpf):
    cpf = ''.join(filter(str.isdigit, str(cpf)))  # Keep only numeric characters
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"  # Format CPF

def openCSV(file):
    if not os.path.exists(file):
        print('Arquivo não encontrado! certifique-se que o arquivo está na pasta correta')
        sleep(5)
        exit()
    return pd.read_csv(file, sep=',', encoding='utf-8')

def findCPFColumn(df):
    # Find the CPF column header
    cpf_column = None
    for col in df.columns:
        if 'cpf' in col.lower():  # Perform a case-insensitive search
            cpf_column = col
            return cpf_column
    print("coluna com CPF não encontrada")
    return None

def fixCPFmask(df):
    cpf_column = findCPFColumn(df)
    # Fix the CPF mask for the CPF column
    df[cpf_column] = df[cpf_column].apply(fix_cpf_mask)
    return df

def saveExcel(df, file, suffix):
    file = file.removesuffix('.csv') + suffix
    if os.path.exists(file + '.xlsx'):
        os.remove(file + '.xlsx')
        print('Arquivo já existente, removendo arquivo antigo...')
    df.to_excel(file + '.xlsx', index=False)
    print('Arquivo salvo com sucesso! \n' + file + '.xlsx')

def repeatedCPF(df):
    # Fix the CPF mask for the CPF column
    df = fixCPFmask(df)
    cpf_column = findCPFColumn(df)
    # Find rows with repeated CPF values
    repeated_cpf = df[df.duplicated(subset=cpf_column, keep=False)]
    return repeated_cpf

def menu():
    print('1- Salvar os CPF repetidos')
    print('2- Consertar máscara do CPF')
    print('3- Sair')
    opt = int(input('Digite a opção desejada: '))
    return opt

def getFileName():
    print('Digite o caminho completo do arquivo ou apenas o nome do arquivo (se estiver na mesma pasta): ')
    nomeArquivo = input()
    return nomeArquivo

def main():
    opt = menu()
    if opt == 1:
        nomeArquivo = getFileName()
        df = openCSV(nomeArquivo)
        repeated_cpf = repeatedCPF(df)
        saveExcel(repeated_cpf, nomeArquivo, '_CPF_repetidos')
    elif opt == 2:
        nomeArquivo = getFileName()
        df = openCSV(nomeArquivo)
        df = fixCPFmask(df)
        saveExcel(df,  nomeArquivo, '_CPF_corrigido')
    else:
        print('Falow!')
        sleep(1)
        return False
    return True

if __name__ == '__main__':
    while main():
        pass
