a = 10
b = 20

a,b = b,a

print(a,b)


# using xor-operator

a = 10
b = 20

a = a^b
b = b^a
a = a^b

print(a,b)