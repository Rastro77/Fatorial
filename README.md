Criar um programa que recebe dois valores e exibe qual é o maior entre eles.
'''Fatorial'''

'''input numero
  if numero > 0
  if numero == inteiro
  fatorial = 1
  loop de 1 a numero
  fatorial = fatorial * numero
  print fatorial'''

numero = int(input("Digite um numero: "))
if numero > 0:
  fatorial = 1
  for item in range(1,numero + 1):
    fatorial = fatorial * item
  print(fatorial)
