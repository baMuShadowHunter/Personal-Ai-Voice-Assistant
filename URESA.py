#! C:\Users\HYESHAN\Desktop\myaiproject\aienv\Scripts\python.exe
from multiprocessing.connection import answer_challenge
import pyttsx3
# from decouple import config
from datetime import datetime
import speech_recognition as sr
import os
import wikipedia
import webbrowser
from googlesearch import search
import requests
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv,dotenv_values
import pyautogui
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import sys
import time
# import openai
config = dotenv_values("perinfo.env")
paths = {
     'sublimenotepad' : "D:\\Apps\\Sublime\\Sublime Text 3\\sublime_text.exe",
     'Brave' : "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\Brave.exe"
 }

speak = pyttsx3.init('sapi5')
# print(speak)
voices = speak.getProperty('voices') 
speak.setProperty('rate',190)
speak.setProperty('volume',1000.0)
speak.setProperty('voice' , voices[0].id)

def Speak(Text):
	speak.say(Text)
	speak.runAndWait()

def wishme():
	time = datetime.now().hour
	if (time>=0) and (time<=12):
		Speak("Good morning Boss")
	elif (time>=12) and (time<=15):
		Speak("Good Afternoon Boss")
	else:
		Speak("Good Evening Boss")

def user_input():
	r = sr.Recognizer() 
	with sr.Microphone() as source:
		print('Listening.....')
		r.pause_threshold = 1
		audio = r.listen(source)
		
	try:
		print("Recognizing......")
		query = r.recognize_google(audio, language="en-in")
		print(f"User said: {query}\n")
		if not 'exit' in query or 'stop' in query:
			# Speak("Cool, I'm on it Boss,")
			# Speak("Okey Boss,I'm working on it")
			# Speak("Just a Secnd Boss")
			Speak("yes boss")
		else:
			time = datetime.now().hour
			if (time >= 21) and (time < 6):
				Speak("Good night Boss,Take care")
			else:
				Speak("Have a good day Boss, bye")
			exit()
	except Exception:
		Speak("sorry Boss,I dont Understand. please say Again? ")
		query = 'None'
	return query
def open_sublime():
	os.startfile(paths['sublimenotepad'])
def open_Brave():
	os.startfile(paths['Brave'])
def play_on_youtube(video):
	kit.playonyt(video)
def send_whatsapp_message(number, message):
	kit.sendwhatmsg_instantly(f"+91{number}",message)
EMAIL = config["EMAIL"]
PASSWORD = config["PASSWORD"]
def send_email(receiver_address, subject, message):
	try:
		email=EmailMessage()
		email['To'] = receiver_address
		email["Subject"] = subject
		email["From"] = EMAIL
		email.set_content(message)
		s = smtplib.SMTP("smtp.gmail.com", 587)
		s.starttls()
		s.login(EMAIL,PASSWORD)
		s.send_message(email)
		s.close()
		return True
	except Exception as e:
		print(e)
		return False
OPENWEATHER_APP_ID = config["OPENWEATHER_APP_ID"]
def getweather(city):
	res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=&appid={OPENWEATHER_APP_ID}&units=metric").json()
	weather = res['weather'][0]['main']
	temperature = res['main']['temp']
	feels_like = res['main']['feels_like']
	return weather,f"{temperature}`C",f"{feels_like}`C"
def find_my_ip():
	ip_address = requests.get("https://api64.ipify.org?format=json").json()
	return ip_address["ip"]
def intro_myself():
	Speak("Welcome boss")
	Speak("Hi,Now me to intruduce my self I am URESA")
	Speak("I am artificial intaligent virtual voice assistend")
	Speak("I am here to assist you varity of tasks best On 24 hours of a day,7 days of week")
	Speak("Import your preferance in home into places")
	Speak("System is fully operational")
	Speak(" How can i help you, naan uuingalukku enna seyya vendum")
def intro_myselff():
	Speak("Hi,Now me to intruduce my self I am URESA")
	Speak("I am artificial intaligent virtual voice assistend")
	Speak("I am here to assist you varity of tasks best On 24 hours of a day,7 days of week")
	Speak("Import your preferance in home into places")
	Speak("System is fully operational")
	Speak(" How can i help you, naan uuingalukku enna seyya vendum")
NEWS_API_KEY = config["NEWS_API_KEY"]
def getlatestnews():
	news_headlines = []
	res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
	articles = res["articles"]
	for article in articles:
		news_headlines.append(article["title"])
	return news_headlines[:5]

