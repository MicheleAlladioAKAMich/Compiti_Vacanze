'''
Author: Michele Alladio
es: 
Tally the results of a small football competition.
Based on an input file containing which team played against which and what the outcome was, create an output string with a table like this:

Team                           | MP |  W |  D |  L |  P
Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
Blithering Badgers             |  3 |  1 |  0 |  2 |  3
Courageous Californians        |  3 |  0 |  1 |  2 |  1

What do those abbreviations mean?

MP: Matches Played
W: Matches Won
D: Matches Drawn (Tied)
L: Matches Lost
P: Points
A win earns a team 3 points. A draw earns 1. A loss earns 0.

The outcome should be ordered by points, descending.
'''

import csv

def fileReader():
    file = open("Matches.csv", "r")  #apertura file  

    results = []

    for row in file:
        lista = row[:-1].split(",")
        results.append({"team1":lista[0],"team2":lista[1],"result":lista[2]})  #crea la lista di dizionari
    
    return results

def createRanking(results):
    ranking = []

    for row in results:
        #vittoria
        if row['result'] == 'win':
            #variabili per il controllo dell'eventuale presenza di una o dell'altra squadra all'interno della classifica
            check1 = False
            check2 = False
            #ciclo la classifica e controllo i nomi
            for k in ranking:
                #se un team è presente aggiorno i suoi valori
                if row['team1'] == k['team']:
                    check1 = True
                    k['MP'] += 1
                    k['W'] += 1
                    k['P'] += 3
                
                if row['team2'] == k['team']:
                    check2 = True
                    k['MP'] += 1
                    k['L'] += 1

            #se un team non è presente 
            if not check1:
                ranking.append({'team':row['team1'], 'MP':1, 'W':1, 'D':0, 'L':0, 'P':3})
            if not check2:
                ranking.append({'team':row['team2'], 'MP':1, 'W':0, 'D':0, 'L':1, 'P':0})

        #pareggio
        elif row['result'] == 'draw':
            check1 = False
            check2 = False
            for k in ranking:
                if row['team1'] == k['team']:
                    check1 = True
                    k['MP'] += 1
                    k['D'] += 1
                    k['P'] += 1
                
                if row['team2'] == k['team']:
                    check2 = True
                    k['MP'] += 1
                    k['D'] += 1
                    k['P'] += 1
            
            if not check1:
                ranking.append({'team':row['team1'], 'MP':1, 'W':0, 'D':1, 'L':0, 'P':1})
            if not check2:
                ranking.append({'team':row['team2'], 'MP':1, 'W':0, 'D':1, 'L':0, 'P':1})

        #sconfitta
        elif row['result'] == 'loss':
            check1 = False
            check2 = False
            for k in ranking:
                if row['team1'] == k['team']:
                    check1 = True
                    k['MP'] += 1
                    k['L'] += 1
                
                if row['team2'] == k['team']:
                    check2 = True
                    k['MP'] += 1
                    k['W'] += 1
                    k['P'] += 3
            
            if not check1:
                ranking.append({'team':row['team1'], 'MP':1, 'W':0, 'D':0, 'L':1, 'P':0})
            if not check2:
                ranking.append({'team':row['team2'], 'MP':1, 'W':1, 'D':0, 'L':0, 'P':3})

        
    rankingByPoints = reordering(ranking)   #riordinamento della classifica in base ai punti

    return rankingByPoints
        

def reordering(ranking):
    rankingByPoints = []
    maxPoints = -1

    while ranking:
        #cerco il/i team con il punteggio maggiore
        for team in ranking:
            if team['P'] > maxPoints:
                maxPoints = team['P']

        for team in ranking:
            #aggiungo il/i team trovati nella classifica secondo i punti e li rimuovo da quella provvisoria
            if team['P'] == maxPoints:
                rankingByPoints.append({'team':team['team'], 'MP':team['MP'], 'W':team['W'], 'D':team['D'], 'L':team['L'], 'P':team['P']})
                ranking.remove(team)
        
        maxPoints = -1   #azzero la soglia di ricerca

    return rankingByPoints



def main():
    results = fileReader()
    rankingByPoints = createRanking(results)

    for team in rankingByPoints:
        print(f"Team: {team['team']}, Matches played: {team['MP']}, Matches won: {team['W']}, Matches drawn: {team['D']}, Matches loss: {team['L']}, Points:{team['P']}")    #li scrivo nel file'''


if __name__ == "__main__":
    main()
