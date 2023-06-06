from funcoes import *
from funcoes.crud import *

while True:
    linha()
    print("MENU PRINCIPAL".center(40))
    linha()
    print('''1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Remover pessoa
4 - Atualizar cadastro
5 - Sair do sistema''')
    linha()
    opc = leiaInt('Sua opção: ')
    
    if opc == 1:
        linha()
        print('Pessoas Cadastradas'.center(40))
        linha()
        ler()
    
    elif opc == 2:
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastro = cadastrar(nome, idade)
        print(f'{nome} foi cadastrado(a) com sucesso!')
    
    elif opc == 3:
        linha()
        print('Pessoas Cadastradas'.center(40))
        linha()
        ler()
        linha()
        id = int(input('Digite o ID que deseja remover: '))
        remover(id)
        print(f'Registro removido com sucesso!')
    
    elif opc == 4:
        linha()
        print('Pessoas Cadastradas'.center(40))
        linha()
        ler()
        linha()
        id = int(input('Digite o ID de quem deseja atualizar: '))
        mostrar=mostrar(id)
        novoNome = str(input(f'Atualizar nome {mostrar.get("nome")}: ')or mostrar.get("nome"))
        novaIdade = int(input('Nova idade: '))
        atualizar(id, novoNome, novaIdade)
        print(f'Registro atualizado com sucesso!')
    
    elif opc == 5:
        print('Obrigado, volte sempre!!!')
        break
    
    else:
        print('Digite uma opção válida!')
        continue