TMDB_API_KEY = config["TMDB_API_KEY"]
def gettrendingmovies():
	trending_movies = []
	res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
	results = res["results"]
	for r in results:
		trending_movies.append(r["original_title"])
	return trending_movies[:5]

def getrandomjoke():
	headers = { 'Accept': 'application/json' }
	res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
	return res["joke"]

def getrandomadvice():
	res = requests.get(f"https://api.adviceslip.com/advice").json()
	return res['slip']['advice']


if __name__ == '__main__':
	wishme()
	intro_myself()
	while True:
		query = user_input().lower()
		if 'wake up' in query or 'wake' in query:
			Speak("Say me anything i give it for you")
			while True:
				query = user_input().lower()
				if 'open sublime' in query:
					open_sublime()
				elif 'open Brave' in query:
					open_Brave()
				elif 'open cmd'in query or 'open command prompt' in query:
					os.system("start cmd")
				elif 'open youtube' in query:
					webbrowser.open("youtube.com")
				elif 'open whatsapp' in query:
					webbrowser.open("whatsappweb.com")
				elif 'open google' in query:
					webbrowser.open("google.com")
				elif 'wikipedia' in query:
					Speak("Searching wikipedia.....")
					query=query.replace("wikipedia","")
					answer=wikipedia.summary(query,sentences=2)
					Speak("According to the wikipidia")
					# print(answer)
					Speak(answer)
				elif 'time' in query:
					strtime = datetime.now().strftime("%H:%M:%S")
					print(strtime)
					Speak(f"Boss the time is{strtime}")
				elif 'search google' in query:
					Speak("what you want to search in google Boss?")
					query=user_input().lower()
					Speak("Searching Google")
					for i in search(query, tld="co.in", num=10, stop=1, pause=2):
						print(i)
					Speak("Search results on Google")
					Speak("open in browser")
					webbrowser.open(i)
				elif 'search youtube'in query:
					Speak("what you want you search or play in youtube")
					video = user_input().lower()
					play_on_youtube(video)
				elif 'send whatsapp message' in query:
					Speak("what nunber should i snd the message?, please enter the number in the console:")
					number  = input("Enter the Whatsapp Number")
					Speak("What is the message Boss?")
					message = user_input().lower()
					send_whatsapp_message(number, message)
					Speak("I have sent the message")
				elif 'send email' in query:
					Speak("on what email do i send Boss?plese enter in the console")
					receiver_address = input("Enter the Email")
					Speak("What should be the subject Boss?")
					subject = user_input().capitalize()
					Speak("What is the message Boss?")
					message = user_input().capitalize()
					if send_email(receiver_address, subject, message):
						Speak("I hae send the Email Boss")
					else:
						Speak("Something is went wrong while I was sending the mail. please check the error lods Boss.")
				elif 'weather' in query:
					try:
						ip_address = find_my_ip()
						city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
						Speak(f"Getting weather report for your city {city}")
						weather, temperature, feels_like = getweather(city)
						Speak(f"The current tepreture is {temperature},but it feels like{feels_like}")
						Speak(f"Also , The weather report talks about{weather}")
						Speak("For your convenience, I am printing it on the screen Boss")
						print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
					except Exception:
						Speak("Boss some error to find the weather")
				elif 'my ip address' in query:
					ip_address = find_my_ip()
					Speak(f"your IP Address is {ip_address}.\n For your convenience, I am printing on the Screen Boss")
					print(f"your IP Address is {ip_address}")
				elif 'temperature' in query:
					#query = user_input().lower()
					url = f"https://www.google.com/search?q={query}"
					r = requests.get(url)
					data = BeautifulSoup(r.text,"html.parser")
					temp = data.find("div",class_="BNeawe").text
					Speak(f"current{query} is {temp}")
				elif 'activate how to make mode' in query:#this mode is activated in anything you want to make ai is instruct you
					Speak("How to make mode is activated")
					while True:
						Speak("please tell me what you want to know Boss")
						query = user_input()
						try:
							if "exit" in query or "close" in query:
								Speak("okey Boss,how make mode closed")
								break
							else:
								max_results = 1
								how_to = search_wikihow(query, max_results)
								assert len(how_to) == 1
								how_to[0].print()
								Speak(how_to[0].summary)
						except Exception as e:
							Speak("sorry Boss, I am not able to find this")
				elif 'news' in query:
					Speak(f"I'm reading out the latest news headlines Boss ")
					speak.setProperty('rate',130)
					Speak(getlatestnews())
					Speak("For your convenience I am printing it on the Screen Boss.")
					print(*getlatestnews(), sep='\n')
				elif 'trending movies' in query:
					Speak(f"Some of the trending movies are:{gettrendingmovies()}")
					Speak("For your convenience I am printing it on the Screen Boss.")
					print(*gettrendingmovies(), sep='\n')
				elif 'joke' in query:
					Speak("Hope you like this one Boss")
					joke = getrandomjoke()
					Speak(joke)
					Speak("For convenience I am printing it on the Screen Boss.")
					print(joke)
				elif 'advice' in query:
					Speak("Here's an advice for you Boss")
					advice = getrandomadvice()
					Speak(advice)
					Speak("For your convenience I am printing it on the Screen Boss.")
					print(advice)
				elif 'search apps' in  query or 'open apps' in query or 'open app' in query:
					Speak("What you want search or open app in pc Boss")
					pyautogui.keyDown('win')
					pyautogui.press('s')
					pyautogui.keyUp('win')
					print("Please Tell me the app Boss")
					app = user_input()
					for i in app:
						pyautogui.press(i)
					pyautogui.press('enter')
				elif 'save' in query:
					pyautogui.keyDown('ctrl')
					pyautogui.press('s')
					pyautogui.keyUp('ctrl')
				elif 'close' in query:
					pyautogui.keyDown('alt')
					pyautogui.press('f4')
					pyautogui.keyUp('alt')
				elif 'minimize' in query or 'minimise' in query:
					pyautogui.keyDown('win')
					pyautogui.press('down')
					pyautogui.press('down')
					pyautogui.keyUp('win')
				elif 'maximize' in query:
					pyautogui.keyDown('win')
					pyautogui.press('up')
					pyautogui.press('up')
					pyautogui.keyUp('win')
				elif 'open' in query:
					pyautogui.keyDown('ctrl')
					pyautogui.press('o')
					pyautogui.keyUp('ctrl')
				elif 'copy' in query:
					pyautogui.keyDown('ctrl')
					pyautogui.press('c')
					pyautogui.keyUp('ctrl')
				elif 'paste' in query:
					pyautogui.keyDown('ctrl')
					pyautogui.press('v')
					pyautogui.keyUp('ctrl')
				elif 'cut' in query:
					pyautogui.keyDown('ctrl')
					pyautogui.press('x')
					pyautogui.keyUp('ctrl')
				elif 'new' in query:
					pyautogui.keyDown('ctrl')
					pyautogui.press('n')
					pyautogui.keyUp('ctrl')
				elif 'scroll up' in query or 'move up' in query:
					pyautogui.press('up')
					pyautogui.press('up')
					pyautogui.press('up')
				elif 'scroll down' in query or 'move down' in query or 'scroll' in query :
					pyautogui.press('down')
					pyautogui.press('down')
					pyautogui.press('down')
				elif 'press win key' in query or 'press window key' in query:
					pyautogui.press('win')
				elif 'type' in query:
					typ=user_input()
					for i in typ:
						pyautogui.press(i)
				elif 'wait' in query or 'sleep' in query or 'stay' in query:
					Speak("How many minute have wait please tell me")
					query = user_input()
					if 'wait 1 minutes' or 'wait 1 minute' in query:
						time.sleep(60)
						Speak("i'm wake up Boss")
					elif 'wait 2 minutes' or 'wait 2 minute' in query:
						time.sleep(120)
						Speak("i'm wake up Boss")
					else:
						exit()
				elif 'introduce your self' in query or 'intro your self' in query or 'introduce yourself' in query:
					intro_myselff()
				elif 'what is your name' in query or 'your name' in query or 'name' in query:
					Speak("My Name is Uresa")
				elif 'how are you' in query or 'ni eppadi erukka' in query:
					Speak("I'm fine boss what about you boss")
				elif 'fine' in query:
					Speak("what i do for you Boss")
				elif 'type' in query:
					Speak("i am type in screen Boss")
					for i in query:
						pyautogui.press(i)
				else:
					Speak("i don't understand this is out of my limite Boss")

		else:
			Speak("i'm dont wake up Boss please say Again in wake up")

				


						


				











              