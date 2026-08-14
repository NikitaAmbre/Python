# #  80.Wap to get the following output using len function.
# #  S=’power star’
# #  Out={‘power’:5,’star’:4}
# S='power star'
# w=S.split()
# out={}
# for i in w:
#     out[i]=len(i)
# print(out)

# #  81.Wap to get the following output.
# #  S=’power star’
# #  Out={‘power’:’rewop’,’star’:’rats’}
# S='power star'
# w=S.split()
# out={}
# for i in w:
#     out[i]=i[::-1]
# print(out)

# #  82. wap to extract all the non default values from a list.
# lst=[0,1,2,3,4,5,6,7,8,9]
# n=[]
# for i in lst:
#     if i!=0:
#         n.append(i)
# print(n)

# #  83.Wap to check whether the list is homogenous or not.
# lst = [12, 3.6, 4+2j, 'python', True, [1,2,3], (1,2), {1,2}, None]
# first_type = type(lst[0])

# for i in lst:
#     if type(i) != first_type:
#         print("not homogenous")
#         break
# else:
#     print("homogenous")
        
# #  84.Wap to replace the space by * present in a string
# s = "always keep smiling"
# out = ""
# for i in s:
#     if i == " ":
#         out += "*"
#     else:
#         out += i
# print(out)

# #  85.Wap to count the number of occurrence of a specified character.
# s = "always keep smiling"
# ch = input("Enter character: ")
# count = 0
# for i in s:
#     if i == ch:
#         count += 1
# print("Occurrence:", count)

# #  86. Wap to get the following output.
# #  S=’always keep smiling’
# #  Out-‘syawla peek gnilims’
# s = "always keep smiling"
# rev = ""
# out = ""
# for ch in s:
#     if ch != " ":
#         rev = ch + rev
#     else:
#         out += rev + " "
#         rev = ""
# out += rev
# print(out)


# # 87. Wap to get the following output.
# # In=’push maadi kushi padi’
# # Out={‘push’:’ph’,’maadi’:’a’,’kushi’:’s’,’padi’:’pi’}
# In='push maadi kushi padi'
# w=In.split()
# out={}
# for i in w:
#     if i=='push':
#         out[i]='ph'
#     elif i=='maadi':
#         out[i]='a'
#     elif i=='kushi':
#         out[i]='s'
#     elif i=='padi':
#         out[i]='pi'
# print(out)

# # 88.Wap to toggle a string.
# s='PYthoN'
# out=''
# for i in s:
#     if i.isupper():
#         out+=i.lower()
#     elif i.islower():
#         out+=i.upper()
# print(out)

# # 89.Wap extract upper, lower, digit and special characters present in a string to different.
# # output variable



# # 90. Wap to get the following output.
# # S=’hai hello ‘
# # Out={‘hai’:’ai’,’hello:’eo’}

# # 91. Wap to get the following output.
# # S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org’]
# # Out=[‘com’,’py’,’html’,’org’]

# # 92. Wap to get the following output.
# # S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’]
# # Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’],
# # ’org’:[‘www’]}

# # 93.Wap to get the following output.
# # L=[‘hai’,34,3.4,’hello’,90,’byebye’]
# # Out={‘hai’:’hi’,’hello’:’ho’,’byebye’:’be’}

# # 94.wap to get the following output.
# # In=’hello’
# # Out={0:’h’,1:’e’,2:’l’,3:’l’,4:’e’}

# # 95.Wap to extract all the string values present in list only if the string is palindrome.

# # 96.Wap to return the positions of vowels present in the given string.

# # 97.Wap to check whether the given collection is having nested collection or not.

# # 98.Wap to count the number of words in a string.

# # 99.Wap to check whether the number is neon number or not.
# # N=9→9**2=81→8+1=9

# # 100.Wap to find the longest word in a string.

# # 101.Wap to replace the special character present in a string by space.

# # 102.wap to print the square of all the integers present in a list.

# # 103.Wap to extract all the odd number present at even index from a list.

# # 104.Wap to extract all the mutable values present in a tuple.

# # 105.Wap to get the following output.
# # In=’10100011231’
# # Out=’010111000’ ( 0→1 and 1→0 if it is other than 0 &1 ignore)

# # 106.Wap to get the following output.
# # In=’abacbaacc’
# # Out={‘a’:4,’b’:2,’c’:3}

# # 107.wap to extract keyvalue pair from the dictionary only if the key is Boolean datatype.




