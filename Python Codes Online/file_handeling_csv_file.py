import csv

# Q1 STUDENT DETAILS

#WRITE A CSV FILE

with open('Student_details.csv','w') as d:
  w=csv.writer(d)  #writer(): allows us to write in the file
  w.writerow(['Name','class','section','roll','marks'])

  w.writerows([['Sneha',12,'A',1,67],
               ['Rashmi',12,'A',2,78],
               ['Puja',12,'A',3,89]])

print("CSV file created successfully!")

#read a csv file
with open('Student_details.csv','r') as r:
  read=csv.reader(r)  #reader will give us access to read the file
  for i in read:
    if i:  #it will skip the empty lines
      print(i)


#append data in csv file
with open('Student_details.csv','a') as d:
  w=csv.writer(d)  #writer(): allows us to write in the file
  w.writerow(['Ishani',12,'A',4,70])



# Q2 EMPLOYEE DETAILS

#write a file in csv format

with open ('employee_details.csv','w') as s:
  w=csv.writer(s)  #writer(): allows us to write in the file
  w.writerow(['Name','Department','Salary','Experience'])

  w.writerows([['Ridha','HR',50000,2],
               ['Roshan','IT',60000,3],
               ['Kajal','Finance',70000,4]])
  
  print("CSV file created successfully!")

#read the file
with open('employee_details.csv','r') as r:
    read=csv.reader(r)
    for i in read:
      if i:
        print(i)

#append the file
with open ('employee_details.csv','a') as a:
    a=csv.writer(a)
    a.writerow(['Rohit','IT',80000,5])
print("Data appended successfully!")

    