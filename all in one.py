def to_morse(words):
    morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", 
                  "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", 
                  "..-", "...-", ".--", "-..-", "-.--", "--..", "/"]
    english_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 
                    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
                    "u", "v", "w", "x", "y", "z", " "]
    
    translation = ""
    for i in words.lower():
        if i in english_list:
            i_index = english_list.index(i)
            equivalent = morse_list[i_index]
            translation += equivalent + " "
        else:
            translation += "? "
    return translation.strip()

def from_morse(morse_input):
    morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                  "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                  "..-","...-",".--","-..-","-.--","--..","/"]
    english_list = ["a","b","c","d","e","f","g","h","i","j",
                    "k","l","m","n","o","p","q","r","s","t",
                    "u","v","w","x","y","z"," "]
    
    translation = ""
    letters = morse_input.strip().split(" ")
    for sequence in letters:
        if sequence in morse_list:
            index = morse_list.index(sequence)
            translation += english_list[index]
        else:
            translation += "?"
    return translation

# Main loop
while True:
    print("Would you like to translate 'to morse' or 'from morse'? (type 'exit' to quit)")
    choice = input("> ").strip().lower()
    
    if choice == "to morse":
        print("Enter the English text:")
        user_input = input("> ")
        print("Morse Code Translation:")
        print(to_morse(user_input))
    
    elif choice == "from morse":
        print("Enter the Morse code (separate letters with spaces, words with '/'): ")
        morse_input = input("> ")
        print("English Translation:")
        print(from_morse(morse_input))
    
    elif choice == "exit":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please type 'to morse', 'from morse', or 'exit'.")
