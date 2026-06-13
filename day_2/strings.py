# day 2
#typecasting 
a=input("Enter a : ")
b=input("Enter b : ")
p=float(a)+float(b)
print("The sum of a and b is:", p)
print (type(a))
print (type(b))
print (type(p))

#input strings
name= input("Enter your name: ")
phone_no=input("Enter your phone no.: ")
age=input("Enter your age: ")
print("Your name is:", name)
print("Your phone no. is:", phone_no)
print("Your age is:", age)

i= '''HI 
My name is Poonam.
I am 18 years old.'''
print(i)
for character in i:
    print(character)    

#slicing
a="Poonam Dhami"
print(len(a))
print(a[0:7])
print(a[7:12])
print(a[:])
print(a[0:12:2])
print(a[0:12:5])
print(a[0:-3])
print(a[-11:-2])