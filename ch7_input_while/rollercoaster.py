#05.09.2018 Ch7 input()

#using int() for input() programs

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
    

#nest int(input())

age = int(input('What is your age '))
print(age > 22)
