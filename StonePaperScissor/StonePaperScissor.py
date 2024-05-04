#Lets make some stone paper scissor game ...........
import random



name = input("User whats your name : ")
print(f"Hello {name}, i hope u will like it ! \n")
pass1 = input("Enter your password : ")


def checkbox():
    try: 
        global playtime
        playtime = int(input("No. of matches you want to play : "))
    except:
        print("Error")
        checkbox()


# test
# x = random.randrange(0,3)
# print(x)

score = 0

if pass1 == "helloJ":
    
    checkbox()

    for i in range(0,playtime):

        x = random.randrange(1,4)

        print("""You have to use input as a integer (Use brain don't be confused !
                    1. Rock !
                    2. Paper !
                    3. Scissor !
              
              good luck ;) \n """)
    
        def reduceerror():
            global userinp
            try:
                userinp = int(input("What is your move (AS Integer) : "))
            except: 
                print("Value that u entered is wrong ! plz carefully enter ... \n")
                reduceerror()

        reduceerror()
                

        #if values are same !
        if userinp == x:
            print("Draw\n")

        elif userinp == 1: #rock == 1, scissor == 3
            if x == 2:
                print(" I was ---> Paper \n")
                print("You are Looser ! \n")
            elif x == 3:
                print("I was ---> Scissor \n")
                print("You Won ! \n")
                score = score + 1 

        elif userinp == 2:  # paper == 2
            if x == 1:
                print("I was ---> Rock \n")
                print("You Won !\n")
                score = score + 1 
            elif x == 3:
                print("I was --> Scissor \n")
                print("You are Looser !\n")
        
        elif userinp == 3:
            if x == 1:
                print("I was ---> Rock\n")
                print("You are Looser !\n")
            elif x == 2:
                print("I was Paper \n")
                print("You Won ! \n")
                score = score + 1 
        else:
            print("You entered a wrong input !\n")

    print("All Done : Check Your score !")
    print(f"Your score = {score} of {playtime}")

else:
    print("You entered a wrong password ! , CBI / FBI is on you now !")
