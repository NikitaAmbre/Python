#operators
# 1. Arithmetic Operators(+,_,*,%,/)
num1 = 40
num2 = 8
print(num1 - num2)       # subtraction
print(num1 * num2)       # multiplication
print(num1 + num2)       # addition  ( we also use + to concatenate 2 strings)
print(num1 / num2)       # division  
print(num1 % num2)       # modulus (returns remainder)   

#2. Assignment Operators(=)
value = 50               # assign 
print(value)
value -= 10              # subtract and assign
print(value)

# 3. Comparison Operators(>,<,<=,>=,!=,==)
p3 = 30
p4 = 25
print(p3<p4)    # less than comparison
print(p3 > p4)  # greater than comparison
print(p3>=p4)   #greater than equal to
print(p3<=p4)   # less than equal to
print(p3==p4)   #exactly equal to or include equal
print(p3!=p4)   # not equal to 

# 4. Logical Operators (and,or,not)
x1 = 5
x2 = 15
x3 = 25
x4 = 35
print("And result :", x1 < x2 and x3 > x4)   # AND condition
print("OR Result :", x1 < x2 or x3 > x4)     # OR condition
print("not Result :", not x3 > x4)           # NOT condition

# 5. Identity Operators (is, is not)
m1 = 100
m2 = 100
print(m1 is m2)
print(m1 is not m2)

# 6. Membership Operators (in, not in)
print("Check 'a' in 'mango' :", 'a' in 'mango')
print("Check 'a' in 'mango' :", 'a' not in 'mango')

# 7. Bitwise Operators. (AND(&), OR(|), NOT(~),XOR(^), Left Shift(<<),Right shift(>>))
a=10                #binary:1010
b=4                 #binary:0100
result=a & b        # Bitwise AND (&)
result=a | b        # Bitwise OR (|)
result= ~(a + b)    # Bitwise NOT (~)   
result=a ^ b        # Bitwise XOR (^)
result=a << b       # Bitwise Left shift (<<)
result=a >> b       # Bitwise Right shift (>>)
print(result)



