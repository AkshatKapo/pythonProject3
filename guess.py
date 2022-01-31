import random


import ran as ran



class guess:

    lower=int(input("Enter the lower bound:"))
    upper=int(input("Enter the upper bound:"))

    ran=random.randrange(lower,upper)
    print(ran)
    print("You have only 3 guesses")





    i = 0

    while i<3:


        i +=1

        z = int(input("Guess the number:"))

        if z==ran:
            print("You got it")
            break
        elif z<ran:
            print("Too small")
        elif z>ran:
            print("Too big")
        if i == 3:
            print("Ooops,Correct number is", ran)
            print("Better luck next time")
            break












