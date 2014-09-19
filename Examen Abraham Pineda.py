import datetime
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def cumple(edad):
    x=datetime.datetime.now().day
    edad=datetime.datetime.strptime(cfecha, "%d/%m/%Y")
    edad2= datetime.date(edad.year+(x), edad.month, edad.day)
    return ("{:%d (%A) %m %Y}".format(edad2))
cfecha=input("Cual es tu fecha de nacimiento? (formato dd/mm/aaaa) ")
dfecha=datetime.datetime.strptime(cfecha, "%d/%m/%Y")
print ("La fecha sumada es: ",(cumple(dfecha)))
fromaddr = "abramitesm@gmail.com"
toaddr = "ramon.ontiveros@itesm.mx"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Examen"
body = "La fecha sumada es: " + (cumple(dfecha))
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("abramitesm", "python12345")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("correo enviado, examen de 10 :D")
