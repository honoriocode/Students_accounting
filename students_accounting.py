aula = 35
nome = input('Informe o nome do aluno : ')
qtde_week = int(input('Quantidade de aulas por semana : '))
qtde_mes = qtde_week * 4
print(f'Quantidade de aulas mensais : {qtde_mes}')
total = qtde_mes * aula
desconto = input('O aluno receberá desconto ? S/N ')
if desconto == 'S':
    valordesc = int(input('Qual o valor do desconto ? '))
    totaldesc = total - (total * valordesc/100)
    print(f'O aluno {nome} pagará a mensalidade no valor de {totaldesc}')
else:
    print('Sem descontos no momento')
    print(f'O aluno {nome} pagará a mensalidade no valor de {total}')