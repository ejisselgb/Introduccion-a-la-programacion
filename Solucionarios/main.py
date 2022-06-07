# IMPLEMENTE DE ESTA MANERA PARA EVITAR COPIAR Y PEGAR EL CÓDIGO
# PONGA LA CLASE SEND_EMAIL.PY EN LA MISMA UBICACIÓN DE SU ARCHIVO PRINCIPAL
# AGREGUE LA IMPORTACIÓN AL SCRIPT QUE ESTÁ UTILIZANDO PARA HACER LAS CONVERSIONES DE LAS CADENAS
from send_email import SendEmail


if __name__ == '__main__':
    # IMPLEMENTE ESTAS LINEAS EN SU ARCHIVO PRINCIPAL
    send_email = SendEmail("erika.giselle.gb@gmail.com", "Erika Gutierrez", "erika.giselle.gb@hotmail.com",
                           "Prueba correo estudiantes", "Esto es una prueba de correo para el trabajo final de los estudiantes")
    send_email.send()
