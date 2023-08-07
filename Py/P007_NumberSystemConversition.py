x = 21
print(x)
print(bin(x))
print(hex(x))
print(oct(x))

print(0b1010)
print(0x12)
print(0o23)

# complex number
p = 2
q = 5
print(complex(p, q))
r = complex(q, p)
print(r)
print(type(r))

# boolean type
c = p > q
print(c, type(c))
c = q > p
print(c, type(c))



# Output:
# 21
# 0b10101
# 0x15
# 0o25
# 10
# 18
# 19
# (2+5j)
# (5+2j)
# <class 'complex'>
# False <class 'bool'>
# True <class 'bool'>