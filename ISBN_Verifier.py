'''
Author: Michele Alladio
es:
The ISBN-10 verification process is used to validate book identification numbers. These normally contain dashes and look like: 3-598-21508-8

ISBN
The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens, and can be checked for their validity by the following formula:

(x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.

Example
Let's take the ISBN-10 3-598-21508-8. We plug it in to the formula, and get:

(3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
Since the result is 0, this proves that our ISBN is valid.

Task
Given a string the program should check if the provided string is a valid ISBN-10. Putting this into place requires some thinking about preprocessing/parsing of the string prior to calculating the check digit for the ISBN.
The program should be able to verify ISBN-10 both with and without separating dashes.

Caveats
Converting from strings to numbers can be tricky in certain languages. Now, it's even trickier since the check digit of an ISBN-10 may be 'X' (representing '10'). For instance 3-598-21507-X is a valid ISBN-10.
'''

validCharacters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']

def validISBN(isbn, numberList):
    sumISBN = 0

    for factor in range(0, 10):
        sumISBN += numberList[factor] * (10-factor) #somma dei caratteri moltiplicati per il peso della propria posizione

    if sumISBN % 11 == 0:   #se la somma è divisibile per 11
        print(f"{isbn} is a valid ISBN-10")
    else:
        print(f"{isbn} isn't a valid ISBN-10")
        

def main():
    isbn = input("Inserisci un codice ISBN-10 valido: ").upper()

    characterNum = 0
    numberList = []

    for character in isbn:
        if character != '-':
            if character not in validCharacters:    #se il carattere non è nella lista dei caratteri validi
                print("Codice ISBN-10 non valido.")
                return
            else:
                characterNum += 1
                if character == 'X':
                    numberList.append(10)   #se il carattere è una X il suo valore è 10
                else:
                    numberList.append(int(character))
    
    if characterNum != 10:  #se non vi sono 10 caratteri
        print("Codice ISBN-10 non valido.")
        return
    else:
        validISBN(isbn, numberList)

if __name__ == "__main__":
    main()