morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---",
              "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", "--..--", ".-.-.-",
              "..--..", "-..-.", "-....-", "-.--.", "-.--.-"]

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ", ", ".", "?", "/", "-", "(",
            ")"]


def make_morse(msg):
    cipher_text = ""
    for letter in msg:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            morse_letter = morse_list[letter_position]
            cipher_text += morse_letter + " "
        elif letter == " ":
            cipher_text += "/" + " "
    return cipher_text


def make_normal(msg):
    plain_text = ""
    for letter in msg.split():
        if letter == "/":
            plain_text += " "
        if letter in morse_list:
            letter_position = morse_list.index(letter)
            plain_letter = alphabet[letter_position]
            plain_text += plain_letter
    return plain_text


phrase = input("Type the phrase you want encoded: ")
morse_message = make_morse(phrase)
print(morse_message)

encoded_phrase = input("Type the phrase you want decoded: ")
plain_message = make_normal(encoded_phrase)
print(plain_message)