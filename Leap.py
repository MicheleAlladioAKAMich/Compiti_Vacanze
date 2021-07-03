'''
Author: Michele Alladio
es:
Given a year, report if it is a leap year.

The tricky thing here is that a leap year in the Gregorian calendar occurs:

on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.
'''

def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year") #se l'anno è divisibile per 4 , per 100 e per 400
            else:
                print(f"{year} isn't a leap year")  #se l'anno è divisibile per 4 e per 100
        else:
            print(f"{year} is a leap year") #se l'anno è divisibile per 4 
    else:
        print(f"{year} isn't a leap year")  #se l'anno non è divisibile per 4 

def main():
    year = int(input("Inserisci un anno: "))

    leap(year)

if __name__ == "__main__":
    main()

