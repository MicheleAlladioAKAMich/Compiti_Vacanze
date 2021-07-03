'''
Author: Michele Alladio
es:
Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.

The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.
'''

def difference(number):
    squareOfSum = 0
    sumOfSquare = 0

    for i in range(number+1):
        squareOfSum += i    #somma dei numeri minori della soglia

    squareOfSum **= 2   #square of the sum

    for i in range(number+1):
        sumOfSquare += i ** 2   #sum of squares

    return squareOfSum-sumOfSquare  #differenza


def main():
    number = int(input("Inserisci una soglia: "))

    if number < 0:  #controllo inserimento della soglia
        print("La soglia dev'essere positiva.")
        return
    else:
        print(f"The difference beetween the square of sum and the sum of squares of the first {number} N is: {difference(number)}") 


if __name__ == "__main__":
    main()