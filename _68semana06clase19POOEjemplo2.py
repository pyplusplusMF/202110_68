# Clase del jueves 19 de Junio
# Ejemplo de la clase círculo

# Realizar una clase circulo que tenga como atributos el radio
# los métodos serán el perimetro y el area
import math
class Circulo:
    # definir el constructor
    def __init__ (self, radio = 1):
        self.radio = radio
    
    # Método para obtener el perimetro
    def getPerimetro (self):
        p = 2 * math.pi * self.radio 
        return p
    
    # Método para obtener el area
    def getArea (self):
        a = math.pi * ( self.radio ** 2 )
        return a
    
    # Establecer el atributo radio
    def setRadio (self, radio):
        self.radio = radio

objetoCirculoA = Circulo()
print ('radio = ', objetoCirculoA.radio)
print ('perimetro =', objetoCirculoA.getPerimetro())
print ('area = ', objetoCirculoA.getArea())

objetoCirculoB = Circulo(5)
print ('radio = ', objetoCirculoB.radio)
print ('perimetro =', objetoCirculoB.getPerimetro())
print ('area = ', objetoCirculoB.getArea())


objetoCirculoC = Circulo()
objetoCirculoC.radio  = 5
print ('radio = ', objetoCirculoC.radio)
print ('perimetro =', objetoCirculoC.getPerimetro())
print ('area = ', objetoCirculoC.getArea())


# objetoCirculoA = Circulo()
# print ('radio = ', objetoCirculoA.radio)
# print ('perimetro =', objetoCirculoA.getPerimetro())
# print ('area = ', objetoCirculoA.getArea())

# radio =  1
# perimetro = 6.283185307179586
# area =  3.141592653589793


# objetoCirculoB = Circulo(5)
# print ('radio = ', objetoCirculoB.radio)
# print ('perimetro =', objetoCirculoB.getPerimetro())
# print ('area = ', objetoCirculoB.getArea())

# radio =  5
# perimetro = 31.41592653589793
# area =  78.53981633974483



# objetoCirculoC = Circulo()
# objetoCirculoC.radio  = 5
# print ('radio = ', objetoCirculoC.radio)
# print ('perimetro =', objetoCirculoC.getPerimetro())
# print ('area = ', objetoCirculoC.getArea())


# radio =  5
# perimetro = 31.41592653589793
# area =  78.53981633974483