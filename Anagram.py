'''
Author: Michele Alladio
es: 
An anagram is a rearrangement of letters to form a new word. Given a word and a list of candidates, select the sublist of anagrams of the given word.
Given "listen" and a list of candidates like "enlists" "google" "inlets" "banana" the program should return a list containing "inlets".
'''

def searchAnagram(word, candidates):
    for candidate in candidates:    #ciclo i candidati
        if candidate != word:   #se il candidato è diverso dalla parola
            #creo due liste contenenti le lettere delle due parole
            list1 = list(candidate)
            list2 = list(word)
            for letter in candidate:    #ciclo le lettere del candidato
                for character in word:  #ciclo le lettere della parola
                    if letter.upper() == character.upper() and letter in list1 and character in list2:  #se le due lettere sono uguali e sono nelle liste
                        #le rimuovo dalle rispettive liste
                        list1.remove(letter)
                        list2.remove(character)

            if not list1 and not list2: #se entrambe le liste sono vuote le due parole sono anagrammi
                print(f"{candidate} is an anagram of {word}")

def main():
    candidates = []

    word = input("Inserisci una parola: ")

    while True:
        candidate = input("Inserisci un candidato (esc per uscire): ")

        if candidate == 'esc' or candidate == 'ESC':
            break
        else:
            candidates.append(candidate)

    searchAnagram(word, candidates)

if __name__ == "__main__":
    main()

