#Jc 2nd simple morse code

letters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ")

morse_code = (".-","-...","-.-.","-..",".",'..-.','--.','....','..','.---', '-.-','.-..','--','-.','---','.--.','--.-','.-.','...', '-','..-','...-','.--','-..-','-.--','--..','/')

def english_to_morse():
    #Will find the index of all the charaters in the list then turn them into morse code based on the index
    player_message = input("What message do you want to turn into morse code:").strip().lower()
    morse_answer = ""
    for x in player_message:
        if x in letters:
            letter_index = letters.index(x)
            y = str(morse_code[letter_index])
            morse_answer += y
            morse_answer += " "
    print(morse_answer)
def morse_to_english():
    player_message = input("What message do you want to turn into morse code:").strip().lower()
    #This is literaly just the oppisite of the english to morse exept i had to split it first
    english_answer = ""
    player_message = player_message.split()
    for x in player_message:
        if x in morse_code:
            morse_code_index = morse_code.index(x)
            y = str(letters[morse_code_index])
            english_answer += y
    print(english_answer)
def main_menu():
    #Just ask the player then throw them into the correct functions
    playing = True
    while playing:
        player_message = input("Do you want to 1.english to morse code or 2 the oppisite or 3 to leave:").strip().lower()
        if player_message == "1":
            english_to_morse()
        if player_message == "2":
            morse_to_english()
        if player_message == "3":
            playing = False


main_menu()