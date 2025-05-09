our_password = "shriram"
your_password = ""
max_try = 5
try_count = 0
password = False

while try_count != max_try:
    your_password = input("what is your password")
    try_count+=1
    if(your_password == our_password):
        password = True
        print("access granted")
        break
    
if not password:
    print("access blocked")
    
