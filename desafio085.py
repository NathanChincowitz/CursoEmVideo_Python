'''
crie uma programa onde o usuario possa digitar sete valores numericos e mantenha separados os valores pares e impares
no final mostre os valores pares e impares em ordem crescente
'''
lista = [[],[]]
temp = []

for i in range(0,7):
    temp.append(int(input('Digite um valor inteiro: ')))
    if temp[0] % 2 == 0: #se for par
        lista[0].append(temp[:])
    else: #se for impar
        lista[1].append(temp[:])
    temp.clear()
    
lista = [sorted(lista[0])], [sorted(lista[1])]
print(f'''Os valores pares digitados foram: {lista[0]}
Os valores impares digitados foram: {lista[1]}''')
