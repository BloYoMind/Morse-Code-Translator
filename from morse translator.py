morse = input("Input the morse code to be translated, with spaces between the different sequences and a space at the end: ")
morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."," "]
english_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
code = ""
translation = ""
letters = []
for character in morse:
    print("character: "+character)
    if character != " ":
        code += character
    elif character == " ":
        print("code: "+code)
        letters.append(code)
        code = ""
print("letters: ")
print(letters)
for sequence in letters:
    print("sequence"+sequence)
    equivalent = morse_list.index(sequence)
    english = english_list[equivalent]
    translation += english
print(translation)