##Practice question on for loop

    # 1. WAP to extract all the integer values from a list collection.
l=[12,2.3,'data',23,4+5j,[1,2,3],100]
for i in l:
    if type(i)==int:
        print(i,end=' ')

    # 2. WAP to extract all the integers which are multiple of 5 and is 3-digit number.
s=[100,25,34,110,20,30,125]
for i in s:
    if i%5==0 and len(str(i))==3:
        print(i,end=' ')

    # 3. WAP to remove duplicate values from the list.
s=[100,25,34,110,20,30,30,20,25,125]
unique=[]
for i in s:
    if i not in unique:
        unique.append(i)
print(unique)

    # 4. WAP to replace every vowel in a given string with *.
s=input('enter a string: ')
vowels='aeiouAEIOU'
for i in s:
    if i in vowels:
        s=s.replace(i,'*')
print(s)

    # 5. WAP to create a new string containing only the characters present at even index positions.
s=input('enter a string: ')
new_string=''
for i in range(0,len(s),2):
    new_string+=s[i]
print(new_string)

    # 6. WAP to extract all the negative values from a list.
s=[100,-25,34,-110,20,-30,30,-20,25,-125]
negative=[]
for i in s:
    if i<0:
        negative.append(i)
print(negative)

    # 7. WAP to create a new list containing the elements of the original list in reverse order without using slicing or reverse().
s=[100,25,34,110,20,30,30,20,25,125]
new_list=[]
for i in range(len(s)-1,-1,-1):
    new_list.append(s[i])
print(new_list)

    # 8. WAP to create a new string containing only alphabets from an alphanumeric string. 
s=input('enter an alphanumeric string: ')
new_string=''
for i in s:
    if i.isalpha():
        new_string+=i
print(new_string)