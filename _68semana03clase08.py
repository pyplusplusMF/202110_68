#ciclos en python

def teoriaCicloWhile():
  n = 5
  while n > 0:
      print(n)
      n = n - 1
      print('Despegue!')
  print ("n", n)

teoriaCicloWhile()



def factorial1 (n: int) -> int:
    factorial = 1
    i = 1
    while (i <= n):
        factorial *= i #factorial = factorial * i 
        i += 1 #i = i + 1
    return factorial


print (factorial1(0)) #1
print (factorial1(1)) #1
print (factorial1(3)) # 1 * 2 * 3



def cicloControladoPorEvento ():
    promedio, total, contar = 0.0, 0, 0

    print("Introduzca la nota de un estudiante (-1 para salir): ")
    grado = int(input())
    while grado != -1:
        total = total + grado
        contar = contar + 1
        print("Introduzca la nota de un estudiante (-1 para salir): ")
        grado = int(input())
    promedio = total / contar
    print("Promedio de notas del grado escolar es: " + str(promedio))

cicloControladoPorEvento()


def cicloConBreak():
    variable = 10

    while variable > 0:
        print('Actual valor de variable:', variable)
        variable = variable - 1
        if variable == 5:
            print ("La variable ha tomado el valor de 5...Fin")
            break
cicloConBreak()


def cicloConContinue():
    variable = 10
    while variable > 0:
        variable = variable - 1
        if variable == 5:
            continue
        print('Actual valor de variable:', variable) # no imprime el 5
cicloConContinue()