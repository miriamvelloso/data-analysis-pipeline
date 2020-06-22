import smtplib
import email,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from analysis import *
from charts import *


def send_email(text):
    subject="¿Quieres saber más de los artistás más escuchados el 2019?"
    body = """\
    Hola,
    Adjunto vas a encontrar una gráfica con los 10 artistas con mayor numero de reproducciones en el 2019,estos son los datos  de cada artista: Nombre, Fecha de Nacimiento, Sexo, Ganancias: {text}
    """
    sender_email = input("Enter sender_email:")
    receiver_email = input("Enter destinatary_email:")
    password = input("Enter password:")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    filename = "Top 10 most popularity Artists.png"
    with open(Output/filename, "rb") as attachment:
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
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)