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
    check = input("Enter the search value: - ")
    if check in spam:
        print("It's in the list\n")

    else:
        print("Oops! Not available in the list !\n")

else:
    print("Cool, You have your results !\n")

print(spam.index("Dhruvik Sakariya"), "\n")

spam.append("DK")
print(spam, "\n")

spam.insert(0, "0")
print(spam, "\n")

# sort()
# sort(reversed = True) 

# .remove("Dhruvik Sakariya") # It will only remove the first value that occurs
nm = "zophie a cat"
nm = nm[0:7] + "the" +nm[8:12]
print(nm, "\n\n")

print("**************** Another Thing ****************")

lis = [1,2,3]
cp = lis
print(f"Lis is = {lis}")
cp.append("New")
print(f"Lis is = {lis}")

print("****************")
cpp = lis.copy()
cpp.append("hl")
print(f"cpp is = {cpp}")
print(f"lis is = {lis}")

print("\n\n")

