from funcoes.conexao import cursor, conexao


def ler():
    comando = 'select * from pessoas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(f'{"ID":<1} {"Nome":<30}{"Idade":<40}')
    print('~' * 40)
    for i in range(0,len(resultado)):
        id = resultado[i]["id"]
        nome = resultado[i]["nome"]
        idade = resultado[i]["idade"]
        print(f'{id:<1}  {nome:<30} {idade:<40}')
    # for v in resultado:
    #     for d in v.values():
    #         print(f'{d:>10}', end='')
    #     print()


def cadastrar(nome, idade):
    comando = f'insert into pessoas(nome, idade) values ("{nome}",{idade})'
    cursor.execute(comando)
    conexao.commit()


def remover(id):
    comando = f'delete from pessoas where id = {id}'
    cursor.execute(comando)
    conexao.commit()
    

def atualizar(id, novoNome, novaIdade):
    comando = comando = f'update pessoas set nome = "{novoNome}", idade = {novaIdade} where id = {id}'
    cursor.execute(comando)
    conexao.commit()
    

def mostrar(id):
    comando = f'select * from pessoas where id = {id}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    # for i in range(0,len(resultado)):
    nome = resultado[0]
    # idade = resultado[]
    # print(f'{nome:<30}')
    return nome 