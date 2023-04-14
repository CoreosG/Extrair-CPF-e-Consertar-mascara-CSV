# Script de Processamento de CPF

Este script ajuda a processar arquivos CSV contendo números de CPF, corrigindo a máscara do CPF e identificando CPFs repetidos. Ele oferece um menu simples para o usuário escolher entre as opções disponíveis.

Este Script foi criado para auxiliar um colega no trabalho que tem de lidar com estas 2 situações com frequência.

## Recursos

- Ler arquivos CSV contendo números de CPF
- Corrigir a formatação da máscara do CPF
- Identificar e salvar linhas com CPFs repetidos
- Salvar os dados processados em um novo arquivo Excel

## Como usar

1. Certifique-se de ter o Python 3 instalado em seu sistema.
2. Instale as dependências necessárias usando o pip:

```
pip install requirements.txt
```

3. Execute o script:

```
python main.py
```

4. Escolha uma opção digitando o número correspondente:

```
- Opção 1: Extrair as linhas com CPFs repetidos em um novo arquivo Excel
- Opção 2: Corrigir a máscara do CPF e salvar em um novo arquivo Excel
- Opção 3: Sair do script
```

5. Insira o nome do arquivo ou o caminho completo do arquivo CSV que deseja processar.

6. O script salvará os dados processados em um novo arquivo Excel com um sufixo indicando a operação realizada, seja `_CPF_repetidos` para CPFs repetidos ou `_CPF_corrigido` para correção da máscara do CPF.

## Observações

- O arquivo CSV deve conter uma coluna com um cabeçalho contendo a palavra "CPF" (não sensível a maiúsculas e minúsculas). O script detectará automaticamente essa coluna para realizar as operações.
- O script assume que o delimitador do arquivo CSV é uma vírgula `,`.
- Se o arquivo de entrada não estiver no mesmo diretório do script, certifique-se de fornecer o caminho completo do arquivo.
- Este script funciona apenas se houver uma única coluna com "CPF" no cabeçalho. Se o arquivo tiver mais de uma coluna com "CPF", o script pegará a primeira coluna encontrada.
