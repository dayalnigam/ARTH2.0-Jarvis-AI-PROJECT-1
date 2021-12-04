import speech_recognition as sr  
import datetime
import requests
from bs4 import BeautifulSoup
import json
import os
import smtplib
from email.message import EmailMessage
from smtplib import SMTPException
import time


def time_of_day(hour):
      """
      Returns one of 'morning' | 'afternoon' | 'evening' | 'night'
      
      Usage Example:
      >>> time_of_day(10)     # 10 a.m.
      morning
      >>> time_of_day(12)     # 12 p.m.
      afternoon
      >>> time_of_day(17)     # 5 p.m.
      evening
      >>> time_of_day(20)     # 8 p.m.
      night
      """
      
     assert 0 <= hour < 24, f"Invalid hour {hour}: should be in range [0,23]"
     if hour < 12:
         return 'morning'
     elif hour < 16:           # it was previously 18 - but I think that 6 p.m. is too late for afternoon
         return 'afternoon'
     elif hour < 19:
         return 'evening'
     return 'night'


def speak(message, words_per_minute=140):
   """
   Speaks message through microphone.
   
   Example Usage:
   >>> speak('Hello World')    # using default words per minute (140)
   >>> speak('Custom Words per minute', words_per_minute=130)
   """
   os.system(f'espeak-ng -s {words_per_minute} {message}')


while True:
   r = sr.Recognizer()
   with sr.Microphone() as source:
       r.adjust_for_ambient_noise(source,duration=1)
       currentTime = datetime.datetime.now()
       speak(f'Good {time_of_day(currentTime.hour)} sir,I am Jarvis. Please tell me how may I help you.')
       audio = r.listen(source)
      
       try:
          text = r.recognize_google(audio)
          print(text)
          if 'time' in text:
             hour = datetime.datetime.now()
             print(hour)
             speak(f'current date and time is {hour}')
       
          elif 'email' in text:
             try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('hulasnigam@gmail.com', 'dayalbaghradhasoami')
                email = EmailMessage()
                email['From'] = 'hulasnigam@gmail.com'
                email['To'] = "hulasnigam@gmail.com"
                email['Subject'] = "Hi"
                email.set_content("Hi")
                server.send_message(email)
                speak('Mail sended successfully')
             except SMTPException as e:
                speak(f'Mail could not be sent due to error {e}')
               
         
          elif 'news' in text:
             query = {
               "source":"bbc-news",
               "sortBy":"top",
               "apiKey":"8e19b13f4d674732b6fa9c425b2fdc45",
             }
             res = requests.get("https://newsapi.org/v1/articles",params=query)
             news_dict = res.json()
             articles = news_dict["articles"]
      
             for article in articles:
                speak(article['title'])
                speak('Moving on the next news headline..')
             speak('These were the top headlines, Have a nice day Sir!!..')
            
          elif 'fun' in text:
             os.system("sl")
             time.sleep(5)
             os.system("asciiquarium")
             time.sleep(5)
             os.system("cowsay 'Hi Vimal sir Hi ARTH LERNERS' ")

          elif 'docker' in text:
              os.system("systemctl start docker")
              r = sr.Recognizer()
              with sr.Microphone() as source:
                  r.adjust_for_ambient_noise(source,duration=2)
                  audio = r.listen(source)
                  image = r.recognize_google(audio)
                  os.system(f"docker pull {image}")
                  print("image pulled")
                  os.system(f"docker run -it {image}")
              os.system("systemctl stop docker")  

          elif 'stop' in text:
             break
         
       except OSError:
              speak('Sorry sir i am not able to recognize you as I am not connected to the internet')


    
