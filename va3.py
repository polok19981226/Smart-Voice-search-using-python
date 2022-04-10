import pyttsx3
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import time




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
	engine.say(audio)
	engine.runAndWait()


	

def usrname():
	speak("What should i call you")
	uname = takeCommand()
	speak("Welcome")
	speak(uname)
	speak("How can i Help you")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.") 
		return "None"
	
	return query



if __name__ == '__main__':

	
	usrname()
	
	while True:
		
		query = takeCommand().lower()
		
		
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 1)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stack overflow' in query:
			speak("Here you go to Stack Over flow")
			webbrowser.open("stackoverflow.com") 

		
		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")


		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak("voice assistant")
			print("My friends call me Voice Assistant")

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query: 
			speak("I have been created by Polok.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "") 
			query = query.replace("play", "")		 
			webbrowser.open(query) 

		elif "who i am" in query:
			speak("If you talk then definately your human.")

		elif "why you came to world" in query:
			speak("Thanks to Polok. further It's a secret")

		elif "who are you" in query:
			speak("I am your voice assistant created by Polok")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by polok ")

		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

			

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query: 
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")

		elif "i love you" in query:
			speak("Are you sure?")
		