'''
Author: Michele Alladio
es:
Given two lists determine if the first list is contained within the second list, if the second list is contained within the first list, if both lists are contained within each other or if none of these are true.

Specifically, a list A is a sublist of list B if by dropping 0 or more elements from the front of B and 0 or more elements from the back of B you get a list that's completely equal to A.

Examples:

A = [1, 2, 3], B = [1, 2, 3, 4, 5], A is a sublist of B
A = [3, 4, 5], B = [1, 2, 3, 4, 5], A is a sublist of B
A = [3, 4], B = [1, 2, 3, 4, 5], A is a sublist of B
A = [1, 2, 3], B = [1, 2, 3], A is equal to B
A = [1, 2, 3, 4, 5], B = [2, 3, 4], A is a superlist of B
A = [1, 2, 4], B = [1, 2, 3, 4, 5], A is not a superlist of, sublist of or equal to B
'''

def listRelation(list1, list2):
    position = 0
    ok = True

    if len(list1) <= len(list2):    #lista1 più corta o = a lista2

        #trovo la posizione della prima corrispondenza
        for number in list2:
            if number == list1[0]:
                break
            else:
                position += 1

        for number in list1:
            if number != list2[position]:   #se il numero nella prima lista è diverso dal numero nella stessa posizione nella seconda
                ok = False
                print(f"list1 is not a superlist of, sublist of or equal to list2")
                break
            else:   #se sono uguali vengono rimossi
                list1.remove(number)
                list2.remove(number)
            
            position += 1

        if ok == True:    
            if not list1 and not list2: #se entrambe le liste sono vuote
                print("list1 is equal to list2")
            else:
                print("list1 is a sublist of list2")
                

    elif len(list1) > len(list2):   #lista 1 più piccola

        for number in list1:    #trovo la posizione della prima corrispondenza
            if number == list2[0]:
                break
            else:
                position += 1

        for number in list2:
            if number != list1[position]:   #se i numeri non corrispondono
                ok = False
                print(f"list1 is not a superlist of, sublist of or equal to list2")
                break
                
            position += 1
        
        if ok == True:
            print("list1 is a superlist of list2")


def main():

    list1 = []
    list2 = []

    #riempimento prima lista
    while True:
        num1 = int(input("Inserisci un numero per la prima lista (-1 per uscire): "))

        if num1 == -1:  #controllo uscita
            break
        else:
            list1.append(num1)

    
    #riempimento seconda lista
    while True:
        num2 = int(input("Inserisci un numero per la seconda lista (-1 per uscire): "))

        if num2 == -1:  #controllo uscita
            break
        else:
            list2.append(num2)
    
    listRelation(list1, list2)
    

if __name__ == "__main__":
    main()
    