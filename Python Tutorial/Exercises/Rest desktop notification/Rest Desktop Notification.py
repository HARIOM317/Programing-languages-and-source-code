from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(title=">>> Take Rest",
                            message="Rest is vital for better mental health.",
                            app_icon="Rest.ico",
                            timeout=5)

        time.sleep(60 * 60)

# Note:- Type pythonw filename.py in terminal to running this program in background
