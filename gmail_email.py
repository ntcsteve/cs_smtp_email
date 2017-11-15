import smtplib

# email package contains many classes and functions for composing and parsing email messages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = input("What is your Gmail address? ")
password = input("What is your Gmail password? ")
toaddr = input("What is the recipient's email address? ")

# setting headers as a keyword dictionary
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Hello from your Python Code"

body = "Hello from your Python Code"

# attach the body of the email to the MIME message:
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
