varA = 123
varB = '123'

print(type(varA) == "<type 'str'>")
print(type(varB))

if type(varA) == type('str') or type(varB) == type('str'):
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    print('smaller')