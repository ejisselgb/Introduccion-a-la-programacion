# Importar librerías
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Settings():
    @staticmethod
    def config_data():
        USERNAME_SMTP = "XXXXX"
        PASSWORD_SMTP = "XXXXX"
        HOST = "email-smtp.us-east-2.amazonaws.com"
        AWS_REGION = "us-east-2"
        PORT = 587

        return {
            "username_smtp": USERNAME_SMTP,
            "pasasword_smtp": PASSWORD_SMTP,
            "host": HOST,
            "region": AWS_REGION,
            "port": PORT
        }


class SendEmail():
    def __init__(self, sender, sendername, recipient, subject, message):
        self.sender = sender
        self.sendername = sendername
        self.recipient = recipient
        self.subject = subject
        self.message = message

    def send(self):
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = email.utils.formataddr((self.sendername, self.sender))
        msg['To'] = self.recipient

        message = MIMEText(self.message, 'plain')
        msg.attach(message)

        config = Settings().config_data()

        try:
            server = smtplib.SMTP(config['host'], config['port'])
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(config['username_smtp'], config['pasasword_smtp'])
            server.sendmail(self.sender, self.recipient, msg.as_string())
            server.close()
            print("Email enviado correctamente")
        except Exception as e:
            print("Error ", e)


send_email = SendEmail("erika.giselle.gb@gmail.com", "Erika Gutierrez", "erika.giselle.gb@gmail.com",
                       "Prueba correo estudiantes", "Esto es una prueba de correo para el trabajo final de los estudiantes")
send_email.send()
