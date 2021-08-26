import speech_recognition
import pyttsx3
from word2number import w2n

recognizer = speech_recognition.Recognizer()

while True:

    try:

        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f'You said:\n{text}')
            total = 0
            for number in text.split():
                total += w2n.word_to_num(number)
            print(f'The sum is: {total}')

    except Exception as exc:
        print(f'Error occured.\n{exc}')
        recognizer = speech_recognition.Recognizer()
        continue