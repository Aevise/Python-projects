import PY_Alphabets

def encode(text, shift):
    letterIndex = 0
    shiftedText = ""
    if(shift >= 26):
        shift = shift%26

    for letter in text:
        letterIndex = PY_Alphabets.roman.index(letter)
        if((letterIndex+shift) >= len(PY_Alphabets.roman)):
            shiftedText += PY_Alphabets.roman[(letterIndex+shift) - letterIndex - 2]
        else:
            shiftedText += PY_Alphabets.roman[shift + letterIndex]
    return shiftedText

def decode(text, shift):
    letterIndex = 0
    shiftedText = ""
    if(shift >= 26):
        shift = shift%26

    for letter in text:
        letterIndex = PY_Alphabets.roman.index(letter)
        if((letterIndex-shift) <= len(PY_Alphabets.roman)):
            shiftedText += PY_Alphabets.roman[letterIndex-shift]
        else:
            shiftedText += PY_Alphabets.roman[shift - letterIndex]
    return shiftedText

decision = input("Type 'encode' to encode or type 'decode' to decode:\n").lower()
message = ""
shift = 0

if(decision == "encode"):  
    message = str(input("Type your message:\n")).lower()
    shift = int(input("Type the shift number:\n"))
    message = encode(message, shift)
    print(f"Your message has been encoded into: {message}")
elif(decision == "decode"):
    message = str(input("Type received message:\n")).lower()
    shift = int(input("Type the shift number:\n"))    
    message = decode(message, shift)
    print(f"Decoded message: {message}")
else:
    print("Something went wrong")