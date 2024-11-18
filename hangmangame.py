def find_indices(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

import random
wordslist =['adipose', 'appoint', 'braised', 'bovines', 'chalice', 'certify', 'decades'
            'decline', 'eggnogs', 'ellipse', 'fluency', 'foaming', 'grottos', 'groused',
            'honeyed', 'hotcake', 'ionized', 'integer', 'jumbled', 'juryman', 'karaoke',
            'ketchup', 'lesbian', 'libeled', 'mafiosi', 'maggots', 'nauseas', 'neutral',
            'outcast', 'oversee', 'plumped', 'ponchos', 'quintet', 'quilled', 'rackets',
            'rainbow', 'sanctum', 'scarves', 'textual', 'thumper', 'timpani', 'unboxed',
            'vendors', 'vicomte', 'voucher', 'visuals', 'wannabe', 'western', 'xeroxed',
            'yoghurt', 'yodeler', 'zealous', 'zoology']
randomword=wordslist[random.randint(0, 52)]
guessedletters=[]
lives=7
count = 0
finished = False
wordtoguess = '_______'
print ("Guess this word {} ".format(wordtoguess))
print("You currently have {} guesses left ".format(lives))
while lives >0 and finished == False:
    guess = input("What's your guess of alphabet? ")
    letters_randomword = list(randomword)
    if guess in letters_randomword and guess not in guessedletters:
        print("congrats you guessed correctly!")
        guessedletters.append(guess)
        indexes_ofguess =find_indices(letters_randomword, guess)
        count = count +1

        list_wordtoguess = list(wordtoguess)
        for num in indexes_ofguess:
            list_wordtoguess[num] = guess
        wordtoguess = ''.join(list_wordtoguess)
        print ("The current word is {} ".format(wordtoguess))
    elif guess in letters_randomword and guess in guessedletters:
        print("you've previously guessed this letter!")
    else:
        lives =lives-1
        print ("wrong letter, you currently have {} lives".format(lives))
        
    if count == 7:
        finished = True

if count ==7:
    print("Congrats ")
else:
    print("Sorry try again ")
print ("The word is {} ".format(randomword))    
