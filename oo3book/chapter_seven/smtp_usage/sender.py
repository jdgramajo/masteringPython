import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, *to_addr, host="localhost",
    port=1025, **headers):

    headers = {} if headers is None else headers
    email = MIMEText(message)
    email['Sender'] = subject
    email['From'] = from_addr
    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addr:
        del email['To']
        email['To'] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()
