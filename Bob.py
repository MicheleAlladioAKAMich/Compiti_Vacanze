'''
Author: Michele Alladio
es: 
Bob is a lackadaisical teenager. In conversation, his responses are very limited.

Bob answers 'Sure.' if you ask him a question, such as "How are you?".

He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).

He answers 'Calm down, I know what I'm doing!' if you yell a question at him.

He says 'Fine. Be that way!' if you address him without actually saying anything.

He answers 'Whatever.' to anything else.

Bob's conversational partner is a purist when it comes to written communication and always follows normal rules regarding sentence punctuation in English.
'''

capitalLetters = ['A','B','C','D','E','F','G','H','I','J','K','L',
            'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','?','!','.']

def BobAnswer(phrase):

    yell = True #controllo per le lettere maiuscole

    for character in phrase:
        if character not in capitalLetters: #se almeno una lettera non è nella lista non viene considerato un urlo
            yell = False
            break
        
    #se la frase è tutta in lettere maiuscole
    if yell == True:
        if phrase[-1] == '?':   #ed è una domanda
            print("Calm down, I know what I'm doing!")
        else:
            print('Whoa, chill out!')

    #se la frase è una domanda
    elif phrase[-1] == '?':
        print('Sure.')
    elif phrase == 'bob' or phrase == 'Bob' or phrase == 'BoB': #se la frase è semplicemente il suo nome
        print('Fine. Be that way!')
    else:
        print('Whatever.')


def main():
    while True:
        phrase = input("Cosa vuoi dire a Bob (esc per uscire dalla conversazione): ")
        
        if phrase == 'esc' or phrase == 'ESC':  #uscita dalla conversazione
            break
        else:
            BobAnswer(phrase)

if __name__ == "__main__":
    main()