import speech_recognition as sr


r = sr.Recognizer()


def listen():

    try:

        with sr.Microphone() as source:

            print("Listening...")

            r.adjust_for_ambient_noise(source)

            audio = r.listen(source)

            text = r.recognize_google(audio)

            return text

    except:

        return ""
