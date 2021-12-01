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

while True:
   r = sr.Recognizer()
   with sr.Microphone() as source:
       r.adjust_for_ambient_noise(source,duration=1)
       currentTime = datetime.datetime.now()
       if currentTime.hour < 12:
          os.system("espeak-ng -s 140 'Good morning sir,I am Jarvis Please tell me how may I help you' ")
          audio= r.listen(source)
       
       elif 12 <= currentTime.hour < 18:
          os.system("espeak-ng -s 140 'Good Afternoon sir,I am Jarvis Please tell me how may I help you' ")
          audio= r.listen(source)
 
       elif 18 <= currentTime.hour < 19:
          os.system("espeak-ng -s 140 'Good evening sir,I am Jarvis Please tell me how may I help you' ")
          audio= r.listen(source)
   
       else:
           os.system("espeak-ng -s 140 'Good night sir,I am Jarvis Please tell me how may I help you' ")
           audio= r.listen(source) 

       try:
    
          text = r.recognize_google(audio)
          print(text)
          if 'time' in text:
             hour = datetime.datetime.now()
             print(hour)
             os.system(f"espeak-ng -s 140 'current date and time is {hour}' ")
       
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
                os.system("espeak-ng -s 130'Mail sended successfully'")
             except:
               os.system("espeak-ng -s 130'Mail not send'")
               
         
          elif 'news' in text:
          
             query = {
            "source":"bbc-news",
            "sortBy":"top",
            "apiKey":"8e19b13f4d674732b6fa9c425b2fdc45",
                }
             res = requests.get(" https://newsapi.org/v1/articles",params=query)
             news_dict = res.json()
             article = news_dict["articles"]
             results=[]
      
             for index, articles in enumerate(article):
             
                os.system(f"espeak-ng -s 130 '{articles['title']}' ")
      
                if index == len(article)-1:
                   
                   break
                os.system("espeak-ng -s 130'Moving on the next news headline..' ")
             os.system("espeak-ng -s 130'These were the top headlines, Have a nice day Sir!!..' ")
            
            
         
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
         
      
          

       except:
              os.system("espeak-ng -s 140 'Sorry sir i am not able to recognize you i am not connected to internet' ")


    
