#20.09.2018
'''
1) problem: User providing text instead of numbers when asked for numerical input
2) if try to convert txt -> int, ValueError
3) Program:
    -prompt for 2x numbers
    -add them together, print a result
    -catch ValueError w/ try-except-else, print error message 
'''

def add_numbers():
    print("We're going to add 2 numbers together")
    
    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        try:
            answer = int(first_number) + int(second_number)
        except ValueError:
            print("You can't enter a letter!")
        else:
            print(answer)
                
add_numbers()
