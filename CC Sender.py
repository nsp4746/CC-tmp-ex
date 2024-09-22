# Nikhil Patil
# CSEC 751
# Covert Channel Sender

import os, random, string


class Sender:
    """
    This class is used for creating a sender client and making "files" that are to be placed in a files directory.
    It encrypts the message via substitution cipher.
    """
    def __init__(self, message):
        self.FILEPATH = os.curdir + "\\files\\"
        os.chdir(self.FILEPATH)
        self.message = message
        self.all_letters = string.ascii_letters
        self.cipher_message = []
        self.encryption_dictionary = {}
        key = 22
        for i in range(len(self.all_letters)):
            self.encryption_dictionary[self.all_letters[i]] = self.all_letters[(i + key) % len(self.all_letters)]

    def __str__(self):
        return f'Message Sent: {self.message}'

    def set_message(self, message):
        """
        Setter for message
        :param message:
        :return:
        """
        self.message = message

    def create_files(self):
        """
        @name: create_files \n
        @function: creates the files that are going to be read by the receiver
        :return:
        """
        for char in self.message:
            randint = random.randint(1,1200)
            filename = "file_" + char + "_" + str(randint)
            f = open(filename, "w")
            os.chmod(filename, 0o666)
            f.close()
           # time.sleep(1)

    def encrypt_message(self):
        """
        @name: encrypt_message \n
        @function: encrypts the plaintext message via substitution cipher.
        :return:
        """
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
    sender = Sender("RIT") # create instance
    sender.encrypt_message() # encrypt the message
    sender.create_files() # create files

if __name__ == "__main__":
    main()

