import random

name = raw_input("What is your name? ")
print "hello, %s" %(name)

number = random.randint(1, 100)
print number

guess = None
while guess != number:
    try:
        guess = int(raw_input("Please guess a number from 1-100: "))
        if guess > 100 or guess < 1:
            print "Your guess is not between 1-100."
        elif guess > number:
            print "Your guess is too high."
        elif guess < number:
            print "Your guess is too low."
        else:
            print "Congratulations!"
            break
    except ValueError:
        print ("Oops that was not a valid number, try again.")
