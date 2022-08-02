import os

def create_if_not_exist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

if __name__ == '__main__':
    files = os.listdir()
    files.remove('Autometic folder cleaner.py')
    print(files)

    create_if_not_exist('Images')
    create_if_not_exist('Docs')
    create_if_not_exist('Media')
    create_if_not_exist('Other')

    imgExts = [".png", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt", ".docx", ".doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts = [".mp3", ".mp4", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)

    move("Media", medias)
    move("Docs", docs)
    move("Images", images)
    move("Other", others)
