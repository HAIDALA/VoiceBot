from typing import Mapping
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import json

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate',150)   ## how fast you want your assistant to talk

todo_list = ['Go Shopping', 'Clean Room', 'Record Video']




def add_Sopping_list():

    global recognizer
    speaker.say("What item do you want to add to your shopping list?")
    speaker.runAndWait()
    done=False
    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                speaker.say("I added {item} to my shopping list!")
                speaker.runAndWait()

        except speech_recognition.UnKnownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not undrstand you!. Please try again!")
            speaker.runAndWait()

def show_Sopping_list():

    speaker.say("The items on your shopping list are the following")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()

def hello():
    speaker.say("Hello. What can I do for you?")
    speaker.runAndWait()

def quit():
    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)




                

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()

while True:

    try:

        with speech_recognition.Microphone() as mic:
           
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()
        
        assistant.request(message)
    
    except speech_recognition.UnKnownValueError:
        recognizer = speech_recognition.Recognizer() 
