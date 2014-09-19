#1
def Cuadrado(numero):
    return numero **2
print ("Ejercicio #1")
numero= input ("Teclee el numero que quieres elevado al cuadrado: ")
resultado= (Cuadrado(int(numero)))
print("El resultado es: {}".format(resultado))
#2
import datetime
def Cumple(edad):
    actual= datetime.datetime.now().year
    dedad= datetime.datetime.strptime(dfecha, "%d/%m/%Y").year
    return (actual-dedad)
print ("Ejercicio #2")
dfecha= input("Cual es tu fecha de nacimiento? (formato dd/mm/aaaa) ")
edad= Cumple (dfecha)
print ("Tienes {} años".format(edad))
#3
import datetime
def Viernes(fecha):
    fecha= datetime.datetime.strptime(dfecha, "%d/%m/%Y")
    if (fecha.weekday() == 4):
        print (True)
    else:
        print (False)
    return fecha
print ("Ejercicio #3")
dfecha= input("Que fecha es hoy? (formato dd/mm/aaaa): ")
cfecha= Viernes(dfecha)
#4
import datetime
def Años(fecha):
    fecha2= (datetime.date(fecha.year,fecha.month,fecha.day))
    fecha3= datetime.date(fecha2.year+10, fecha2.month, fecha2.day)
    return ("{:%d (%A) %m %Y}".format(fecha3))
print ("Ejercicio #4")
cfecha=input("Cual es la fecha de hoy? (formato dd/mm/aaaa) ")
dfecha=datetime.datetime.strptime(cfecha, "%d/%m/%Y")
print (Años(dfecha))
#5
def imc(peso,estatura):
    return (peso/(estatura^2))
print ("Ejercicio #5")    
peso= input("Cuanto pesas (en kgs)? ")
estatura= (float(input("Cuanto mides en mts)? ")))
peso= int(peso)
estatura= int(estatura)
IMC= (imc(peso, estatura))
print ("Tu IMC es: {}".format(IMC))
#6
import math
def AreaCirculo(radio):
    return math.pi * (radio**2)
print ("Ejercicio #6")
radio = input ("Teclee el radio del circulo ")
area=(AreaCirculo(int(radio)))
print("El area del circulo es: {}".format(round(area,3)))
#7
def division(x):
    y= x/2
    
    if (y ==int (y)):
        return True
    else:
        return False
print ("Ejercicio #7")
print ("comprobacion con el 5")
print (division(5))
print ("comprobacion con el 4")
print (division(4))
#8
def division(x):
    y= x/3
    
    if (y ==int (y)):
        return True
    else:
        return False
print ("Ejercicio #8")    
print ("comprobacion con el 8")
print (division(8))
print ("comprobacion con el 9")
print (division(9))
#9
def division(x):
    y= x/3
    z= x/2
    if (((y) ==int (y)) and ((z)==int(z))):
        return True
    else:
        return False
print ("Ejercicio #9")
print ("comprobacion con el 12")
print (division(12))
print ("comprobacion con el 9")
print (division(9))
#10
def lista(l):
    return (sum(l)/len(l))
l= [1,5,1,2,7,5,4,7,1,4]
print ("Ejercicio #10")
print ("El promedio de los numeros [1,5,1,2,7,5,4,7,1,4] es de",(lista(l)))

