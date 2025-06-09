morse = input("Input the morse code to be translated, with spaces between the different sequences and a space at the end: ")
morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."," "]
english_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
code = ""
translation = ""
letters = []
for character in morse:
    if character != " ":
        code += character
    elif character == " ":
        letters.append(code)
        code = ""
for sequence in letters:
    equivalent = morse_list.index(sequence)
    english = english_list[equivalent]
    translation += english
print(translation)
