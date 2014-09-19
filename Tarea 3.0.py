#1
def non(x):
    if(x%2 == 0):
        return False
    else:
        return True
print ("Ejercicio #1")
x= (float(input("Escribe un numero, si es par sera Falso y si es non sera Verdadero: ")))
print (non(x))
#2
def binario(num):
    num = int(num)& 1
    if (num == 1):
        return True
    else:
        return False
print ("Ejercicio #2")
num= input("Escribe un numero, si es par sera Falso y si es non sera Verdadero: ")
print (binario(num))
#3
def mayus(x):
    return x.title()
print ("Ejercicio #3")
x=input("Escribe una oracion en minisculas:")
print (mayus(x))
print ("Que tal eeeh?")
#4
import random
def bala():
    turno=0
    muerte=3
    vida= 1
    while (turno<8) and (vida==1):
        turno+=1
        balas= random.randint(1,6)
        if(balas==3):
            print("Moriste en el turno:",turno)
            vida=0
    if (vida==1):
        print("Ganaste!!!")
    else:
        print("Game Over")
print ("Ejercicio #4")
print("Veamos si sobrevives a la ruleta rusa")
bala()
#5
import math
def lado(base, ang):
    rad=math.radians(ang)
    tan=math.tan(rad)
    resultado= base * tan
    return resultado
print ("Ejercicio #5")
print ("Vamos a sacar el lado opuesto de un triangulo rectangulo")
base= (float(input("Que lado tiene la  base?: ")))
ang= (float(input("Que angulo tiene el vertice B?: ")))
print (lado(base, ang))

#6
import statistics
def desv():
    x= [1.5,2.5,2.5,3.75,3.25,4.75]
    return print("La Desviacion Estandar de [1.5,2.5,2.5,3.75,3.25,4.75] es:",statistics.stdev(x))
print ("Ejercicio #6")
desv()
#7
import multiprocessing
def proc():
    x=multiprocessing.cpu_count()
    if(x>=2):
        print("Tienes una super computadora")
    else:
        print("Le falta galleta a tu computadora")
print ("Ejercicio #7")
print ("Veamos que tan chida es tu compu")
proc()

#8
def oper(x):
    return x
print ("Ejercicio #8")
x=input("Escribe una operacion matematica: ")
print (eval(x))
#9
import tkinter 
import tkinter.filedialog
def nombre():
    name= tkinter.filedialog.askopenfilename()
    return print(name)
print ("Ejercicio #9")
print ("Escoge un archivo para ver su direccion")
nombre()
#10
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def mail():
    fromaddr = "abramitesm@gmail.com"
    toaddr = "ramon.ontiveros@itesm.mx"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Tarea 5 ejercicio 6"
    body = "Mensaje enviado desde " + (socket.gethostname())
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("abramitesm", "python12345")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
print ("Ejercicio #10")
mail()
print ("Le ha llegado un correo nuevo a ramon.ontiveros@itesm.mx" )
print ("FIN, deme un 10 profe :D")
