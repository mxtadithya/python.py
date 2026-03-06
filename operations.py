#arithematic operations
#a=10
#b=5
#p=10
#q=3
#name='adithya'
#print(a+b)#addition
#print(a-b)#subtraction
#print(a*b)#multiplication
#print(a/b)#division
#print(p/q)#division
#print(p//q)#floor division .values ozhivakkaan
#print(p%q)#exponential 10*10*10

#print(name*2)


#assignment operators
#x=60
#x+=5 #x=x+5
#x-+5 #x=x-5
#x*=5 #x=x*5
#x/=5 #x=x/5
#x//=5 #x=x//5
#x**=5
#print('x:',x)


# Comparison operators

a=30
b=10

print(a==b) # equal to
print(a!=b) # not equal to
print(a> b) # greater than
print(a< b) # less than
print(a>=b) # greater than or equal to
print(a<=b) # less than or equal to

#logical operations

#AND   
x=10
print(x>5 and x<15) 
print(x<5 and x>15)
print(x<15 and x>30)
print(x>5 and x<3)

#OR
print(x>5 or x<15)
print(x<5 and x>15)
print(x<15 and x>30)
print(x>5 and x<3)

#NOT
is_adult=True
print(not(x>5 and x<15))
print(not(x<5 and x>15))
print(not(x<15 and x>30))
print(not(x>5 and x<3))
print(not(is_adult))


#identify operator
a=[10,11]
a=b
c=[10,11]
print(a is b)
print(a is c)
print(a is not c)

#membership operator
print(10 in [10,15,20])
print(100 not in [10,20,29])

# Bitwise operators

print(10 & 5) # bitwise and
print(10 | 5) # bitwise or
print(10 ^ 5) # bitwise xor
print(~10) # bitwise not
print(10 << 2) # bitwise left shift
print(10 >> 2) # bitwise right shift