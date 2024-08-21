def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
print(getDoubleAlphabet("ABC"))

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return  shiftAmount
    
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    

def caesarCipherProgram():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {alphabet}')
    doubleAlphabet = getDoubleAlphabet(alphabet)
    print(f'Double Alphabet: {doubleAlphabet}')
    message = getMessage()
    print(message)
    cipherKey = getCipherKey()
    print(cipherKey)
    myEncryptMessage = encryptMessage(message, cipherKey, doubleAlphabet)
    print(f'Encrypted Message: {myEncryptMessage}')
    myDecryptMessage = decryptMessage(myEncryptMessage, cipherKey, doubleAlphabet)
    print(f'Decypted Message: {myDecryptMessage}')
    
    
caesarCipherProgram()