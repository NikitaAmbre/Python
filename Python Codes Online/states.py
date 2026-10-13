'''
class qspiders:
    qsp_addr = 'hadapsar'
    branch_head = 'chandrashekhar sir'
vishal = qspiders()
rajat = qspiders()

#print class and object dictionary
print(qspiders.__dict__)   #{'qsp_addr': 'hadapsar',
                            #'branch_head': 'chandrashekhar sir'}
print(vishal.__dict__)     #{}
print(rajat.__dict__)      #{}

#create object members
vishal.name = 'vishal'
vishal.phno = 1234

rajat.name = 'rajat'
rajat.phno = 5678

print(vishal.__dict__)     #{'name': 'vishal', 'phno': 1234}
print(rajat.__dict__)      #{'name': 'rajat', 'phno': 5678}

#access class members
print(qspiders.qsp_addr, qspiders.branch_head)   #hadapsar chandrashekhar sir
print(vishal.qsp_addr, vishal.branch_head)       #hadapsar chandrashekhar sir
print(rajat.qsp_addr, rajat.branch_head)         #hadapsar chandrashekhar sir


#access object members
print(vishal.name, vishal.phno)    #vishal 1234
print(rajat.name, rajat.phno)      #rajat 5678

#modify class member wrt class
qspiders.qsp_addr = 'baner'
qspiders.branch_head = 'divya'

print(qspiders.__dict__)    #{'qsp_addr': 'baner', 'branch_head': 'divya'}

print(qspiders.qsp_addr, qspiders.branch_head)    #baner divya
print(vishal.qsp_addr, vishal.branch_head)        #baner divya
print(rajat.qsp_addr, rajat.branch_head)          #baner divya

#modify object members
vishal.name = 'vishal mahadik'
rajat.name = 'rajat kumar'

vishal.phno = 1357
rajat.phno = 9876

print(vishal.__dict__)   #{'name': 'vishal mahadik', 'phno': 1357}
print(rajat.__dict__)    #{'name': 'rajat kumar', 'phno': 9876}

print(vishal.name, vishal.phno)   #vishal mahadik 1357
print(rajat.name, rajat.phno)     #rajat kumar 9876

#create new object member
vishal.sid = 11
rajat.sid = 12

print(vishal.__dict__)   #{'name': 'vishal mahadik', 'phno': 1357, 'sid': 11}
print(rajat.__dict__)    #{'name': 'rajat kumar', 'phno': 9876, 'sid': 12}

print(vishal.name, vishal.phno, vishal.sid)   #vishal mahadik 1357 11
print(rajat.name, rajat.phno, rajat.sid)     #rajat kumar 9876 12

#modify class member wrt object
vishal.branch_head = 'nandish sir'

print(qspiders.qsp_addr, qspiders.branch_head)    #baner divya
print(vishal.qsp_addr, vishal.branch_head)        #baner nandish sir
print(rajat.qsp_addr, rajat.branch_head)          #baner divya

print(vishal.__dict__)   #{'name': 'vishal mahadik', 'phno': 1357, 'sid': 11,
                         #'branch_head': 'nandish sir'}

#create new class member
qspiders.hr = 'nik'

print(qspiders.qsp_addr, qspiders.branch_head, qspiders.hr)    #baner divya nik 
print(vishal.qsp_addr, vishal.branch_head, vishal.hr)        #baner nandish sir nik
print(rajat.qsp_addr, rajat.branch_head, rajat.hr)          #baner divya nik

#create new class member wrt object
rajat.trainer = 'pradutt'

print(rajat.__dict__)  #{'name': 'rajat kumar', 'phno': 9876,
                       # 'sid': 12, 'trainer': 'pradutt'}
#print(qspiders.trainer)    -----> error
'''




#method - 1
'''
class bank:
    bank_name = 'pnb'
    bank_branch = 'pune'

c1 = bank()
c1.name = 'rohan'
c1.age = 22
c1.balance = 100000

c2 = bank()
c2.name = 'om'
c2.age = 22
c2.balance = 200000

print(bank.__dict__)     #{'bank_name' : 'pnb', 'bank_branch' : 'pune'}
print(c1.__dict__)       #{'name' : 'rohan', 'age' : 22, 'balance' : 100000}
print(c2.__dict__)       #{'name' : 'om', 'age' : 22, 'balance' : 200000}
'''


#method - 2
'''
class bank:
    bank_name = 'pnb'
    bank_branch = 'pune'

c1 = bank()
c2 = bank()

def to_initialize(obj, name, age, balance):
    obj.name = name
    obj.age = age
    obj.balance = balance

to_initialize(c1, 'rohan', 22, 100000)
to_initialize(c2, 'om', 22, 200000)

print(bank.__dict__)     #{'bank_name' : 'pnb', 'bank_branch' : 'pune'}
print(c1.__dict__)       #{'name' : 'rohan', 'age' : 22, 'balance' : 100000}
print(c2.__dict__)       #{'name' : 'om', 'age' : 22, 'balance' : 200000}
'''



#method - 3
'''
class bank:
    bank_name = 'pnb'
    bank_branch = 'pune'

    def to_initialize(obj, name, age, balance):
        obj.name = name
        obj.age = age
        obj.balance = balance
        
c1 = bank()
c2 = bank()

bank.to_initialize(c1, 'rohan', 22, 100000)
bank.to_initialize(c2, 'om', 22, 200000)

print(bank.__dict__)     #{'bank_name' : 'pnb', 'bank_branch' : 'pune'}
print(c1.__dict__)       #{'name' : 'rohan', 'age' : 22, 'balance' : 100000}
print(c2.__dict__)       #{'name' : 'om', 'age' : 22, 'balance' : 200000}
'''
