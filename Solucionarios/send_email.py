########################################################### NO MODIFICAR #####################################################################

# Importar librerías
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Se crea clase para las configuraciones estaticas que permitirán el envio de correos


class Settings():
    # Método con valores estáticos de configuración
    # Se retorna la información con las credenciales.
    # SOLO MODIFICAR USERNAME_SMTP Y PASSWORD_SMTP CON LOS VALORES ENTREGADOS POR TEAMS
    @staticmethod
    def config_data():
        # REEMPLAZAR POR VALORES ENTREGADOS VÍA TEAMS - NO SUBIR ARCHIVO CON CREDENCIALES AL REPOSITORIO
        USERNAME_SMTP = "XXXXX"
        # REEMPLAZAR POR VALORES ENTREGADOS VÍA TEAMS - NO SUBIR ARCHIVO CON CREDENCIALES AL REPOSITORIO
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

# Se crea clase para el envio de correo que recibe un emisor, nombre de quien envia, remitente, titulo del mesanje y mensaje en texto plano


class SendEmail():
    # Constructor para recibir parámetros al momento de inicializar la clase
    def __init__(self, sender, sendername, recipient, subject, message):
        self.sender = sender
        self.sendername = sendername
        self.recipient = recipient
        self.subject = subject
        self.message = message

    # Método encargado del envío del mensaje
    # NO REEMPLAZAR NADA AQUÍ
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

########################################################## NO MODIFICAR HASTA AQUÍ #######################################################3


# Se invoca la clase y se le otorgan los parámetros necesarios para el envío de correo
# Usted solo deberá implementar una línea parecida a esta, no modificar nada de la clase Settings y de la clase SendEmail
# Solo en settings deberá cambiar los valores para las variables USERNAME_SMTP, PASSWORD_SMTP
# Recuerda proporcionar los dos emails uno para emisor y otro para receptor
# Estructura: emisor, nombre emisor, remitente, titulo correo, mensaje correo


########## DESCOMENTAR ESTAS LINEAS SI VAS A COPIAR Y PEGAR EL VALOR O CONTENIDO DE ESTA CLASE EN TU PROYECTO #################
#send_email = SendEmail("erika.giselle.gb@gmail.com", "Erika Gutierrez", "erika.giselle.gb@hotmail.com", "Prueba correo estudiantes", "Esto es una prueba de correo para el trabajo final de los estudiantes")
#send_email.send()
