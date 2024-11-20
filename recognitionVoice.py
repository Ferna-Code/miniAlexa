# first create the virtual environment
# python -m venv venv

# Activate virtual environment
# .\venv\Scripts\activate

# Install SpeechRecognition whit pip install SpeechRecognition
# Install pyttsx3 whit pip install pyttsx3

# web amazon https://www.amazon.es/s?k=

import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk():
    try:
        mic = sr.Microphone()
        with mic as source:
            print("Escuchando...")
            audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio, language='es-ES')
        print(f'Has dicho: {text}')
        return text.lower()
    except sr.UnknownValueError:
        print("No entendí lo que dijiste, por favor intenta de nuevo.")
        engine.say("No entendí lo que dijiste, por favor intenta de nuevo.")
        engine.runAndWait()
        return ""
    except sr.RequestError as e:
        print(f"Error del servicio de reconocimiento de voz: {e}")
        engine.say("Hubo un problema con el servicio de reconocimiento de voz.")
        engine.runAndWait()
        return ""

try:
    while True:
        text = talk()
        if 'amazon' in text:
            engine.say('¿Qué quieres comprar en Amazon?')
            engine.runAndWait()
            search = talk()
            if search:
                webbrowser.open(f'https://www.amazon.es/s?k={search}')
            else:
                engine.say("No se pudo realizar la búsqueda.")
                engine.runAndWait()
            break 
        else:
            print("No mencionaste Amazon. Por favor, inténtalo de nuevo.")
            engine.say("No mencionaste Amazon. Por favor, inténtalo de nuevo.")
            engine.runAndWait()
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    engine.say("Ocurrió un error inesperado.")
    engine.runAndWait()
