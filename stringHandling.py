str = "Hello world!"
print(str)
print(len(str))     #print the length of the string 
print(str[10])       #return the character of given index.no
print(str[2:10])      #return the substring with start index.no and end index.no
print(str.split(" "))
para = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium dolorum placeat vel recusandae voluptas commodi in accusamus nam? Esse iste quasi modi quam in perspiciatis labore sunt reprehenderit totam ipsa?"
print(para.split(" "))

remove = "   Hello world!   "
print(remove.strip())       #removes prefix and postfix whitespaces.

print(str.replace("o","k"))     #replaces the old character with new character

print(str.lower())      #convert string into small letters
print(str.upper())      #convert string into Capital letters

print(str.title())      #The title() method returns a string where the first character in every word is upper case

language = ["HTML","CSS","React"]

print(" ".join(language))       #join the array
