from Lógica import *
# Calcule o fatorial

# Variáveis
#fat = 1

while True:
# Apresentação
    print('\n\t\t\t -- Calcula Fatorial \n\n')
    print('1.Fatorial')
    print('2.Tabuada')
    print('3.Sair')
# Entrada

    op = int(input('opção:'))
#Processamento
#for cont in range(1, num+1):
 #   fat *= cont
    if op == 1:
        num = int(input('\nInforme um número: '))
        fat = gera_fatorial(num)
#Saída
        print(f'{num}! = {fat}')

    elif op == 2:
        num = int(input('\nInforme um número: '))
        print(gerar_tabuada(num))
    elif op == 3:
        print('\nBye')
        break
    else:
        print('\ninvalido')




