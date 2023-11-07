#Lets make some stone paper scissor game ...........
import random



name = str(input("User whats your name : "))
print(f"Hello {name}, i hope u will like it ! \n")
pass1 = str(input("Enter your password : "))



playtime = int(input("No. of matches you want to play : "))

# test
# x = random.randrange(0,3)
# print(x)

score = 0

if pass1 == "helloJ":
    

    for i in range(0,playtime):

        x = random.randrange(1,4)

        print("""You have to use imput a integer (be use brain dont be confused !
                    1. Rock !
                    2. Paper !
                    3. Scissor !
              
              good luck )\n """)

        userinp = int(input("What is you move (AS Integer) : "))

        #if values are same !
        if userinp == x:
            print("Draw")

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
                print("I was ---> Rock")
                print("You are Looser !\n")
            elif x == 2:
                print("I was Paper \n")
                print("You Won ! \n")
                score = score + 1 
        
        else:
            print("You entered a wrong input !")


print(f"Your score = {score} of {playtime}")
