import smtplib
import ssl


CORREO = "carlosvaldez0518@gmail.com"

CONTRASENA = "proyecto"


print("Conectando con Gmail...")

contexto = ssl.create_default_context()

try:

    servidor = smtplib.SMTP(
        "smtp.gmail.com",
        587,
        timeout=30
    )

    print("Conexion TCP correcta.")

    servidor.ehlo()

    print("EHLO correcto.")

    servidor.starttls(
        context=contexto
    )

    print("STARTTLS correcto.")

    servidor.ehlo()

    print("Intentando iniciar sesion...")

    servidor.login(
        CORREO,
        CONTRASENA
    )

    print("INICIO DE SESION CORRECTO.")

    servidor.quit()

except Exception as error:

    print("ERROR:")

    print(
        repr(error)
    )