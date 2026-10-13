# Practice Questions on while loop

#     WAP to find the product of individual digits in a given integer .(multiplication of digits)
n=int(input('enter a number: '))
p=1
while n>0:
    d=n%10
    p*=d
    n=n//10
print('product of digit : ',p)

#     WAP to find the sum of 'n' natural numbers.)
n = int(input("Enter the value of n: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print("Sum of first", n, "natural numbers =", sum)

#     WAP to find the sum of the values in the even index position.
#Eg: n=123456 1+3+5=9
num=input('enter a number: ')
i=0
sum=0
while i < len(num):
    sum=sum+int(num[i])
    i=i+2
print('sum of values in the even index: ',sum)

#     WAP to extract lowercase character from the given string.
s=input('enter a string: ')
i=0
while i<len(s):
    if s[i].islower():
        print(s[i])
    i=i+1

#     WAP to find the product of all the float number present in the odd index position in a given tuple .
t=(1,2.2,3.4,4,5.2,9.8,5.7,3.9)
p=1
i=1
while i < len(t):
    if type(t[i])==float:
        p=p*t[i]
    i=i+2
print('product of float number in odd index position:',p)
