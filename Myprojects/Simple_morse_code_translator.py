#Jc 2nd simple morse code

letters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","")

morse_code = ("·−","−···","−·−·","−··","·",'··−·','−−·','····','··','·−−−', '−·−','·−··','−−','−·','−−−','·−−·','−−·-','·−·','···', '−','··−','···−','·−−','−··−','−·−−','−−··')

def english_to_morse():
    #Will find the index of all the charaters in the list then turn them into morse code based on the index
    player_message = input("What message do you want to turn into morse code").strip().lower()
    morse_answer = ""
    for x in player_message:
        letter_index = letters.index(x)
        y = morse_code[letter_index]
        morse_answer + y
    print(morse_answer)
    pass
def morse_to_english():
    pass


english_to_morse()