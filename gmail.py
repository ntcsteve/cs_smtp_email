import smtplib

# declaring variables
email = input("What is your Gmail address? ")
password = input("What is your Gmail password? ")
recipient = input("What is the recipient's email address? ")
msg = "Hello from your Python code!"

# a new session using the SMTP function from the library smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.set_debuglevel(True)

# Initiate connection to the server
server.ehlo()

# Start encrypting everything you're sending to the server
server.starttls()

# Initiate connection to the server
server.ehlo()

# Log into the server by sending them our username and password
server.login(email, password)

# Send your email
server.sendmail(email, recipient, msg)

# Close the connection to the SMTP server
server.quit()
