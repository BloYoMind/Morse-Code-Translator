def to_morse(words):
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", 
             "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", 
             "..-", "...-", ".--", "-..-", "-.--", "--..", "/"]
    english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
               "u", "v", "w", "x", "y", "z", " "]
    
    translation = ""
    for i in words.lower():
        if i in english:
            i_index = english.index(i)
            equivalent = morse[i_index]
            translation += equivalent + " "
        else:
            translation += "? "  # Unknown character
    return translation.strip()

loop = True
while loop:
    print("Enter your text below:")
    user_input = input()
    morse_output = to_morse(user_input)
    print("Morse code translation:")
    print(morse_output)

    print("Would you like to restart? (yes/no)")
    loop_response = input().lower()
    if loop_response == "yes":
        continue
    else:
        loop = False
