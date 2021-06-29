'''
Author: Michele Alladio
es: 
Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan gramma, "every letter") is a sentence using every letter of the alphabet at least once. The best known English pangram is:
The quick brown fox jumps over the lazy dog.
The alphabet used consists of ASCII letters a to z, inclusive, and is case insensitive. Input will not contain non-ASCII symbols.
'''

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L',
            'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def isPangram(phrase):
    
    for character in phrase:
        #controllo se il carattere nella frase è contenuto nell'alfabeto
        if character.upper() in alphabet:
            #lo rimuovo
            alphabet.remove(character.upper())
    
    if not alphabet:    #se non rimangono lettere inutilizzate
        print(f"{phrase} is a pangram")
    else:   #se rimangono lettere inutilizzate
        print(f"{phrase} isn't a pangram")

    
def main():
    phrase = input("Inserisci una frase: ")

    isPangram(phrase)

if __name__ == "__main__":
    main()