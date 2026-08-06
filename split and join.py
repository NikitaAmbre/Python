x=['pro1.html','file.txt','google.com','yahoo.in']
#out={'html':'pro1','txt':'file','com':'google','in':'yahoo'}
out={}

for i in x:
    l=i.split('.')
    out[l[1]]=l[0]
print(out)

p = 'example on for loop'
#out='ee on fr lp'
words = p.split()
out = []
for i in p:
    out.append(i[0] + i[-1])
print(" ".join(out))


s='abcaabccbbb'
# out={'a':3,'b':5,'c':3}
out={}
for i in s:
    if i in out:
        out[i]=out[i]+1
    else:
        out[i]=1
print(out)


l=['i@gmail.com','r@yahoo.com','b@qspiders.in']
# output=['gmail.com','yahoo.com','qspiders.in']
out=[]
for i in l:
    out.append(i.split('@')[1])
print(out)

s='aPPlE#23'
# out={'a':'A','P':'p','l':'L','E':'e'}
out={}
for i in s:
    if i.isalpha():
        if i.isupper():
            out[i]=i.lower()
        else:                       
            out[i]=i.upper()
print(out)

l=['p1.py','file2.txt','file1.py','google.com','data.txt','yahoo.com']
# out={'py':['p1','file1'],'txt':['file2','data'],'com':['google','yahoo']}
out={}
for i in l:     
    l1=i.split('.')
    if l1[1] in out:
        out[l1[1]].append(l1[0])
    else:
        out[l1[1]]=[l1[0]]
print(out)

s='aPPlE#23'
# out='AppLe#23'
out=''
for i in s:
    if i.isalpha():
        if i.isupper():
            out+=i.lower()
        else:                       
            out+=i.upper()
    else:
        out+=i
print(out)