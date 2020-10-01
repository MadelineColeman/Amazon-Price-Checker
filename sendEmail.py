import smtplib

subject = "Amazon Price Alert"
body = "check the link"
msg = f"Subject: {subject},\n\n{body}"

server = smtplib.SMTP('smtp.gmail.com',587)
server.connect('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("maddyc193@gmail.com", "helloWorld123")
server.sendmail("maddyc193@gmail.com","maddyc193@gmail.com",msg)
server.quit()