import os

def prettify_folder(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i} Image{format}")
            i += 1

prettify_folder(r"A:\Python Tutorial\Exercises\pretify_the_folder",
                r"A:\Python Tutorial\Exercises\pretify_the_folder\hariom.txt", ".jpg")