
#define tuple
tuple1 = (1,2,3,4,5,6,7,8,9,1,1)
print(tuple1)

print(tuple1[1])        #access the element using index number 

print(len(tuple1))      #length of the tuple

print(tuple1.count(1))      #count of the specific element

print(tuple1.index(5))      #return the index number of given element

for i in tuple1:    #loop with tuple
    print(i)
    
if 1 in tuple1:
    print('yes')
    
#another way to create a tuple using tuple constructor
tuple2 = tuple((1,2,3,4,5,6))
print(tuple2)
