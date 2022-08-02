import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("Hello! Good Morning. Here is the top 10 latest sport's news for you.")
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=bcfbe6f7612746c58e64c1e613af0204"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    news_no = 1
    for article in arts:
        if news_no > 10:
            break

        elif news_no == 10:
            print(f"News {news_no} : {article['description']} \n")
            print(f"For more information click on the given link below: \n {article['url']} \n")
            speak(f"The last news is: ")
            speak(article['description'])

        else:
            print(f"News {news_no} : {article['description']} ")
            print(f"For more information click on the given link below: \n {article['url']} \n")
            speak(f"The news number {news_no} is: ")
            speak(article['description'])
            speak("Now, moving on the next news. Listen carefully!")
        news_no = news_no + 1

speak("Thanks for listening all news. Have a nice day.")
