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
                arquivo = open(f'filmes {nome_filme}.txt', 'a')

                for filme in dicionario_filme['Search']:
                    arquivo.write(filme['Title'] + '\n')
                    lista_de_filmes.append(filme['Title'])

            else:
                arquivo.close()
                return resultado_pesquisa(len(lista_de_filmes), pagina-1)

        except Exception as erro:
            return print('Erro na conexão ', erro)


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