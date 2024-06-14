'''
crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista
caso ja exista la dentro ele nao sera adicionado
no final serao exibidos todos os valores únicos digitados em ordem crescente
'''
lista = []
n = 0
print('Para parar o programa digite um caractere alfabetico')
while True:
    n = (input('Digite um valor para adicionar a lista: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor ja digitado anteriormente. Número NÃO adicionado a lista')
        
    check_break = lista[-1]
    if check_break.isnumeric() == False:
        lista.pop()
        break

print(f'os numeros digitados foram: {sorted(lista)}')
