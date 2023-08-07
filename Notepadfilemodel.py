import os
import string
from tkinter import filedialog


class File_model:
    def __init__(self):
        self.url = ""
        self.key = string.ascii_lowercase + string.ascii_uppercase + "0123456789"
        self.offset = 5

    def encrypt(self, plaintext):
        result = ""
        for a in plaintext:
            try:
                ind = self.key.index(a)
                ind = ind + self.offset % 62
                print(ind)
                result += self.key[ind]
            except ValueError:
                result += a
        return result

    def decrypt(self, ciphertext):
        result = ""
        for ch in ciphertext:
            try:
                ind = self.key.index(ch)
                ind = (ind - self.offset) % 62
                result += self.key[ind]
            except ValueError:
                result += ch
        return result

    def open_file(self):
        self.url = filedialog.askopenfilename(title="Select File", filetype=[("Text Document", "*.*")])

    def new_file(self):
        self.url = ""

    def save_as(self, msg):
        msg_encrpyted = self.encrypt(msg)
        self.url = filedialog.asksaveasfile(mode="w",defaultextension=".ntxt",filetype=[("All Files","*.*"),("Text Documents","*.*")])
        self.url.write(msg_encrpyted)
        filepath = self.url.name
        self.url.close()
        self.url = filepath

    def save_file(self,msg):
        if self.url == "":
            self.url = filedialog.asksaveasfilename(title="Select File",defaultextension=".ntxt",filetype=[("Text Documents","*.*")])
        filename,file_extension = os.path.splitext(self.url)
        content = msg
        if file_extension in ".ntxt":
            content = self.encrypt(content)
        with open(self.url, 'w',encoding='utf-8') as fw:
            fw.write(content)

    def read_file(self, url=''):
        if url != "":
            self.url = url
        else:
            self.open_file()
        base = os.path.basename(self.url)
        file_name, file_extension = os.path.splitext(self.url)
        fr = open(self.url,"r")
        contents = fr.read()
        if file_extension == '.ntxt':
            contents = self.decrypt(contents)
        fr.close()
        return contents,base



