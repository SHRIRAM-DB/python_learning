
#For loop 

str = "" 
n = 4
for i in range(0,n):
    str+="*"
    print(str)

for i in range(5):
    print(i)
    
print("-------------------------------------------")

for i in range(1,10,2):
    print(i)
    
# While loop
print('-------------------------------------------')
i = 1               #Initilization
while i < 10:       #Condition
    print(i)
    i+=1            #Increment / Decrement
    

#reverse count
for i in range(9,-1,-1):
    print(i)
    
#reverse the array
arr = [1,2,3,4,5,6,7,8,9,0]

for i in arr[::-1]:
    print(i)

# dynamic value in while loop   
count = 0
while count < 5:
    print(f"count: {count}")
    count+=1
    
# dynamic value in for loop
fruits = ["apple","orange","mango","cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
    
