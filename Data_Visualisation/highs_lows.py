#Trying to find the highest and the lowest temperatures and the associated days
#Of rainfall
from matplotlib import pyplot as plt
from datetime import datetime
import csv


#Store the file in filename object
filename = 'sitka_weather_2014.csv' 
#Open the file and store the object in f
with open(filename) as f:
    #Reader stores the object in reader variable (to use csv related functions)
    reader = csv.reader(f)
    #Next function reads the the line (only called once)
    header_row = next(reader)
    #Header row is then printed
    #Enumerate returns a (x, y) pairing over the header_row value
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    #The min temperature = index 0, max temperature = index 1
    dates, highs, lows = [], [], []

    #Run through each row in the file
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
    
        low = int(row[3])
        lows.append(low)

        high = int(row[1])  
        highs.append(high)
        


    # print(highs)

#Plot the data
fig = plt.figure(dpi = 128, figsize=(10, 6))

plt.plot(dates, lows, c="blue")
plt.plot(dates, highs, c="red")
#Draws dates diagonally
fig.autofmt_xdate()

#Format plot
plt.title("Daily high and low temperatures 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
