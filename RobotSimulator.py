"""
Author: Michele Alladio
es: 
Write a robot simulator.

A robot factory's test facility needs a program to verify robot movements.

The robots have three possible movements:

turn right
turn left
advance
Robots are placed on a hypothetical infinite grid, facing a particular direction (north, east, south, or west) at a set of {x,y} coordinates, e.g., {3,8}, with coordinates increasing to the north and east.

The robot then receives a number of instructions, at which point the testing facility verifies the robot's new position, and in which direction it is pointing.

The letter-string "RAALAL" means:
Turn right
Advance twice
Turn left
Advance once
Turn left yet again
Say a robot starts at {7, 3} facing north. Then running this stream of instructions should leave it at {9, 4} facing west.
"""

cardinalPoints = ['North', 'East', 'South', 'West']
coordinates = [0, 0]

def robotMovement(command, direction):

    for character in command:   #controllo per comandi con minimo 1 carattere

        #se la direzione esce dalla portata della lista viene ridimensionata 
        if direction > len(cardinalPoints)-2:   
            direction -= len(cardinalPoints)
        elif direction < 0:
            direction += len(cardinalPoints)

        if character == 'A':    #avanzamento
            #aggiornamento delle coordinate in base alla direzione
            if cardinalPoints[direction] == 'North':
                coordinates[0] += 1
            elif cardinalPoints[direction] == 'South':
                coordinates[0] -= 1
            elif cardinalPoints[direction] == 'East':
                coordinates[1] += 1
            elif cardinalPoints[direction] == 'West':
                coordinates[1] -= 1
        
        elif character == 'R':  #gira a destra
            direction += 1
        elif character == 'L':  #gira a sinistra
            direction -= 1

    print(f"Robot coordinates: {coordinates}, he's pointing at {cardinalPoints[direction]}")

    return direction
            

def main():
    direction = 0
    while True:
        command = input("Inserisci un comando o una stringa di comandi (esc per uscire): ").upper() 

        if command == 'ESC':    #controllo per l'uscita
            break
        else:
            direction = robotMovement(command, direction)


if __name__ == "__main__":
    main()