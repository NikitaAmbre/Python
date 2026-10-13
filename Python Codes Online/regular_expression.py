# # pattern matching
import re

#match gmail and print if it is valid. 
# Eg: 'ishanibanerjee@gmail.com'---Valid  
# 'ishanibanerjee@outlook.com'---Invalid
# \w {[A-Za-z0-9]}\w {@gmail.com}
text=input("Enter your email id: ")
pattern='[A-Za-z0-9]+@gmail.com'
s=re.findall(pattern,text)
if s:
    print("Valid email id")
else:
    print("Invalid email id")


#match website and print if it is valid or not.
#eg: 'www.google.com'--valid
#eg: 'www.yahoo.in'--not valid

text1=input("Enter your website name: ")
pattern1='www\.[A-Za-z0-9]+\.com'
s1=re.findall(pattern1,text1)
if s1:
    print("Valid website name")
else:
    print("Invalid website name")   