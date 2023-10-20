import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server details (replace with your email provider's SMTP server)
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587

# Your email credentials
your_email = 'youremail@hotmail.com'
your_password = 'yourpassword'

# Recipient's email address
recipient_email = 'recipient@example.com'

# Create a connection to the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(your_email, your_password)

# Subject and message
subject = "Subject 1"
message_body = "This is the message body."

msg = MIMEMultipart()
msg['From'] = your_email
msg['To'] = recipient_email
msg['Subject'] = subject

message = message_body
msg.attach(MIMEText(message, 'plain'))

# Send the email
server.sendmail(your_email, recipient_email, msg.as_string())

# Quit the SMTP server
server.quit()
