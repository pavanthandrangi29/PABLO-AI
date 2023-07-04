import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import openai
from config import apikey
import random
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
chatStr=""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr+=f"Pavan: {query}\n Pablo: "

    
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=chatStr,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    #wrap inside try catch block
    speak(response["choices"][0]["text"])
    chatStr+=f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
    

    #with open(f"Openai/prompt- {random.randint(1, 234567)}", "w") as f:
    with open(f"Openai/{ ''.join(prompt.split('intelligence')[1:])}.txt","w") as f:
        f.write(text)


def ai(prompt):
    openai.api_key = apikey

    text=f"openAI response for Prompt: {prompt} \n *************\n\n"
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    #wrap inside try catch block
    print(response["choices"][0]["text"])
    text+=response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    #with open(f"Openai/prompt- {random.randint(1, 234567)}", "w") as f:
    with open(f"Openai/{ ''.join(prompt.split('intelligence')[1:])}.txt","w") as f:
        f.write(text)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!!")
    else:
        speak("Good evening!!")
    speak("I AM PABLO SIR. PLEASE TELL ME HOW MAY I HELP YOU")   

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)  

    try:
    
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        #print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "some error occured. sorry from PABLO" #None string will be returned
    return query               

     

if __name__ == "__main__":
    speak("hey this is PABLO AI") 
    #wishme()
    #takeCommand()
    while True:
        #print("listening")
        query=takeCommand()
        #speak(query)
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        #to open sites directly
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        ''' #to open music and can open any other apps
            if"Open music" in query:
            musicPath=
            os.system(f"open{musicPath}") '''  
        #to know present time     
        if  "the time" in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"sir the time is {strfTime}")    
        elif "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "pablo stop".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr=""    

        else:
            print("chatting...")
            chat(query)



        #speak(query)   
        