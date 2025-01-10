spam = ["My", "name", "is", "Dhruvik Sakariya", ["1", 2]]
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3], "\n")
# print(spam[4]) // list index out of range

# it starts from backwords and the index starts from 1
# "Dhruvik Sakariya" = 1, "is" = 2
print(spam[-5]) 
print(spam[-4])
print(spam[-3])
print(spam[-2], "\n")

print(spam[4])
print(spam[4][0])
print(spam[4][1],"\n")
print(spam[4][-2])
print(spam[4][-1])

# slice
print(spam[1:4], "\n")

spam.append("e")

print(spam)
del spam[-1] # deleted the elemets from the list !

print(spam, "\n") 

looking = input("looking for something ? y/n : ")

if looking == "y":
    check = input("Enter the value: - ")
    if check in spam:
        print("It's in the list")

    else:
        print("Oops! Not available in the list !")

else:
    print("Cool, You have your results !")




print("\n\n")