
import smtplib
from email.message import EmailMessage
import os

def enviar_pdf(destinatario, archivo_pdf):
    remitente = "tuservicio@example.com"
    asunto = "Tu novela digital protegida"
    cuerpo = "Gracias por tu compra. Adjuntamos tu novela digital protegida con contraseña."

    msg = EmailMessage()
    msg['Subject'] = asunto
    msg['From'] = remitente
    msg['To'] = destinatario
    msg.set_content(cuerpo)

    with open(archivo_pdf, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=os.path.basename(archivo_pdf))

    print(f"Email preparado para enviar a {destinatario} con el archivo {archivo_pdf}.")
