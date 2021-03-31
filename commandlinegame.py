import random

ans=random.randint(1,20)

print("I'am guessing numbers from 1 to 20:can you guess it correctly!")

count=0
while(True):
    count=count+1
    predic=int(input("Enter your guess:"))
    if predic > ans :
        print("the answer is too high.")
    elif predic < ans :
        print("the answer is too low.")
    else:
        print("hurrahhh!!! the predication is correct.")
        break

print("you have attempted for "+str(count)+" times.")
    


    
