'''
Author: Michele Alladio
es:
Given a moment, determine the moment that would be after a gigasecond has passed.
A gigasecond is 10^9 (1,000,000,000) seconds.
'''

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
GIGASECOND = 1000000000

def afterGigasecond(clock):
    day = clock['Day']

    clock['Seconds'] += GIGASECOND  #incremento minuti

    while clock['Seconds'] >= 60:   #se si supera il limite di minuti per ora
        clock['Minutes'] += 1 #incremento di 1 ora 
        clock['Seconds'] -= 60  #decremento dei minuti

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
    
    print(clock)


def main():
    clock = {'Day': days[0], 'Hours': 0, 'Minutes': 0, 'Seconds': 0}

    seconds = int(input("Inserisci il numero di secondi (< 60): "))
    minutes = int(input("Inserisci il numero di minuti (< 60): "))
    hours = int(input("Inserisci il numero di ore (< 24): "))
    day = input("Inserisci il giorno: (in inglese, prima lettera maiuscola): ")

    if seconds < 0 or seconds > 59 or minutes < 0 or minutes > 59 or hours < 0 or hours > 59 or day not in days:
        print("Formato del momento sbagliato.")
        return
    else:
        clock['Day'] = day
        clock['Hours'] = hours
        clock['Minutes'] = minutes
        clock['Seconds'] = seconds

        afterGigasecond(clock)
    

if __name__ == "__main__":
    main()