# Lógica do sistema

#Função que calcula fatorial

def gera_fatorial(valor):
    if valor > 1:
        fat = valor * gera_fatorial(valor - 1)
        return fat
    else:
        return 1

def gerar_tabuada(valor):
    for cont in range(1,11):
         print(f'{cont} X {valor} = {cont * valor}')
