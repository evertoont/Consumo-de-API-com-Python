import requests
import json
import os
import time

def main():
    print('\n********** Escolha uma opção **********\n')
    print('1 - Procurar filme')
    print('2 - Sair')
    opcao = input('Opção: ')

    if opcao == '1':
        escolher_filme()
    elif opcao == '2':
        exit()
    else:
        main()


def escolher_filme():
    nome_filme = input('\nDigite o nome do filme em INGLÊS: ')

    requisicao(nome_filme)


def requisicao(nome_filme):

    lista_de_filmes = []
    print('Pesquisando...')

    for pagina in range(1,101):
        url = f'http://www.omdbapi.com/?i=tt3896198&apikey=315afb54&s={nome_filme}&type=movie&page={pagina}'
        
        try:
            resposta = requests.get(url)
            dicionario_filme = json.loads(resposta.text)

            if dicionario_filme['Response'] == 'True':
                for filme in dicionario_filme['Search']:
                    lista_de_filmes.append(filme['Title'])

            else:
                return criar_arquivo(lista_de_filmes, nome_filme, pagina)

        except Exception as erro:
            return print('Erro na conexão ', erro)


def criar_arquivo(lista_filmes, nome_filme, pagina):

    print('Criando arquivo...')

    with open(f'filmes {nome_filme}.txt', 'w') as arquivo:
        for filme in lista_filmes:
            arquivo.write(filme + '\n')
    
    total_paginas = pagina - 1
    total_filmes = len(lista_filmes)

    return resultado_pesquisa(total_filmes, total_paginas)


def resultado_pesquisa(total_filmes, paginas):    
    print('\n###############################################################')
    print(f'Pesquisa feita em {paginas} paginas')
    print(f'Filmes encontrados: {total_filmes}')
    print('Pesquisa encerrada! Consulte o TXT criado com a lista de filmes')
    print('###############################################################')
    time.sleep(10)
    os.system('cls' if os.name == 'nt' else 'clear')
    main()


if __name__ == '__main__':
    main()