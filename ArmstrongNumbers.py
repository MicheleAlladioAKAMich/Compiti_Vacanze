'''
Author: Michele Alladio
es:
An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9
10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
Write some code to determine whether a number is an Armstrong number.
'''

def armstrongNumber(number):
    powsSum = 0
    powValue = 0

    for value in str(number):
        powValue += 1   #calcola il valore della potenza in base alle cifre del numero 

    for value in str(number):   #somma delle potenze
        powsSum += int(value) ** powValue
    
    if powsSum == number:   #se la somma delle potenze è = al numero 
        print(f"{number} is an Armstrong number")
    else:    #se la somma delle potenze è != dal numero 
        print(f"{number} isn't an Armstrong number")


def main():
    number = int(input("Inserisci un numero > 0: "))

    if number < 0:  #controllo inserimento del numero
        print("Il numero dev'essere positivo.")
        return
    else:
        armstrongNumber(number)


if __name__ == "__main__":
    main()