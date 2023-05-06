import datetime
import time

end_time = datetime.datetime(2022, 3, 7)
site_block = ["www.wscubetech.com", "www.facebook.com"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect_number = "127.0.0.1"   # Open host file in notepad and copy localhost number

while True:
    if datetime.datetime.now() < end_time:
        print("Start Blocking the website...")
        with open(host_path, "r+") as hp:
            content = hp.read()
            for website in site_block:
                if website not in content:
                    hp.write(redirect_number+" "+website+"\n")
                else:
                    pass
    else:
        with open(host_path, 'r+') as hp:
            content = hp.read()
            hp.seek(0)
            for line in content:
                if not any(website in line for website in site_block):
                    hp.write(line)

            hp.truncate()   # Convert file into the original file by using truncate() function
        time.sleep(5)

