spam = "hello world"

print(f'is capitalized ? {spam.capitalize()}')

print(f'is upper ? {spam.upper().isupper()}')

print(f'is decimal ? {spam.isdecimal()}')

print(f'White space ? {spam[5].isspace()}')

print(f'is title ? {spam.istitle()}')
 
print(f'is alpha ? {spam.isalpha()}')

print(f'is alnum () alpha & number ? {spam.isalnum()}')

print(f'Starts with {spam.startswith('H')}')

print(f'Ends with {spam.endswith('d')}')

lst = ["my", "name", "is", "Dhruvik."]

print(f'{' '.join(lst)}')