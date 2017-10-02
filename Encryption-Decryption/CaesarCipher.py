class CaesarCipher(object):
    def __init__(self, key=0, message=""):
        self.key = key
        self.message = message

    def user_input(self):
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
        # https://inventwithpython.com/hacking/chapter7.html
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        decrypted_string = ""
        for char in message:
            if char in letters:
                num = letters.find(char)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                decrypted_string = decrypted_string + letters[num]
            else:
                decrypted_string = decrypted_string + char
        return str(decrypted_string)

if __name__ == '__main__':
    CaesarCipher().user_input()
