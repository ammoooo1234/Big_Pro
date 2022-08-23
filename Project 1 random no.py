def check_int(a,b):
    if(a==b):
        print("true")
        quit()
    else:
        print("false")
import random
a=random.randint(0,9)
for i in range(0,9):
    b=int(input("please enter a number between 0 and 9"))
    check_int(a,b)