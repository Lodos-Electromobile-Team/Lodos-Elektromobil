import os
import sys

import speech_recognition as sr
from gtts import gTTS
from PyQt5 import QtWidgets

from Thread import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle("Lodos Elektromobil")
        
        self.gui()
        self.show()


    def gui(self):
        btn = QtWidgets.QPushButton("Buton",self)
        btn.move(10,10)
        btn.setStyleSheet("background-color: black;color: white;")
        btn.clicked.connect(self.sesDeneme)

    def speak(self,audioString):
        print(audioString)
        tts = gTTS(text=audioString, lang='tr', slow=False)
        tts.save("audio.mp3")
        os.system("mpg123 audio.mp3")

    def recordAudio(self):
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("5 saniyelik dinleme başladı")
            audio = r.record(source,duration=3)
            # Speech recognition using Google Speech Recognition
            data = ""
            try:
                # Uses the default API key
                # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                data = r.recognize_google(audio,language='tr')
                print(data + " dedin")
            except sr.UnknownValueError:
                print("Ne dediğini anlamadım")
            except sr.RequestError as e:
                print("Google Konuşma Tanımlama Serivisinde bir hata oluştu; {0}".format(e))

            return data

    def jarvis(self, data):
        data = data.lower()
        if "nasılsın" in data:
            self.speak("İyiyim teşekkürler")

        if "aracı çalıştır" in data:
            self.speak("bataryada enerji mi kaldı mk fakiri")

        if "lambaları aç" in data:
            self.speak("tamam. farlar açık")
            self.setStyleSheet("background-color: red;")
        if "lambaları kapat" in data:
            self.speak("tamam. farlar kapalı")
            self.setStyleSheet("background-color: white;")

            



    def sesDeneme(self):
        data = self.recordAudio()
        self.jarvis(data)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())
