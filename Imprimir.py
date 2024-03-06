#PROJETO 1 - FATORIAL DE UM NÚMERO
'''Crie um programa que recebe um número e imprime o seu fatorial '''

#Método 5Q's para montar um algorítimo:
'''1 Quais são os dados de entrada necessários?
-Número
2 O que devo fazer com estes dados?
-Calcular o fatorial do número que for passado para o meu programa e exibir na tela
3 Quais são as restrições deste problema?
-O número deve ser um valor positivo
-O número deve ser um valor inteiro
4 Qual é o resultado esperado?
-Fatorial do número providenciado seja exibibido
5 Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
-input numero
-if numero > 0
-if numero = inteiro
-fatorial = 1
-loop de 1 a numero
-fatorial = fatorial * numero
-print(fatorial)'''

numero = int(input('Digite um número: '))
if numero>0:
  fatorial=1
  for item in range(1,numero+1):
    fatorial=fatorial*item
  print(fatorial)
