import pyttsx3 # text-to-speech conversion library in Python
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
engine =  pyttsx3.init('sapi5') #sapi5 is windows api to recognize voices
voice=engine.getProperty('voices')
#print(voice[1].id)
engine.setProperty('voice',voice[1].id)



def speak(audio):
     engine.say(audio)
     engine.runAndWait()



def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good Morning')
    elif hour >=12 and hour <=18:
                speak('Good Afternoon')
    else:
        speak('Good Evening') 

    speak('I am siri how may i help you')



def tcommand(): #takes microphone input from the user and returns string output
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1 
        audio=r.listen(source)
    try:
        print('Recognizing.....')
        query=r.recognize_google(audio,language='en-in')
        print(query)
        
        
          
    except Exception as e:
        print(e)
        speak('Sorry I did not hear you Say that again....')
        return 'None'
    return query
      
if __name__ == "__main__":
    wish()
    
    query=tcommand().lower()
    if 'wikipedia' in query:
        speak('Searching wikipedia')
        # erase wikipedia in the sentence
        query=query.replace('wikipedia',"")
        results=wikipedia.summary(query,sentences=2)
        speak('According to wikipedia')
        speak(results)
        #rint(results)
    elif 'open youtube' in query:
        webbrowser.open('youtube.com')
    elif 'open google' in query:
        webbrowser.open('google.com')
    elif 'open stackoverflow' in query:
        webbrowser.open('stackoverflow.com')
    elif 'play music' in query:
        music='D:\\music'
        songs=os.listdir(music)
        print(songs)
        os.startfile(os.path.join(music,songs[0]))
    elif 'time' in query: 
        perTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'the time is {perTime}')
    elif 'open cricket' in query:
        path='D:\\games\\Cricket_2007\\Cricket07.exe'
        os.startfile(path)
    
    

                

