'''
Objetivo 90 -
Faça um programa que leia nome e média, de um aluno.
    Guardado também a situação em um dicionário. No final mostre
o conteúdo da estrutura na tela.
'''
print(f'{"Seja, Bem Vindo":>35}')
print(f'Boletim Escolar:')
print(f'Vamos adicionar a estrutura do "diconário" juntamente com valores cedidos pelo usuário,e apresentar o resultado da estrutura ao final!')
print()
# Etapa - 1
estudante = {} # Criação do dicionário
# Etapa 2  Adiciona as keys juntamente com values
estudante['nome'] = str(input(f'Nome: ')).upper()
estudante['média'] = float(input(f'Média de {estudante["nome"]}: '))
# Testa as medias ,e os posteriores comandos  adidonam com keys 'situação' e values ''.
if estudante['média'] >=7:
    estudante['situação'] = 'Aprovado'
elif estudante['média'] >= 5 :
    estudante['situação'] = 'Recuperação'
else:
    estudante['situação'] = 'Reprovado'
print() # Quebra de linha
for k , v in estudante.items():
    # Exibi  kesy separados pro uma seta values
    print(f'{k} -> {v}')
print()
print('-==-==-'*10)
print("Fim do programa. Obrigado por usar o Boletim Escolar!")
