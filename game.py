import random

name = raw_input("What is your name? ")
print "hello, %s" %(name)
number = random.randint(1, 100)
print number
guess = None
while guess != number:
    guess = raw_input("Please guess a number from 1-100: ")
    if int(guess) > number:
        print "Your guess is too high."
    elif int(guess) < number:
        print "Your guess is too low."
    else:
        print "Congratulations!"
        break