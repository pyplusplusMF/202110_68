# introduccion a la POO
# sesion del miercoles 9 de junio

class Empleado:
    def __init__(self):
        self.nombre = input('Ingrese su nombre: ')
        self.sueldo = float(input('Ingrese su sueldo: '))
    
    def imprimir (self):
        print ('Nombre', self.nombre  )
        print ('Sueldo ', self.sueldo)
        
    def pagarImpuesto(self):
        if (self.sueldo > 3000):
            print ('USted debe pagar impuesto')
        else:
            print ('usted no paga impuesto')

empleadoA = Empleado()
empleadoA.imprimir()
empleadoA.pagarImpuesto()

empleadoB = Empleado()
empleadoB.imprimir()
empleadoB.pagarImpuesto()

empleadoC = Empleado ()
empleadoC.imprimir()
empleadoC.pagarImpuesto()