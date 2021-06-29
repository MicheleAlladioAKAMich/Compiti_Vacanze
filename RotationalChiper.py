'''
Author: Michele Alladio
es: 
Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.
The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular arithmetic. 
The letter is shifted for as many values as the value of the key.
The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: nopqrstuvwxyzabcdefghijklm
It is stronger than the Atbash cipher because it has 27 possible keys, and 25 usable keys.

Ciphertext is written out in the same formatting as the input including spaces and punctuation.

Examples
ROT5 omg gives trl
ROT0 c gives c
ROT26 Cool gives Cool
ROT13 The quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The quick brown fox jumps over the lazy dog.
'''

alphabetUpper = ['A','B','C','D','E','F','G','H','I','J','K','L',
            'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

alphabetLower = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']



def ROT(phrase, rot):
    position = rot-1    #la posizione iniziale è settata tenendo conto del rot inserito
    ROTphrase = ''

    for character in phrase:    
        
        if character in alphabetUpper:  #se il carattere è nell'alfabeto maiuscolo
        
            for upperCharacter in alphabetUpper:
                position += 1   #incremento della posizione
                if character == upperCharacter: #quando viene trovata la corrispondenza
                    if position >= len(alphabetUpper):  #se la posizione è maggiore della lunghezza della lista
                        position -= len(alphabetUpper)  #alla posizione viene sottratta la lunghezza della lista

                    ROTphrase += alphabetUpper[position]    #costruzione della frase
            
        elif character in alphabetLower:    #se il carattere è contenuto nell'alfabeto minuscolo
        
            for lowerCharacter in alphabetLower:
                position += 1
                if character == lowerCharacter:
                    if position >= len(alphabetLower):
                        position -= len(alphabetLower)
                        
                    ROTphrase += alphabetLower[position]
        
        else:   #se il carattere non è contenuto nei due alfabeti
            ROTphrase += character  #non viene variato

        position = rot-1

    return ROTphrase


def main():
    phrase = input("Inserisci la frase da trasformare: ")
    rot = int(input("decidi il numero di ROT (da 0 a 26): "))

    if rot < 0 or rot > 26:
        print("ROT non valido")
        return
    else:
        print(ROT(phrase, rot))

if __name__ == "__main__":
    main()
