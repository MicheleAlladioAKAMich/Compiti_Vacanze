'''
Author: Michele Alladio
es: 
Given a word, compute the scrabble score for that word.

Letter Values
You'll need these:

Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
'''

dictValues = {'AEIOULNRST':1, 'DG':2, 'BCMP':3, 'FHVWY':4, 'K':5, 'JX':8, 'QZ':10}  #dizionario lettere: valore

def scrabbleScore(phrase):
    score = 0   

    for character in phrase:    #ciclo i caratteri nellla frase
        for string, value in dictValues.items():
            for letter in string:   #ciclo le lettere nel dizionario
                if letter == character.upper(): #se trovo una corrispondenza
                    score += value  #incremento il punteggio con il valore adatto
    
    return score
            

def main():
    phrase = input("Inserisci una frase: ")
    
    print(f"Scrabble score of {phrase}: {scrabbleScore(phrase)}")


if __name__ == "__main__":
    main()