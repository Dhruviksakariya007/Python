spam = {"name" : "Dhruvik", "age" : 20}
print(f'{spam}\n')


print(f"{spam}\n")

print(spam["name"], "\n")

# search by the key only ! 
print("name" in spam, "\n")

print(spam.keys())
print(spam.values())
print(spam.items(),"\n")

for i in spam.keys():
    print(f'key = {i}')
print(f'\n')

for i in spam.values():
    print(f'value = {i}')
print(f'\n')

for k,v in spam.items():
    print(f'key : {k}, value : {v}')
print(f'\n')
    
# Returns a value of the key and key is not present then return 0
print(f'{spam.get("df", 0)}')
print(f'{spam.get("name")}')

animals = {"name": "elephent", "weight": 200, "age": 30}
animals.setdefault('color', "black")

print(f'{animals['color']}')
print(f'{animals}')

print("\n\n")
