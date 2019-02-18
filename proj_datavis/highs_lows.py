import csv
from datetime import datetime

from matplotlib import pyplot as plt

#Get dates, high, and low temperatures from file 
filename1 = 'death_valley_2014.csv'
with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates_dv, highs_dv, lows_dv = [], [], []
    for row in reader: 
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_dv.append(current_date)
            highs_dv.append(high)
            lows_dv.append(low)
        
filename2 = 'sitka_weather_2014_2.csv'
with open(filename2) as f:
    reader = csv.reader(f)matplotlib, plot, 
    header_row = next(reader)
    
    dates_sk, highs_sk, lows_sk = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates_sk.append(current_date)
            highs_sk.append(high)
            lows_sk.append(low)
        
#plot same axis
fig = plt.figure(dpi=128, figsize=(10, 6))
#plot DV highs 
plt.plot(dates_dv, highs_dv, c='#ff0000', alpha=0.5)
#plot DV lows
plt.plot(dates_dv, lows_dv, c='#ff9d00', alpha=0.5)
#plot SK highs
plt.plot(dates_sk, highs_sk, c='#00fff9', alpha=0.5)
#plot SK lows
plt.plot(dates_sk, lows_sk, c='#0037ff', alpha=0.5)
#fill DVs
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor='#f1c200', alpha=0.1)
#fill SKs
plt.fill_between(dates_sk, highs_sk, lows_sk, facecolor='#27c2d5', alpha=0.1)



#format plot
title = "Daily high and low temperatures - 2014\nDeath Valley, CA and Sitka, AK"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim([0, 1000])

plt.show()
