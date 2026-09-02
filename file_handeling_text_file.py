# #write in file

f=open('Bangalore.txt','w')
f.write('The Electronic City- Bengaluru')

f.writelines('''\n Bengaluru (also called Bangalore) is the capital of India's southern Karnataka state.
The center of India's high-tech industry, the city is also known for its parks and nightlife.
By Cubbon Park, Vidhana Soudha is a Neo-Dravidian legislative building. 
Former royal residences include 19th-century Bangalore Palace, modeled after England’s Windsor Castle, 
and Tipu Sultan’s Summer Palace, an 18th-century teak structure. ''')
f.close()


#with:

with open('Delhi.txt','w') as x:
  x.write('The Capital of India')
  x.writelines('''\n\n Delhi, India’s capital territory, is a massive metropolitan area in the country’s north. 
  In Old Delhi, a neighborhood dating to the 1600s, stands the imposing Mughal-era Red Fort, a symbol of India, 
  and the sprawling Jama Masjid mosque, whose courtyard accommodates 25,000 people. 
  Nearby is Chandni Chowk, a vibrant bazaar filled with food carts, sweets shops and spice stalls.''')


# read the file

with open('Delhi.txt','r') as v:
  #print(v.read())
  #print(v.readline())
  #print(v.readline())
  #print(v.readline())
  print(v.readlines())

  #Append

with open('Delhi.txt','a') as v:
  v.write('\n\nDelhi is very famous because it is the vibrant political capital of India '
  'and an ancient city filled with thousands of years of layered history')

#reading existing file
with open(r'C:\Users\Admin\Documents\Python_Library_Notes_QSpider\INTRO1.txt','r') as x:
  print(x.read())

 #  appending data in existing file
with open(r'C:\Users\Admin\Documents\Python_Library_Notes_QSpider\INTRO1.txt','a') as x:
  x.write('\n\n mock test is very important')

