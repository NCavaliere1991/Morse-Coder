# Morse-Coder

Has two lists consisting of the regular and morse alphabet. 

The make_morse function is passed a message input to encrypt into morse code. It iterates over the inputted message and retrieves each letter's index position in relation to the alphabet list. 
It creates a morse letter variable by retrieving the morse letter in the morse list at the index position of the alphabetical letter.
The morse letter is added to an empty string along with an extra space to separate the letters. Two words are separated by a "\" and an extra space.
It then returns the encrypted message

The make_normal function is passed an encrypted phrase to decode. The encoded message is split into a list using the .split() function then iterated over using a for loop.
If a "\" is in the message, an empty space is added to the plain_text. Otherwise the function does the exact same as the make_morse function in reverse and returns the decoded message.
