'''
Author: Michele Alladio
es: 
Use the Sieve of Eratosthenes to find all the primes from 2 up to a given number.
The Sieve of Eratosthenes is a simple, ancient algorithm for finding all prime numbers up to any given limit. It does so by iteratively marking as composite (i.e. not prime) the multiples of each prime, starting with the multiples of 2. It does not use any division or remainder operation.
Create your range, starting at two and continuing up to and including the given limit. (i.e. [2, limit])

The algorithm consists of repeating the following over and over:

take the next available unmarked number in your list (it is prime)
mark all the multiples of that number (they are not prime)
Repeat until you have processed each number in your range.

When the algorithm terminates, all the numbers in the list that have not been marked are prime.
'''

def sieve(number):
    primeNumbers = [k for k in range(2, number)]    #creazione della lista di numeri dal 2 al numero impostato come soglia

    #variabili per il controllo dei multipli
    multiple1 = 2 
    multiple2 = 2

    while multiple1 <= number:  #fino a quando il primo numero non raggiunge la soglia
        while multiple2 <= number:  #fino a quando il secondo numero non raggiunge la soglia
            multiple2 += multiple1  #tutti i multipli di ogni numero sotto la soglia
            #se un numero nella lista corrisponde ad un multiplo viene tolto dalla lista dei numeri primi
            for element in primeNumbers:
                if multiple2 == element:
                    primeNumbers.remove(element)
    
        multiple1 += 1  #incremento del primo multiplo
        multiple2 = multiple1   #il secondo multiplo diventa uguale al primo
    
    return primeNumbers

def main():
    number = int(input("Inserisci una soglia: "))

    print(f"Numeri primi sotto il {number}: {sieve(number)}")


if __name__ == "__main__":
    main()