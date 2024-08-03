import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia


def speck(audio):
    """use for return the string to voice"""
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def date_():
    """return the date"""
    date = datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year
    speck(date)
    print(date)


def time_():
    """return the time"""
    time = datetime.datetime.now().time().strftime("%H:%M:%S")
    speck(time)
    print(time)


def greeting():
    """use for the greeting """
    hours = datetime.datetime.now().hour
    if 6 <= hours <= 12:
        speck("Good Morning sir!")
    elif 12 <= hours <= 18:
        speck("Good Afternoon Sir!")
    elif 18 <= hours <= 24:
        speck("Good Evening Sir!")
    else:
        speck("Good night sir!")

    speck("Jarvis at your service.how can i help you ?")


def TakeCommand():
    """take command from user and recognizing that"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except sr.UnknownValueError as e:
        print("Say again please.....")
        return "None"
    return query


def wikipedia_(query):
    query1 = query.replace('wikipedia', '')
    result = wikipedia.summary(query1, sentences=3)
    speck("According to wikipedia")
    print(result)
    speck(result)


if __name__ == '__main__':
    greeting()
    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            wikipedia_(query)
