import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()
mic = sr.Microphone(device_index = 0)
engine = pyttsx3.init()
with mic as source:
    print("speak")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    if(audio):
        print("listening")
        if(audio == "exit"):
            exit()
    print(r.recognize_google(audio))
    engine.say(r.recognize_google(audio))
    engine.setProperty('rate',120)
    engine.setProperty('volume',1.0)
    engine.runAndWait()

