import smtplib, ssl
import email.message
import os, sys

def sendMail(subject, body):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    with open(os.path.join(sys.path[0], "info.txt")) as f:
        lines = f.readlines()
        sender_email = lines[0]
        receiver_email = lines[1]
        password = lines[2]

    msg = email.message.Message()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_payload(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
    
    except:
        print("Error sending email with subject:" + subject)


