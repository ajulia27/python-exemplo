alunos = ['maria']
alunos.append('Rafael')
while True:
      nome = input('digite o nome do aluno: ')
      alunos.append(nome)
      resposta = input('deseja adicionar mais um aluno? (S/N): ')
      if resposta.upper() == 'N':
            break
print(f"Alunos cadastrados: (alunos)")