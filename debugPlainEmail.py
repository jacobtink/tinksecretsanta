import smtplib, ssl, csv

port = 1025
smtp_server = "localhost"
sender_email = "my@gmail.com"
receiver_email = "testing@gmail.com"

message = """\
Subject: Hi there {name}

This message is sent from Python to {email}. You are {secret}'s secret santa!"""

#password = input("Enter password: ")

#context = ssl.create_default_context()

print("trying to connect")

with open("contacts_file.csv") as file:
	reader = csv.reader(file)
	next(reader) # skip header row
	for name, email, secret in reader:
		print(f"Sending email to {name}")
		try:
			server = smtplib.SMTP(smtp_server, port)
			server.ehlo()		
			server.sendmail(sender_email, email, message.format(name=name, email=email, secret=secret))
		except Exception as e:
			print(e)
		finally:
			server.quit()

"""
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	print("connected to server")
	#server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email, message)
"""
