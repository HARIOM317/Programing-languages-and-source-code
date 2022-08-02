import os
# Show all os module methods
print(dir(os))

# Show your current directory
print("My current working directory: ", os.getcwd())

# Show all files and folders of current directory
print("Files and Folders of current directory: ", os.listdir())

# Make a new folder in current directory
os.mkdir("My New Folder")

# Make folder in folder in folder....in current directory
os.makedirs("Folder_1/Folder_2/Folder3")

# Rename a file
os.rename("Hariom.txt", "HSR.txt")

# Join paths
print(os.path.join("D:", "/HSR"))

# Return true if path is exist otherwise return false
print("Path Exist: ", os.path.exists("C:/Program Files"))

# Return true if given path is a file otherwise return false
print("IsFile: ", os.path.isfile("C:/Program Files"))

# Return true if given path is a folder otherwise return false
print("IsDirectory: ", os.path.isdir("C:/Program Files"))

# Get environment variable
print("Environment Variable Path: ", os.environ.get('path'))

# Change your current directory
os.chdir("C:")
print("Now my current directory: ", os.getcwd())
print("Files and Folders of current directory: ", os.listdir())
