import smtplib
import email,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import src.analysis as an
import src.charts as ch
import getpass 
import os
from dotenv import load_dotenv
load_dotenv()


def send_email(text,text1):
    subject="¿Quieres saber más de los artistás más escuchados el 2019?"
    body = """\
    Hola,
    Adjunto vas a encontrar una gráfica con los 10 artistas con mayor numero de reproducciones en el 2019,estos son los datos  de cada artista: Nombre, Fecha de Nacimiento, Sexo, Ganancias: {text}
    estos son los datos personales de cada artista: Nacionalidad, Fecha de Nacimiento, Sexo, Streams: {text1}
    """
    sender_email = 'pruebaironhackmiriam@gmail.com'
    receiver_email = input("Enter destinatary_email:")
    password = p = getpass.getpass(prompt='Your password')

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    filename = "Top 10 most popularity Artists.png"
    with open("Output/Top 10 most popularity Artists.png", "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with  smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls() 
        server.login("sender_email", "password")
        server.sendmail("pruebaironhackmiriam@gmail.com", "receiver_email", "text")
        server.quit()
