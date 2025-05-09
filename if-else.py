# if-else Statement

house = True
if(house):
    print("I own a small house")
else:
    print("I don't own a small house")
    
a = 10
b = 20

if a < b:
    print("B is greater than A")
else:
    print("A is greater than B")
    
score = 80

if score >= 90:
    print("A grade")
elif score < 90 and score >= 70:
    print("B grade")
elif score < 70 and score >= 50:
    print("C grade")
elif score < 50 and score > 35:
    print("D grade")
else:
    print("E grade")    



# find the biggest number 
x = 90366
y = 90943
z = 90742

if(x>y and x>z):
    print("X is the biggest number")
elif y>x and y>z:
    print("Y is the biggest number")
else:
    print("Z is biggest number")