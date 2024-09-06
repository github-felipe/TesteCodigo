print('Seja bem-vindo(a) ao verificador de letra "A". Como o nome sugere o objetivo do programa é verifcar se existe letra "A" no texto, retornando a quantidade de vezes em que ela se faz presente.')
Texto = str(input('Digite Qual texto você deseja verificar: '))

Texto = list(Texto.lower())

QuantLetraA = Texto.count('a')

if QuantLetraA == 0:
    print('Não existe letras "A" nesse texto!')
else:
    print(f'Nesse texto a letra "a" se faz presente em um total de {QuantLetraA} vezes!')
