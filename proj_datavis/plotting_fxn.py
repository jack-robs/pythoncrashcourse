#create function that plots after feeding in csv data

import csv
from matplotlib import pyplot as plt
from datetime import datetime



def plotter(filename, x_value='', y_value_one='', yvalue_two='',
            index_one='', index_two='', index_three=''):
    '''
    Plot .csv data for 1 xval and up to 2 yval, given their index 
    locations. xval must be a date
    '''
    #read out header
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        #create lists for storage
        xvals, yvals_one, yvals_two, = [], [], []
        #read in values two lists
        for row in reader:
            try:
                x_val = datetime.strptime(row[index_one], "%Y-%m-%d")
                y_val = int(row[index_two])
                y_val2 = int(row[index_three])
            except ValueError:
                print(x_val, "missing data")
            else:
                xvals.append(x_val)
                yvals_one.append(y_val)
                yvals_two.append(y_val2)
    
    #create and fill graph        
    fig = plt.figure(dpi=128, figsize=(10,  8))
    plt.plot(xvals, yvals_one, c='red', alpha=0.5)
    plt.plot(xvals, yvals_two, c='blue', alpha=0.5)
    plt.fill_between(xvals, yvals_one, yvals_two, facecolor='yellow', alpha=0.1)
    
    
    
    plt.show()

def exit_plotter():
    print("Goodbye!")

#user prompts
print("This will enter user inputs, enter 'q' to exit at any time")
active= True

while active:

    x_value = input("What is the x value name: " )
    if x_value == '':
        print("must have a x value")
        continue
    elif x_value == 'q':
        break
    
    y_value_one = input("What is the first y value name: ")
    if y_value_one == '':
        print("must have a y value")
        continue
    elif y_value_one == 'q':
        break
        
    y_value_two = input("What is the second y value name: ")
    
    index_one = int(input("What is the csv index value of the x value: "))
    if index_one == '':
        print("must have one x index value")
        continue
    if index_one == 'q':
        break
    
    index_two = int(input("What is the csv index location of the first y value: "))
    if index_two == '':
        print("must have one y index value")
        continue
    if index_two == 'q':
        break
    try:
        index_three = int(input("What is the csv index location of the second y value: "))
    except ValueError:
        pass
    filename = input("What is the full csv filename, and path relative to current directory: ")
    break

plotter(filename, x_value, y_value_one, y_value_two, index_one, index_two,
        index_three)
