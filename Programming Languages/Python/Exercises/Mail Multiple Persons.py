import smtplib as s

obj = s.SMTP('smtp.gmail.com', 587)
obj.ehlo()
obj.starttls()
obj.login("Your Email", "Password")     # it is recommended to use password by using another file.

# Note: less secure app should br turned on of your gmail account for this.
print("Login successfully...")
subject = "Type Subject"
body = "Body of the message."
massage = "subject: {}\n\n{}".format(subject, body)
list_address = ["Email address 1",
                "Email address 2",
                "Email address 3",
                "Email address 4",
                "Email address n",
                ]
obj.sendmail("Sender mail address", list_address, massage)
print("Mail send successfully!")
obj.quit()      # Close the server.
