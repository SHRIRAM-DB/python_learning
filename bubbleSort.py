arr = [2,5,3,1,4]
count = 1
while count > 0:
    count = 0
    for i in range (len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            count=count+1
                     
print(arr)

