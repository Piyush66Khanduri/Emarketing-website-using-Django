import smtplib
import secrets



'''server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('piyushkhanduri65@gmail.com','cetqiwemdeecvriq')
server.sendmail('piyushkhanduri65@gmail.com','piyushkhanduri65@gmail.com',"OTTP")
print("Email sent")'''

random_number = secrets.randbelow(99999) + 1
print("Secure random number:", random_number)