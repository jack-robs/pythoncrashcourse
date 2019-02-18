'''
Plot highs/low temps of BOS, source https://www.wunderground.com/history/,
save as a .csv
'''

'''
import modules, needed:
1) csv
2) matplotlib
3) datetime for strptime
'''
import csv
from datetime import datetime
from matplotlib import pyplot as plt



'''
parse data in csv
1) open csv, read-out the header
2) make lists to store high/lows/dates
3) for-loop through data @ index points, append into lists
4) try/except/else build in for error parsing
5) test: print out lists[] to see if stored
'''
#open csv, read-out the header row, tested/functional
filename = 'boston_weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #make lists to store data, tested/functional
    dates, highs, lows = [],[],[]
    for row in reader:
        #try/except/else
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[8])
            low = int(row[9])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

'''
make graph 
1) make graph 
2) add x1/x2/y vals
'''
fig = plt.figure(dpi=128, figsize=(10, 8))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='#00ffbd', alpha=0.1)


'''
format graph
1) title it
2) xlabel
3) xformat
4) ylabel
5) yformat
'''
title = "Daily Temperature in Boston, January 2018"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperatures (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

'''
display graph
plt.show()
'''

plt.show()

