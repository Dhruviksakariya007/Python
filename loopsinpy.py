import random, sys
# from random import *
print("**************** Let's start with tables ****************")

# for i in range(5, -1, -1):
#     print(i)
# 5,4,3,2,1,0x

tbl = random.randint(1, 101) # generates the random numbers between 1 to ...

if tbl:
    for i in range(1, 11):
        multiplication = int(tbl)*i
        if i == 4:
            # sys.exit() used to exit from the code.
            pass
        print(str(tbl) + " x " + str(i) + " = " + str(multiplication))

        

        

# con = input("wanna continue ? y/n - ")
# if con == 'y':
#     tbl = input("Enter table - ")

# elif con == 'n':
#     print("Thank you !")


    