import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = input("What is your Gmail address? ")
password = input("What is your Gmail password? ")
msg = "Hello from your Python code!"

# a list of ID to send emails
recipient = ["xxx@email.com", "yyy@email.com"]

for i in range(len(recipient)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(email, password)
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient[i]
    msg['Subject'] = "Hello from your Python Code"
    body = "Hello from your Python Code"
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    s.sendmail(email, recipient[i], text)
    s.quit()
