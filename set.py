set1 = {1,2,3,4,5}
set2 = {10,4,5,6,7,3}

union_result = set1 | set2      #this two is same method don't confusess
result = set1.union(set2)

intersection_result = set1 & set2

different_result = set1 - set2

print(union_result)
print(result)
print(intersection_result)
print(different_result)

for i in set1:
    print(i)
    
result = 3 in set2
print(result)

first = next(iter(set2))        # first element of the array
max = max(set2)                 # Find the maximum element of the array
min = min(set2)                 # Find the minimum element of the array

print(first)
print(max)
print(min)


my_set = {1,2,3,4,5}

my_set.add(6)               #add the element
print(my_set)
 
my_set.update({4,5,6,7,8})    #update the set 
print(my_set)


my_set.remove(4)
print(my_set)

my_set.pop()            #remove the first element
print(my_set)

my_set.clear()
print(my_set)