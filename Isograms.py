'''
Author: Michele Alladio
es:
Determine if a word or phrase is an isogram.

An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:

lumberjacks
background
downstream
six-year-old
The word isograms, however, is not an isogram, because the s repeats.
'''

def isogram(word):
    characterList = []
    double = False

    for character in word.upper():
        if character in characterList and character != ' ' and character != '-':    #se il carattere è doppio e non è uno spazio o un -
            double = True   #la parola non è un isogramma
            break

        characterList.append(character)
    
    if double:
        print(f"{word} non è un isogramma")
    else:
        print(f"{word} è un isogramma")


def main():
    word = input("Inserisci una parola: ")
    isogram(word)


if __name__ == "__main__":
    main()