
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys

recognizer = speech_recognition.Recognizer()
fr_voice_id ="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
speaker = tts.init()
speaker.setProperty('voice', fr_voice_id)
speaker.setProperty('rate',180)   ## how fast you want your assistant to talk




Shopping_list = ['parfum', 'Cafe', "pomme" ]

def search_item():
    global recognizer
    speaker.say("Quel article voulez-vous rechercher?")
    speaker.runAndWait()
    done=False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                product = recognizer.recognize_google(audio, language="fr-FR")
                product = product.lower()

                url = 'https://herboristerie-principale.ma/?s='+ product +'&page=search&post_type=product'
                done = True

                

        except speech_recognition.UnKnownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("je n'ai pas compris! Veuillez réessayer!")
            speaker.runAndWait()


    


def create_shopping_list():
    global recognizer

    speaker.say("Que souhaitez-vous ajouter à votre liste d'achat?")
    speaker.runAndWait()

    done=False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio, language="fr-FR")
                note = note.lower()

                speaker.say("Choisissez un nom de liste d'achat")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio, language="fr-FR")
                filename = filename.lower()
            
            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say("J'ai créé avec succès la liste d'achat {filename}")
                speaker.runAndWait()

        except speech_recognition.UnKnownValueError():
            recognizer = speech_recognition.Recognizer()
            speaker.say("je n'ai pas compris! Veuillez réessayer!")
            speaker.runAndWait()


def add_item_shopping_list():

    global recognizer

    speaker.say("Quel article voulez-vous ajouter?")
    speaker.runAndWait()
                
    done=False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio, language="fr-FR")
                item = item.lower()

                Shopping_list.append(item)
                done = True

                speaker.say(f"J'ai ajouter {item} dans votre list d'achat!")
                speaker.runAndWait()

        except speech_recognition.UnKnownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("je n'ai pas compris! Veuillez réessayer!")
            speaker.runAndWait()

def show_Shopping_list():

    speaker.say("les articles dans votre liste d'achat sont")
    for item in Shopping_list:
        speaker.say(item)
    speaker.runAndWait()

def hello():
    speaker.say("Bonjour. Que puis-je faire pour vous?",)
    speaker.runAndWait()
   
    
  
def quit():
    speaker.say("Au revoir")
    speaker.runAndWait()
    sys.exit(0)


mappings ={
    "greeting":hello,
    "create_shopping_list": create_shopping_list,
    "add_item_shopping_list":add_item_shopping_list,
    "show_Shopping_list":show_Shopping_list,
    "exit":quit,
    "search_item":search_item
}



assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()



while True:

    try:

        with speech_recognition.Microphone() as mic:
           
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio, language="fr-FR")
            message = message.lower()
        
        assistant.request(message)
        
    
    except speech_recognition.UnKnownValueError:
        recognizer = speech_recognition.Recognizer() 
        speaker.say("je n'ai pas compris! Veuillez réessayer!")
        speaker.runAndWait()



    

        






