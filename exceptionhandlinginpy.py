def division(a):
    try:
        return 42/a
    except:
        print("Error Occured..!")

print(division(2))
print(division(0))
print(division(3))


cats = input("Enter the number of cats: ")
try:
    if int(cats) >= 4:
        print("That's a lot of cats!")
    
    else:
        print("That's not that many cats!")

except:
    print("You didn't enter a number..!")