#Program to send an email to my friend

#Importing smtp library package
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)

#start TLS for security
s.starttls()

#Authentication
s.login("***********@gmail.com", "****#$!&%")

#Message to be sent
message = "Hey ,how r u?...."

#Sending an email
s.sendmail("***********@gmail.com" , "!####!!!!!!!$$$$$*&#@gmail.com", message)
print("Message has been sent")
print("Hope u had an intresting time with us..........")
#Terminating the session
s.quit()

s