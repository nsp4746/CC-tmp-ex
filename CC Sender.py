# Nikhil Patil
# CSEC 751
# Covert Channel Sender

import os, random, time, string


class Sender:
    def __init__(self, message):
        self.FILEPATH = os.curdir + "\\files\\"
        os.chdir(self.FILEPATH)
        self.message = message
        self.all_letters = string.ascii_letters
        self.cipher_message = []
        self.encryption_dictionary = {}
        key = 4
        for i in range(len(self.all_letters)):
            self.encryption_dictionary[self.all_letters[i]] = self.all_letters[(i + key) % len(self.all_letters)]

    def __str__(self):
        return f'Message Sent: {self.message}'

    def set_message(self, message):
        self.message = message


    def create_files(self):
        for char in self.message:
            filename = "file_" + char + "_" + str(random.randint(1, 1000))
            f = open(filename, "w")
            f.close()
            time.sleep(.5)

    def encrypt_message(self):
        for char in self.message:
            if char in self.all_letters:
                temp =  self.encryption_dictionary[char]
                self.cipher_message.append(temp)
            else:
                temp = char
                self.cipher_message.append(temp)

        self.cipher_message = "".join(self.cipher_message)
        self.message = self.cipher_message


def main():
    sender = Sender("i am studying covert channels at rit")
    sender.encrypt_message()
    sender.create_files()

if __name__ == "__main__":
    main()

