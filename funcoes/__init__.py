def linha(tam = 40):
    linha = print('-' * tam)
    return linha

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = (str(input(msg)))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('Digite um número inteiro válido.')
        if ok:
            break
    return valor
