'''
Author: Michele Alladio
es:
Implement a clock that handles times without dates.
You should be able to add and subtract minutes to it.
'''
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
clock = {'Day': days[0], 'Hours': 0, 'Minutes':0}

def clockControl(number, decision, day):

    if decision == 'a' or decision == 'A':  #aumento minuti
        clock['Minutes'] += number  #incremento minuti
        while clock['Minutes'] >= 60:   #se si supera il limite di minuti per ora
            clock['Hours'] += 1 #incremento di 1 ora 
            clock['Minutes'] -= 60  #decremento dei minuti

        while clock['Hours'] >= 24: #se si supera il numero di ore in un giorno
            day += 1    #incremento del giorno
            if day < len(days):
                clock['Day'] = days[day]
            else:   #riinizio della settimana
                day = 0
                clock['Day'] = days[day]
            
            clock['Hours'] -= 24    #decremento del numero delle ore

    
    else:   #diminuzione minuti
        clock['Minutes'] -= number
        while clock['Minutes'] < 0: #ora precedente
            clock['Hours'] -= 1
            clock['Minutes'] += 60
        
        while clock['Hours'] < 0:
            day -= 1
            if day >= 0:
                clock['Day'] = days[day]
            else:
                day = len(days)-1   #settimana precedente
                clock['Day'] = days[day]
            
            clock['Hours'] += 24
    
    print(clock)
    return day


def main():
    day = 0
    while True:
        decision = input("A per aumentare l'orario, D per diminuirlo: ")

        if decision != 'A' and  decision != 'a' and  decision != 'D' and  decision != 'd':  #controllo del carattere
            print("Error")
            break
        elif decision != 'A' or  decision != 'a':
            number = int(input("Di quando vuoi aumentare (minuti)? "))
        elif decision != 'D' or  decision != 'd':
            number = int(input("Di quando vuoi diminuire (minuti)? "))
        
        if number < 0:  #controllo del numero per incrementare/decrementare
            print("Error")
            break
        else:
            day = clockControl(number, decision, day)
    

if __name__ == "__main__":
    main()