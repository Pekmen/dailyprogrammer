#!/usr/bin/env python3

morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
encoded = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"
message = "miodrag stojanovic gidra"
def decrypt(message):
	return "".join([chr(morse_alphabet.index(c) + 97) if c!= "/" else " " for c in message.split()])

def encrypt(message):
	return " ".join([morse_alphabet[ord(c) - 97] if c!=" " else "/" for c in "".join(message)])

print(decrypt(encoded))
print(encrypt(message))