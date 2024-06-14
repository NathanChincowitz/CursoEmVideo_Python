'''
refaça o desafio 35 dos triangulos acrescentando o recurso de mostrar o tipo de triangulo sera formado
- equilatero todos lados iguais
- isosceles dois lados iguais
- escaleno todos os lados diferentes
'''

n1 = float(input('primeiro valor: '))
n2 = float(input('segundo valor: '))
n3 = float(input('terceiro valor: '))

lista = sorted([n1,n2,n3])

c1 = lista[0]
c2 = lista[1]
h  = lista[2]

if c1 + c2 < h:
    print('Não é possivel formar um triangulo os os valores sugeridos!')
elif c1 == c2 == h:
    print('É possivel formar um triangulo, e ele é um triangulo equilatero!')
elif c1 == c2 or c2 == h:
    print('É possivel formar um triangulo e ele é um triangulo isosceles!')
elif c1 != c2 != h != c1:
    print('é possivel formar um triangulo,e ele é um triangulo escaleno!')