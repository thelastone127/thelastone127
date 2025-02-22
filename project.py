import pyttsx3
import time


machine = pyttsx3.init('sapi5')
voices = machine.getProperty('voices')

machine.setProperty('voice',voices[0].id)



def speak(audio):
    machine.say(audio)
    machine.runAndWait()



if __name__ =="__main__":
    a = ("red","yellow","green")


for i in range (0,2):
    b = a[i]
    if(a[i]=="red"):
        print("Red light is on please Stop your vehicle....")
        speak("Red light is on please Stop your vehicle....")

        time.sleep(4)
    elif(a[i]=="yellow"):
        print("Yellow traffic signal light is on stay on hold...")
        speak("Yellow traffic signal light is on stay on hold...")
        time.sleep(2)
        print("green light is on you can pass the road...")
        speak("green light is on you can pass the road...")
        