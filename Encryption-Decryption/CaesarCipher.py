######################################################
#
# (C) Michael Kane 2017
#
# Student No: C14402048
# Course: DT211C
# Date: 03/010/2017
#
# Title: Caesar Cipher Decryption Alogorithm.
#
# References:
#
# Al Sweigart. (2013). Hacking The Caesar Cipher With The Brute-Force Technique. In: Hacking Secret Ciphers with Python.
# United States: Creative Commons BY-NC-SA. p88-95.

class CaesarCipher(object):
    """
    The purpose of this class is to take Cipher text and key from a user and decrypt the text.
    """
    def __init__(self, key=0, message=""):
        self.key = key
        self.message = message

    def user_input(self):
        """
        Take a cipher text and key from the user.
        Strip the line endings off the cipher text so they dont interfere with the decription.
        Call the Decrypt function.
        :return:
        """
        try:
            filename = input("Please enter a filename, which contains your encrypted string.")
            self.message = [line.rstrip('\n') for line in open(filename)]
            self.message = list("".join(self.message))
            self.key = int(input("Hello please enter a key."))
            decrypted_string = self.decrypt(self.key, self.message)
            print(decrypted_string)
        except IOError:
            print("file could not be found")

    def decrypt(self, key, message):
        """
        Code is taken from the above source with minor alterations.
        :param key:
        :param message:
        :return:
        """
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        decrypted_string = ""
        for char in message:
            if char in letters:
                num = letters.find(char)
                num = num - key
                if num < 0:
                    num += len(letters)
                decrypted_string += letters[num]
            else:
                decrypted_string = decrypted_string + char
        return str(decrypted_string)

if __name__ == '__main__':
    CaesarCipher().user_input()
