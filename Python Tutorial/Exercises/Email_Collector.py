import re

str = '''

Video provides a powerful way hdr453@outlook.com to help you prove your point. 
When you click Online Video, you can paste in GoodBoy@Hotmail.com the embed code for the video you want to add. 
You can also type a keyword to search online for krish3@gmail.com the video that best fits your document. 
To make your document look professionally produced, Word provides header, footer, cover page, and text box on spiderman10@hsr.com and designs that complement each other. 
For example, you can add a matching cover page on Myemail210@hotmail.com, header, and sidebar.
Click on hsr1000@github.com for Insert and then choose the elements you want from the different galleries. 
Themes and styles also help keep your document coordinated on hunny_bunny@gamil.com.
When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change mypc@nothing.com to match your new theme. 
When you apply styles, your headings change to match the new theme. Save time in Word with new buttons that show up where you need them.
To change the way a picture fits in your document, click it and a button for layout options appears next to it. 
When you work on a table, click where you want to add a row or a column, and then click the plus sign. Reading is easier, too, in the new Reading view. 
You can collapse parts of the document and focus on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on another device.
Video provides a powerful way to help you prove your point. When you click on Akshaykumar@gmail.com Online Video, you can paste in the embed code for the video you want to add. 
You can also type a keyword to search online for the video that best fits your document. To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. 
For example, you can add a matching cover page, header, and sidebar.
Click Insert and then choose the elements on Modiji@sarkar.com you want from the different galleries. 
Themes and styles hariom@gmail.com, hsr001@gmail.com also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme. 
Save time in Word with mygoverment@gov.in new buttons that show up where you need them.

'''

# Email = re.findall(r"[0-9a-zA-Z._%]+@[0-9a-zA-Z._%]+[.][a-zA-z.0-9]+", str)
#           __________OR__________
# Here:  \w -->  find a-z, A-Z, and 0-9
# and    \S -->  find space
Email = re.findall(r'\w+@\S+\w', str)
# print(Email)
print("Emails are available in given paragraph: \n")
for i in Email:
    print(i)
