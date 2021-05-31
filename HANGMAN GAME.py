while True:
    print('\nWelcome to the HANGMAN game')
    word=list(input('Enter an word'))
    guess=list('-'*len(word))
    count=0
    print(guess)
    while True:
        user_guess=input('\nenter your guess:  ').lower()
        while user_guess in word:
            letter_index=word.index(user_guess)
            guess[letter_index]=user_guess
            word[letter_index]=''
        else:
            if user_guess in guess:
                pass
            else:
                print('\nwrong guess')
                count+=1
        print(guess)        
        if count<3 and word==['']*7:
            print ('\nCONGRATULATIIONS YOU HAVE WON\n')
            break
        elif count==3 and word!=list(''*len(guess)):
            print('\n You Have lost')
            break
    new_game=input('Do You Want To Play Again? Y or N: ')
    if new_game[0].lower()=='y':
        continue
    else:
        break
        



