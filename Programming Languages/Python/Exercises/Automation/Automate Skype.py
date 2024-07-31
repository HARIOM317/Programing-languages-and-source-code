from skpy import Skype

login = Skype("Enter Skype Account Id", "Password")

# Show all contact of Skype which are connected with you
contact = login.contacts
for i in contact:
    print(i)

# Send message of a person
contact = login.contacts["Enter live ID of a person"]
contact.chat.sendMsg("Type message here")

# Send Image
contact = login.contacts["Enter live ID of a person"]
with open("Image file location path", 'rb') as f:
    contact.chat.sendFile(f, "Image name", image=True)

# Create a group on skype
group = login.chats.create(["Enter live Id of person 1", "Enter live Id of person 2", "Enter live Id of person n"])
