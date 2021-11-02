import smtplib, ssl, csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

testServerEnabled = True # change to true if you want to work forwards a SMPT Test-server

sender_email = "secretsanta.tink@gmail.com"
#receiver_email = "your@gmail.com"

if(not testServerEnabled):
    password = input("Type your password and press enter:")

message = MIMEMultipart("alternative")
message["Subject"] = "Your Secret Santa"
message["From"] = sender_email

# Create the plain-text and HTML version of your message

text = """\
Hi there {name}
This message is sent from Python to {email}. You are {secret}'s secret santa!
This should be the plaintext-version"""

text = """\
Hi,
How are you?"""
html = """\
<html>
  <body>
    <p>Hi there {name}<br>
       This message is sent from Python to {email}. You are {secret}'s secret santa!<br>
       This should be the html-version
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

if(testServerEnabled):
    with open("contacts_file.csv") as file:
    	reader = csv.reader(file)
    	next(reader) # skip header row
    	for name, email, secret in reader:
    		try:
    			server = smtplib.SMTP("localhost", 1025)
    			server.ehlo()		
    			server.sendmail(sender_email, email, message.as_string().format(name=name, email=email, secret=secret))
    		except Exception as e:
    			print(e)

if(not testServerEnabled):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        with open("contacts_file.csv") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for name, email, secret in reader:
            
                message["To"] = email
            
                server.sendmail(
                    sender_email,
                    email,
                    message.as_string().format(name=name, email=email, secret=secret),
                )
