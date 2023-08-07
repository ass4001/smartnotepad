import Notepadfilemodel
import speech_recognition as s


class File_Controller():
    def __init__(self):
        self.file_model = Notepadfilemodel.File_model()

    def save_file(self, msg):
        self.file_model.save_file(msg)

    def save_as(self, msg):
        self.file_model.save_as(msg)

    def read_file(self, url=""):
        self.msg, self.base = self.file_model.read_file(url)
        return self.msg, self.base

    def new_file(self):
        self.file_model.new_file()

    def take_quary(self):
        sr = s.Recognizer()
        print("Listening...")
        with s.Microphone() as m:
            audio = sr.listen(m)
            sr.adjust_for_ambient_noise(m, duration=5)
            text = sr.recognize_google(audio, language='en-IN')
            return text
