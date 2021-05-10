#lunes 10 de mayo
'''
    Autor: Maria Medina
    Fecha: 10 - mayo - 2021 
    
'''


#Condicional simple
def condicionalSimple():
  print ("Condicional simple")
  x = 8
  if x > 0 :
      print('x es positivo')
condicionalSimple()


#condicional alternativa - doble
def condicionaDoble ():
  print ("Condicional doble")
  x = 10
  if x%2 == 0 :
      print('x es par')
  else :
      print('x es impar')
condicionaDoble()


#condicional encadenada - multiple
def condicionalEncadenada ():
  print ("Condicional encadenada")
  x= 8
  y= 8

  if x < y:
      print('"x" es menor que "y"')
  elif x > y:
      print('"x" is mayor que "y"')
  else:
      print('"x" y "y" son iguales')
condicionalEncadenada ()




#Condicional anidada 
def condicionalAnidado():
  x = 5
  if 0 < x:
      if x < 10:
          print('x es un número positivo de un solo dígito.')

  if 0 < x and x < 10:
    print('es un número positivo de un solo dígito')
condicionalAnidado ()


def excepciones1 ():
  #si alguien ingresa un valor diferente a un numero real 
  # se imprime el mensaje de error que ingrese un numero
  temperatura_fahr = input('Enter Fahrenheit Temperature:')
  try:
      fahr = float(temperatura_fahr)
      cel =  5.0 / (9.0 * (fahr - 32.0))
      print(cel)
  except:
      print('Please enter a number')

excepciones1 ()


#Clase 8 - Creación de instrucciones con condicionales.ipynb
#quedamos por los ejercicios al final