#print in console numbers from 1 to 10
for i in range(1,11,):
    print(i)


for i in range(1,21,2):
    print(i)


print ( list(range(1,10,1)) )
print ( list(range(10,1,-1)) )

for el in 'abc':
    print(el) 


#Nested for loops
for i in range(5):
        for j in range(3):
             print(i,j)
        

for i in range(5):
     if i==3:
        continue
     print(i)


for i in range(5):
     if i==3:
        break
     print(i)


while 