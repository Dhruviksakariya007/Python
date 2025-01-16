import re

msg = "calling in +91 8128574360 means +91 8128574361"

phoneRegx = re.findall(r"[+]\d\d \d\d\d\d\d\d\d\d\d\d", msg) # \d is for digits

try:
    print(f'{phoneRegx}')

except:
    print(f'Phone number is not found..!')
    
