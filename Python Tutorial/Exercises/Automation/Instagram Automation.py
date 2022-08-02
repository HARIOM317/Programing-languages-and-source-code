from instabot import Bot
bot = Bot()

# Login your instagram account
bot.login(username="Type_Username_Here", password="Enter Password here")

# Follow a person
bot.follow('Enter username whom you want to follow')

# Upload a photo
bot.upload_photo("D:/photos/My photos/HSR.jpg", caption="Keep Coding, Keep Learning")

# Unfollow a person
bot.unfollow("Enter username whom you want to unfollow")

# Message multiple persons at once
bot.send_message("Type your message here", ["User_name-1", "Usr_name-2", "User_name-3", "User_name-n"])

# Show your all instagram followers
followers = bot.get_user_followers("Enter your user name")
for follower in followers:
    print(bot.get_user_info(follower))

# Show your all instagram following
Followings = bot.get_user_following("Enter your user name")
for following in Followings:
    print(bot.get_user_info(Followings))

