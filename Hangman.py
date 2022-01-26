import random

name=input("What is your name?")

print("Good luck!", name)

words=['butterfly','school','octopus','computer','python','banana','blueberry','watermelon','breakfast','robot','tv','india']

word=random.choice(words)

print("Guess the characters of the word")

guesses=' '

turns = 5

while turns>0:
    failed=0

    for char in word:
        if char in word:
            if char in guesses:
                print(char)

            else:
                print("_")

                failed += 1
    if failed == 0:
        print("You win congratulations!!")

        print("The word is:" , word)
        break
    guess = input("guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("wrong")
        print("you have" , + turns, "more guesses")
        
        if turns == 0:
            print("You loose , better luck next time ")