# More Practise question on slicing

#     String s = 'ComputerVision' Extract 'Vision' using negative indexing.
s = 'ComputerVision'
print(s[-6:])

#     String s = 'OpenAIChatGPT' Extract every 4th character starting from the first character.
s = 'OpenAIChatGPT'
print(s[::4])

#     String s = 'CyberSecurity' Create a new string by removing the first and last three characters using slicing only.
s = 'CyberSecurity'
print(s[3:10])

#     String s = 'DataVisualization' Extract the characters from the middle of the string to the end.
s = 'DataVisualization'
print(s[8:])

#     String s = 'Knowledge' Create a new string that contains all characters except every third character.
s = 'Knowledge' 
print(s[:2]+s[3:5]+s[6:8])

#     List marks = [45,56,67,78,89,91,82,73,64] Extract the first five marks in reverse order.
marks = [45,56,67,78,89,91,82,73,64] 
print(marks[:5])

#     List languages = ['Python','Java','C','C++','JavaScript','Go','Rust'] Extract only the programming languages that appear after 'C'.
languages = ['Python','Java','C','C++','JavaScript','Go','Rust']
print(languages[2:])

#     List nums=[3,6,9,12,15,18,21,24,27,30] Create a list containing every third element starting from 9.
nums=[3,6,9,12,15,18,21,24,27,30]
print(nums[2::3])

#     List animals=['Cat','Dog','Lion','Tiger','Elephant','Horse','Zebra'] Extract all elements except the middle one(s) using slicing and concatenation.
animals=['Cat','Dog','Lion','Tiger','Elephant','Horse','Zebra']
print(animals[:3]+animals[4:])

#     List values=[100,200,300,400,500,600,700] Swap only the first two and last two elements using slicing.
values=[100,200,300,400,500,600,700]
print(values[-2:]+values[2:5]+values[:2])

#     Tuple t=(11,22,33,44,55,66,77,88) Extract all elements except the first three and last two.
t=(11,22,33,44,55,66,77,88)
print(t[3:6])

#     Tuple months=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug') Extract the summer months (Apr to Jun) using slicing.
months=('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug')
print(months[3:6])

#     Tuple letters=('P','Y','T','H','O','N') Create the tuple ('N','O','H') using one slicing operation.
letters=('P','Y','T','H','O','N')
print(letters[-1:-4:-1])

#     Nested List matrix=[[2,4,6],[8,10,12],[14,16,18],[20,22,24],[26,28,30]] Extract only the first three rows.
matrix=[[2,4,6],[8,10,12],[14,16,18],[20,22,24],[26,28,30]]
print(matrix[:3])

#     Nested List records=[['A',80],['B',75],['C',90],['D',88],['E',95]] Extract the last four records using slicing.
records=[['A',80],['B',75],['C',90],['D',88],['E',95]]
print(records[1:])

#     Bytes b=b'Artificial' Extract the first six bytes.
b=b'Artificial'
print(b[:6])

#     Bytearray ba=bytearray(b'ProgrammingLanguage') Extract 'Language' using slicing.
ba=bytearray(b'ProgrammingLanguage')
print(ba[-8:])

#     Mixed data=['Python','Java','C++','SQL','HTML','CSS','JavaScript','Django'] Using slicing only:
data=['Python','Java','C++','SQL','HTML','CSS','JavaScript','Django']

    #     Extract the first four technologies.
print(data[:4])
    #     Extract the last three technologies.
print(data[-3:])
    #     Reverse the entire list.
print(data[::-1])
    #     Create a new list containing only the middle four technologies.
print(data[2:6])
