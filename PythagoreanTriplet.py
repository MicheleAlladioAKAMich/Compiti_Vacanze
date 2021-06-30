'''
Author: Michele Alladio
es: 
A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for which,

a**2 + b**2 = c**2
and such that,

a < b < c
For example,

3**2 + 4**2 = 9 + 16 = 25 = 5**2.
Given an input integer N, find all Pythagorean triplets for which a + b + c = N.

For example, with N = 1000, there is exactly one Pythagorean triplet for which a + b + c = 1000: {200, 375, 425}.
'''

def pythagoreanTriplet(number):
    numberList = [k for k in range(1, number)]  #lista dei numeri da 1 alla soglia

    #triplo ciclo per sommare insieme chiascun numero con altri due numeri nella lista
    for a in numberList:
        for b in range(a+1, len(numberList)+1):
            for c in range(b+1, len(numberList)+1):
                #notare: con questi 3 cicli sarà sempre vera la condizione a<b<c
                if a+b+c == number and a**2 + b**2 == c**2: #se i tre numeri sommati danno la soglia ed i quadrati di a e b sommati danno il quadrato di c
                    print(a,b,c)    #Pythagoric triplet


def main():
    number = int(input("Insert a number: "))

    pythagoreanTriplet(number)

if __name__ == "__main__":
    main()
