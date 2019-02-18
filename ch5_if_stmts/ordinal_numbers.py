#Exercise 5-11 Ordinal Numbers, 1st, 2nd, 5th, etc


#store numbers 1-9 in a list

number_list = [number for number in range(1, 10)]

#loop through list, change to ordinals:




for number in number_list:
    if number < 4:
        print(str(number) + 'st')
    else:
        print(str(number) + 'th')
