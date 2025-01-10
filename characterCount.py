import pprint
msg = "My name is dhruvik and i'm 20 year's old !"

count = {}

for char in msg:
    # print(f'{char}')
    count.setdefault(char, 0)
    count[char] += 1

pprint.pprint(count)