
#Enlaces de configuración
#https://accounts.google.com/DisplayUnlockCaptcha
#https://www.google.com/settings/security/lesssecureapps
  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
  
class SendEmail():
    def __init__(self, password, fromEmail, toEmail, subject, message):
        self.password = password
        self.fromEmail = fromEmail
        self.toEmail = toEmail
        self.subject = subject
        self.message = message
    
    def send(self):
        message = self.message
        # create message object instance
        msg = MIMEMultipart()
        msg.attach(MIMEText(message, 'plain'))
        password = self.password
        msg['From'] = self.fromEmail
        msg['To'] = self.toEmail
        msg['Subject'] = self.subject

        server = smtplib.SMTP('smtp.gmail.com: 587')
  
        server.starttls()
  
        server.login(msg['From'], password)
  
        server.sendmail(msg['From'], msg['To'], msg.as_string())
  
        server.quit()
  
        print("successfully sent email to %s:" % (msg['To']))

sendmail = SendEmail("clave", "erika.giselle.gb@gmail.com", "erika.giselle.gb@gmail.com", "Test", "Aqui mandar datos")
sendmail.send()
