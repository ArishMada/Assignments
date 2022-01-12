import csv
import statistics
import pandas as pd
import matplotlib.pyplot as plt


# Creating a Function
def check_weekday(date):
    # computing the parameter date
    # with len function
    n = len(pd.bdate_range(date, date))
    if n == 0:
        return "weekend"
    else:
        return "weekday"


# create a new document with a 4th column that shows the day type as weekend or weekday
filename = 'newActivityKuDataSet.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    new = open("activity_new.csv", "w")
    new.write(str(headerRow[0]) + "," + str(headerRow[1]) + "," + str(headerRow[2]))
    new.write("\n")

    for row in reader:
        day_type = check_weekday(str(row[1]))
        if day_type == "weekend":
            new.write(str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + "weekend")
            new.write("\n")
        else:
            new.write(str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + "weekday")
            new.write("\n")

    new.close()

# Open the new document just created
newFile = "activity_new.csv"
with open(newFile) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    dictWeekdaysInterval = {}
    dictWeekendsInterval = {}
    intervals = []

    for row in reader:
        steps = row[0]
        date = row[1]
        interval = int(row[2])
        d_type = row[3]

        if d_type == "weekday":
            dictWeekdaysInterval.setdefault(interval, [])
            dictWeekdaysInterval[interval].append(int(steps))
        elif d_type == "weekend":
            dictWeekendsInterval.setdefault(interval, [])
            dictWeekendsInterval[interval].append(int(steps))

    listAveragePerIntervalWeekends = []
    listAveragePerIntervalWeekdays = []

    # append the mean for each day in a list for weekends and for weekdays
    for i in dictWeekendsInterval.keys():
        listAveragePerIntervalWeekends.append(statistics.mean(dictWeekendsInterval.get(i)))
    for i in dictWeekdaysInterval.keys():
        listAveragePerIntervalWeekdays.append(statistics.mean(dictWeekdaysInterval.get(i)))

    # plot the two curves with the same x axis could dictWeekendsInterval keys or the
    # dictWeekdaysInterval keys, they are the same
    fig, (ax1, ax2) = plt.subplots(2, sharex="all", sharey="all")
    plt.suptitle('Average Daily Activity for Weekdays and Weekends')
    ax1.plot(list(dictWeekendsInterval.keys()), listAveragePerIntervalWeekends, c='blue')
    ax1.set_title('Weekends')
    ax2.plot(list(dictWeekendsInterval.keys()), listAveragePerIntervalWeekdays, c='red')
    ax2.set_title('Weekdays')
    plt.show()
