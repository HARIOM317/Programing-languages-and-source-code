import PyPDF2
a = PyPDF2.PdfFileReader("A:/My Notes/CMD Tutorial.pdf")
print(a.documentInfo)   # Get PDF Information
Pages = a.getNumPages()
print("Pages = ", Pages)  # Print number of pages of pdf

str = ""
for i in range(1, Pages):
    str += a.getPage(i).extractText()

with open("Text.txt", "w", encoding="utf-8") as f:
    f.write(str)