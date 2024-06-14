'''
faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
ex: ana maria de souza
primeiro: ana
ultimo: souza
'''
nome = (input('digite seu nome completo: ')).title().split()
print(f"""
      seu primeiro nome é {nome[0]}
      seu ultimo nome é {nome[-1]}
      """)