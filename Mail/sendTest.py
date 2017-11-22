import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text  import MIMEText

count = 0


# setting up the server
fromaddr = "shahad.nowhere@gmail.com"
print("Trying to log in")
server = smtplib.SMTP('smtp.gmail.com', 587)
print('.')
server.starttls()
print('.')
server.login(fromaddr, "ihacgdyaoysdhnfh")
print("Logged in")

toaddr = "1305022.si@ugrad.cse.buet.ac.bd"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = "shahad.nowhere@gmail.com"
msg['Subject'] = "Orientation class for the course "
body = 'this is the body'
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print(count)
