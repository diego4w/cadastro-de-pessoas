def menu():
    print(''' Escolha uma opcao:

            1. Cadastrar uma pessoas
            2. Listar pessoas
            3. sair

    ''')

def cadastrar(pessoas):
    identificador = input('id? ')
    nome = input('nome? ')
    idade= input('idade? ')
    pessoas.append((identificador, nome, idade))

def listar(pessoas):
    for pessoa in pessoas:
        idetificador,nome,idade = pessoa
        print(f'nome: {nome}, idade: {idade}, id: {idetificador}')
    

def main():
    pessoas = []

    while True:
        menu()
        opcao = int(input('opcao? '))
        if opcao == 1:
            cadastrar(pessoas)
        elif opcao == 2:
            listar(pessoas)
        elif opcao == 3:
            return 0
        else:
            print('opcao invalida')

main()