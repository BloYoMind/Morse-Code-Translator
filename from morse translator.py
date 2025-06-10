def from_morse(morse)
    morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."," "]
    english_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    code = ""
    translation = ""
    letters = []
    for character in morse:
    if character == " ":
        letters.append(code)
        code = ""
    elif character == "/":
        letters.append(code)
        code = ""
        letters.append(" ")
    else:
        code += character
    for sequence in letters:
        equivalent = morse_list.index(sequence)
        english = english_list[equivalent]
        translation += english
    return translation

loop = True
while loop:
    morse_input = input("Input the morse code to be translated, with spaces between the different sequences and a space at the end: ")
    english_output = from_morse(morse_input)
    print("English translation:")
    print(english_output)

    print("Would you like to restart? (yes/no)")
    loop_response = input().lower()
    if loop_response == "yes":
        continue
    else:
        loop = False
