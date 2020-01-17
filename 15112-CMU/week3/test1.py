def applyCaesarCipher(message, shiftNum):
    cipherText = ""
    for ch in message:
        if ch.isspace():
            finalLetter = ch
            cipherText += finalLetter

        elif ch.isalpha() and ch.islower() and shiftNum > 0:
            stayInAlphabet = ord(ch) + shiftNum
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter

        elif ch.isalpha() and ch.islower() and shiftNum < 0:
            stayInAlphabet = ord(ch) + shiftNum
            if stayInAlphabet < ord('a'):
                stayInAlphabet += 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter

        elif ch.isalpha() and ch.isupper() and shiftNum > 0:
            stayInAlphabet = ord(ch) + shiftNum
            if stayInAlphabet > ord('Z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter

        elif ch.isalpha() and ch.isupper() and shiftNum < 0:
            stayInAlphabet = ord(ch) + shiftNum
            if stayInAlphabet < ord('A'):
                stayInAlphabet += 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
        else:
            cipherText += ch
    return cipherText




def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3) == \
        "defghijklmnopqrstuvwxyzabc")
    assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    assert(applyCaesarCipher("1234", 6) == "1234")
    print("Passed.")

testApplyCaesarCipher()
# applyCaesarCipher("We Attack At Dawn", 1)
# applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3)
# applyCaesarCipher("zodiac", -2)
# applyCaesarCipher("1234", 6)
print(applyCaesarCipher('What. An. Evil! Test? Case@[`{', 25))
