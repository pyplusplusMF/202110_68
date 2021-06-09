# miércoles 9 de junio
# matplotlib
# https://matplotlib.org/stable/gallery/index.html

import matplotlib.pyplot as plt

def ejemplo1 ():
  x1=[2,5,6,14] 
  y1= [11,22,33,44]

  # grupo B
  x2=[2,5,6,15]
  y2=[4,12,18,45]

  #Graficar 2 lineas en la misma grid
  plt.plot(x1,y1, color="blue", linewidth = 3, label = 'Linea 1')
  plt.plot(x2,y2, color="green", linewidth = 3, label = 'Linea 2')

  plt.title('Dos Graficas juntas')
  plt.xlabel('Eje X')
  plt.ylabel('Eje Y')
  plt.legend()
  plt.grid()
  plt.show()
# ejemplo1
def ejemplo2():
  #Histogramas
  Datos = [20,22,21,20,23,25,28,40,22,23,22,15,16,18,18,19,21,22,24,4,12,17,17,22,30,]
  Rangobin=[0,10,20,30,40]
  plt.hist(Datos, Rangobin, histtype='bar',rwidth=0.8, color='lightgreen')

  plt.title('Histograma')
  plt.xlabel('Eje X')
  plt.ylabel('Eje Y')
  plt.grid()  #la grid no es necesaria (lineas horizontales y verticales)
  plt.show()
# ejemplo2()

def ejemplo3():
  valores =[20,40,60,80]

  plt.pie(valores, labels=['Prekinder', 'kinder', 'primaria', 'secundaria'], colors=['red','purple','blue','orange']
          , startangle=90,shadow=True, explode=(0.1,0,0,0),autopct='%1.1f%%')
  plt.title('Grafico circular')
  plt.show()
ejemplo3()