arr = ['a','b','c','d','e']

print(arr)

arr[3] = 's'    #Replace an element from array
print(arr)

x = arr.index('c')      #find the index number of an element
print(x)

y = arr.append('f')     #append an element of the array
print(arr)

arr.insert(3,'k')       #insert an element on a specfic index number
print(arr)

arr.extend(['m',"k",'l'])         # add one and more element
print(arr)

#for loop
for i in arr:       #for(i=0;i<arr.length;i++)
    print(i)
    
if 'a' in arr:
    print("yes")
else:
    print('no')

    
num = [1,2,3,4,5,6]
print(num)

num.remove(4)       #using remove()
print(num)

num.pop(1)      #using pop() with index number
print(num)

num.pop()       #using pop() without index number
print(num)

del arr[1]      #using del keyword with index number
print(arr)

#del() deletes the variable and the array, while clear() clears the array but does not delete it.

del arr # delete whole arr
# print(arr)

num.clear()
print(num)

arr = ['a','b','c','d','e']

arr1 = arr.copy()      #using copy
print(arr1)

arr2 = list(arr)        #using list() constructor
print(arr2)


#list limit

array = ["apple","orange","mango","pineapple","grapes","lemon","papaya","dragonFruit"]

print(array[2:6])

print(array[2:])       #it start from 2 and print the all element