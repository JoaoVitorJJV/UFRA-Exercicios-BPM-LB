print('________________ALUNO APROVADO___________________')

# Dados
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + 2 * nota2) / 3

if media >= 5:
    print('Media: {:.1f} \nAPROVADO'.format(media))
elif media < 5:
     print('Media: {:.1f} \nREPROVADO'.format(media))