'''
Author: Michele Alladio
es:
Given an age in seconds, calculate how old someone would be on:

Earth: orbital period 365.25 Earth days, or 31557600 seconds
Mercury: orbital period 0.2408467 Earth years
Venus: orbital period 0.61519726 Earth years
Mars: orbital period 1.8808158 Earth years
Jupiter: orbital period 11.862615 Earth years
Saturn: orbital period 29.447498 Earth years
Uranus: orbital period 84.016846 Earth years
Neptune: orbital period 164.79132 Earth years
So if you were told someone were 1,000,000,000 seconds old, you should be able to say that they're 31.69 Earth-years old.
'''

SECONDS_PER_DAY = 86400 #secondi in un giorno
DAY_PER_YEAR = 365.25   #giorni in un anno

planets = {'Mercury':0.2408467, 'Venus':0.61519726,
           'Mars':1.8808158, 'Jupiter':11.862615, 'Saturn':29.447498,
           'Uranus':84.016846, 'Neptune':164.79132}

def calculateAge(age):
    earthYears = round(age / (DAY_PER_YEAR*SECONDS_PER_DAY), 2) #anni sulla terra (arrotondamento)
    print(f"On the Earth you're {earthYears} years old")

    for planet in planets:
        print(f"On {planet} you're {round(earthYears * planets[planet], 2)} years old: ")   #anni su ogni pianeta (arrotondamento)


def main():
    age = int(input("Inserisci un'età (in secondi): "))

    if age < 0: #controllo sull'età
        print("L'età dev'essere positiva.")
        return
    else:
        calculateAge(age)


if __name__=="__main__":
    main()