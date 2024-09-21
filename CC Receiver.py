# Nikhil Patil
# CSEC 751
# Covert Channel Receiver

import os, string
from pathlib import Path

class Receive:
    def __init__(self):
        self.filepath = os.curdir + "\\files\\"
        os.chdir(self.filepath)
        self.message = ""
        self.all_letters = string.ascii_letters
        self.decrypted_message = []
        self.decryption_dictionary = {}
        key = 4
        for i in range(len(self.all_letters)):
            self.decryption_dictionary[self.all_letters[i]] = self.all_letters[(i - key) % (len(self.all_letters))]

    def receive_message(self):
        paths = sorted(Path().iterdir(), key=os.path.getmtime)
        for cf in paths:
            self.message = self.message + str(cf)[5]

    def decrypt_message(self):
        for char in self.message:
            if char in self.all_letters:
                temp = self.decryption_dictionary[char]
                self.decrypted_message.append(temp)
            else:
                temp = char
                self.decrypted_message.append(temp)
        self.decrypted_message = "".join(self.decrypted_message)

        for filename in os.listdir(os.curdir):
            os.remove(os.curdir + "\\" + filename)


        return self.decrypted_message


def main():
    receiver = Receive()
    receiver.receive_message()
    receiver.decrypt_message()
    print(receiver.decrypted_message)

if __name__ == "__main__":
    main()