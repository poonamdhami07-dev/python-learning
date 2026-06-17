#for loops
#printing number series
print("Number Series")
number = int(input("How long number series you want to print: "))
for i in range(1,number+1):
    print(i)

#printing even number series
print("Even Number Series")
number = int(input("How long even number series you want to print: "))
for i in range(1,number+1):
    if i%2==0:
        print(i)

# printing odd number series
print("Odd Number Series")
number = int(input("How long odd number series you want to print: "))
for i in range(1,number+1):
    if i%2!=0:
        print(i)

#printing specfic number series
print("Specific Number Series in differnce of 3")
number = int(input("How long number series you want to print: "))
for i in range(1,number,3):
    print(i)

#printing name and checking if it starts with vowel or consonant
print("Your name ")
name = str(input("Enter your first name: "))
if name.isalpha():
    print("My name is: " ,name)
    for i in name:
     print(i)
    
    if name.lower()[0] == "a" or name.lower()[0] == "e" or name.lower()[0] == "i" or name.lower()[0] == "o" or name.lower()[0] == "u":
        print("Your name starts with a vowel.")
    else:
        print("Your name starts with a consonant.")
else:
    print("Please enter a valid name.")


#while loops
i = 0
while i < 6:
    print(i)
    i += 1


i = int(input("Enter a number: "))
while i < 10:
    if i < 10:
        print(i)
        i += 1

count = 5
while count > 0:
    print(count)
    count -= 1
else:
    print("Countdown complete!")

#break and continue statements

for i in range(12):
    if i == 5:
        break
    #break ke niche wala code skip ho jata hai aur loop se bahar aa jata hai
    print("5 X", i, "=", 5*i)

for i in range(12):
    if i == 5:
        continue
    #continue ke niche wala code skip ho jata hai aur loop ke next iteration me chala jata hai
    print("5 X", i, "=", 5*i)