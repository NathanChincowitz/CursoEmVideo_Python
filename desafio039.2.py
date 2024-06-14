#codigo refeito com leitura simplificado apos resolução do exercicio

from datetime import date

nascimento = int(input('digite seu ano de nascimento: '))
genero = input('digite seu genero: M para masculino e F para feminino').strip().upper()
hoje  = int(date.today().year)
idade = hoje - nascimento

if genero == 'F':
    print('voce nao precisa fazer o alistamento obrigatorio')
else:
    if idade == 18:
        print('esta na hora de se alistar')
    
    elif idade < 18:
        print(f'ainda não é hora, faltam {18-idade} anos para o alistamento obrigatorio')
        ano = nascimento + 18
        print(f'seu alsitamento sera no ano de {ano}')
    elif idade > 18:
        print(f'seu tempo de alistamento foi a {idade-18} anos atras')
        ano = nascimento + 18
        print(f'seu alsitamento foi no ano de {ano}')