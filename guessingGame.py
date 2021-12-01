import random
num = random.randint(1,9)
chance = int(5)
print(num)
enterval = int(input("Enter a value"))



while(chance > 0):
    if(enterval < num):
        print("Too low, Guess a number higher then " + str(enterval))
        if(enterval + 3 <= num):
            print("Hint: try Guessing higher by at least 3 number")
        chance = chance - 1
        enterval = int(input("Enter a value"))
    elif(enterval > num):
        print("Too high, Guess a number lower then " + str(enterval))
        if(enterval - 3 >= num):
            print("Hint: try Guessing lower by at least 3 number")
        chance = chance - 1
        enterval = int(input("Enter a value"))
    elif(enterval == num ):
        print("You Won, " + str(enterval) + " was the correct answer!")
        
        chance = -1

if(chance == 0):
    print("You lost, the number is" + num)
    chance = chance - 1

