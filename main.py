from arvore import *

print('-='*5 + 'Acervo Bibliotecário' + '-='*5)
print('''(1) Inserir livro
(2) Buscar livro por titulo
(3) Buscar livros por ano
(4) Remover livro
(5) Listar livros em ordem alfabética
(6) Altura da arvore
(7) Sair do programa.''')
print('-='*20)
print()

x = input('Escolha uma opção: ')
while x not in '1234567':
    x = input('Opção inválida.\nTente novamente: ')
print()

raiz = None

while x != '7':
    if x == '1':
        print('Inserção')
        titulo = input('Informe o título do livro: ').lower()
        if titulo == '':
            print('Invalido')
        else:
            if buscaTitulo(raiz,titulo):
                print('Já existe esse livro')
                pass
            
            else:
                ano = input('Ano da publicação: ')
                raiz = inserir(raiz, titulo, ano)
                balancear(raiz)
        
    elif x == '2':
        titulo = input('Título do livro: ').lower()
        busca = buscaTitulo(raiz, titulo)

        if busca is None:
            print('Livro informado não existe no catálogo')

        else:
            print('Busca feita com sucesso!')
            print(busca)
    
    elif x == '3':
        ano = input('Ano a pesquisar: ')
        busca = buscaAno(raiz, ano)

        if busca == [] or busca == None:
            print('No acervo não há livros com o ano informado')

        else:
            print(busca)
    
    elif x == '4':
        titulo = input('Título do livro: ').lower()

        if buscaTitulo(raiz, titulo) is None:
            print('Livro informado não existe no catálogo')

        else:
            raiz = excluir(raiz, titulo)
            balancear(raiz)
            print('Remoção feita com sucesso!')
    
    elif x == '5':
        print(transfere(raiz))
    
    elif x == '6':
        if raiz == None:
          print('Árvore vazia.')
        else:
          print('Altura da árvore\n' + str(raiz.profundidade()))
    else:
      print('Nenhuma opção inserida, tente novamente.')
    

    print()
    print('-='*5 + 'Acervo Bibliotecário' + '-='*5)
    print('''(1) Inserir livro
(2) Buscar livro por titulo
(3) Buscar livros por ano
(4) Remover livro
(5) Listar livros em ordem alfabética
(6) Altura da arvore
(7) Sair do programa.''')
    print('-='*20)
    print()

    x = input('Escolha uma opção: ')
    while x not in '1234567':
        x = input('Opção inválida.\nTente novamente: ')
    print()
    

else:
    print("Fim do programa.")