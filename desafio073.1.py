'''
crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação
depois mostre:
a) apenas os 5 primeiro colocados
b) os ultimos 4 colocados
c) uma lista com os times em ordem alfabetica
d) em que posição na tabela esta o time da chapecoense(envelheceu mal, vou por Fortaleza no lugar)
'''
#a principio era um programa passivo sem interação com usuario que iria somente mostrar todos os dados de uma vez
#mas decidi adicionar uma interface

colocados = ('Flamengo', 'Palmeiras', 'São Paulo', 'Athletico Paranaense', 'Atlético Mineiro', 'Corinthians', 'Fluminense', 'Grêmio', 'Fortaleza', 'América Mineiro', 'Intencional', 'Santos', 'Bahia', 'Botafogo', 'Red Bull Bragantino', 'Atlético Goianiense', 'Cruzeiro', 'Ceará', 'Cuiabá', 'Goiás')
menu = 0

while True:
    while True:
        menu = input('''
 [1] Exibir os 5 primeiro colocados
 [2] Exibir os ultimos 4 colocados
 [3] Exibir todos os times em ordem alfabética
 [4] Exibir posição do Fortaleza
 [5] Sair
 Selecionar: ''')
        if menu in '12345':
            break
    
    #cinco primeiro colocados
    if menu == '1':
        print('Os 5 primeiros colocados são: ')
        for i in range(1,6):
            print(f'    Em {i}°',colocados[i-1])

    #quatro ultimos colocados
    if menu == '2':
        print('\nOs ultimos 4 colocados são: ')
        for i in range(-4,0):
            print(f'    Em {i+21}° esta {colocados[i]}')

    #times em ordem alfabeticas
    if menu == '3':
        print(f'\nOs times são: ')
        for i in range(0,len(colocados)):
            print('   ',sorted(colocados)[i])
    
    #mostrar posição de time especifico
    if menu == '4':
        flu_index = (colocados.index('Fortaleza')) + 1
        print(f'\nFortaleza esta na {flu_index}° colocação')
    
    if menu == '5':
        break