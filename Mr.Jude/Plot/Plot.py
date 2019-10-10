#%% A
A. What is mean total number of steps taken per day?
For this part of the task, we ignore the missing values (NA) in the dataset.
1. Calculate the total number of steps taken per day
2. Make a histogram of the total number of steps taken each day
3. Calculate and report the mean and median of the total number of steps taken per day
#%%
import csv
import matplotlib.pyplot as plt

filename = "activity.csv"
def step_per_day():
    stepsDay = []
    with open(filename) as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        tmp = 0
        acc = 0
        while True:
            try:
                if acc % 288 == 0:
                    stepsDay.append(tmp)
                    tmp = 0
                ne = next(csvreader)[0]
                if ne != "NA":
                    tmp += int(ne)
                acc += 1
            except StopIteration:
                break
    return stepsDay

def makeplot(stepday):
    fig,axs =plt.subplots(2)
    axs[0].set_title("Step per day")
    axs[0].plot(stepday)
    axs[1].set_title("Average steps per day")
    axs[1].plot(mean(stepday))
    plt.tight_layout()
    plt.show()

def median(stepday):
    stepday.sort()
    if len(stepday)%2 == 0:
       x = len(stepday)//2
       return (stepday[x]+stepday[x+1])/2
    else :
        x = len(stepday)//2
        return stepday[x]

def mean(stepday):
    average = []
    for step in stepday:
        average.append(step/len(stepday))
    return average


def max_per_day():
    maxstepDay = []
    with open(filename) as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        acc = 0
        maxstepday = 0
        while True:
            try:
                if acc % 288 == 0: 
                    maxstepDay.append(maxstepday)
                    maxstepday = 0
                ne = next(csvreader)[0]
                if ne != "NA":
                    ne = int(ne)
                    if maxstepday < ne:
                        maxstepday = ne
                acc += 1
            except StopIteration:
                break
    return maxstepDay



makeplot(step_per_day())

print("The total median step is: ",median(step_per_day()))
print("The total number of steps taken: ",sum(max_per_day()))

#%% B
What is the average daily activity pattern? 
1. Make a time series plot of the 5-minute interval (x-axis) and the average number of steps taken,
averaged across all days (y-axis) 
2. Which 5-minute interval, on average across all the days in the dataset, contains the maximum number of
steps? 
#%% B
import csv
import matplotlib.pyplot as plt

filename = "activity.csv"

def time_series():
    with open(filename) as f:
        csvreader = csv.reader(f)
        next(csvreader)
        interval_step = [0]*288
        days = 61
        acc = 0
        while True :
            try:
                step = next(csvreader)[0]
                interval_step[acc] += int(step) if step != "NA" else 0
                acc += 1
                if acc == 288:
                    acc = 0
            except StopIteration:
                break
        return interval_step
    
def average(interval_step):
    days = 61
    averages = []
    for step in interval_step:
        averages.append(step/days)
    return averages

def makeplot():
    fig,axs =plt.subplots(2)   
    axs[0].set_title("Steps per 5 mins")
    axs[0].plot(time_series())
    axs[1].set_title("Average steps per 5 mins")
    axs[1].plot(average(time_series()))
    plt.tight_layout()
    plt.show() 
    
makeplot()

#%% C
Inputting missing values 
1. Calculate and report the total number of missing values in the dataset (i.e. the total number of rows with
NAs) 
2. Devise a strategy for filling in all of the missing values in the dataset
3. Create a new dataset that is equal to the original dataset but with the missing data filled in.
4. Make a histogram of the total number of steps taken each day and Calculate and report the mean and 
median total number of steps taken per day.
#%% C
import csv
import statistics
import re
import matplotlib.pyplot as plt
filename = "activity.csv"

def numNA():
    with open(filename) as f :
        x = f.read()
        return len(re.findall("NA",x))
        
print("Total NA in activity.csv is :",numNA())

def strategy():
    with open(filename) as f:
        x = f.read()
    with open("New Data.csv","w+") as f:
        f.write(re.sub("NA","0",x))

def getMedianMeanPerDay():
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        medianPerDay = []
        meanPerDay = []
        stepToday = []
        acc = 0
        while True:
            try:
                acc += 1
                step = next(reader)[0]
                stepToday.append(int(step) if step != "NA" else 0)
                if acc % 288 == 0:
                    stepToday.sort()
                    medianPerDay.append(statistics.median(stepToday))
                    meanPerDay.append(statistics.mean(stepToday))
                    stepToday = []
            except StopIteration:
                   break
        return medianPerDay, meanPerDay
    
def makeplot(): #cannot install pygal so i use plot instead of histogram
    median,mean = getMedianMeanPerDay()
    plt.plot(mean,c= "orange")
    plt.plot(median,c = "blue")
    plt.show()
#%% D
D. Are there differences in activity patterns between weekdays and weekends?
1. Create a new factor variable in the dataset with two levels - "weekday" and "weekend" indicating 
whether a given date is a weekday or weekend day.
2. Make a plot containing a time series plot of the 5-minute interval (x-axis) and the average number of 
steps taken, averaged across all weekdays or weekend days (y-axis).
#%% D
import csv
import matplotlib.pyplot as plt
filename = "activity.csv"
def getweek():
    weekdays, weekends = [], []
    with open(filename) as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        tmp = 0
        acc = 0
        days = 1
        while True:
            try:
                if acc % 288 == 0:
                    if days not in [6, 7]:
                        weekdays.append(tmp)
                    else:
                        weekends.append(tmp)
                    days += 1
                    if days == 8:
                        days = 1
                    tmp = 0
                ne = next(csvreader)[0]
                if ne != "NA":
                    tmp += int(ne)
                acc += 1
            except StopIteration:
                break
    return weekdays, weekends

def makeplot():
    weekdays, weekends = getweek()
    fig,axs =plt.subplots(2)   
    axs[0].set_title("Weekdays")
    axs[0].plot(weekdays,c= "black")
    axs[1].set_title("Weekends")
    axs[1].plot(weekends,c="red")
    plt.tight_layout()
    plt.show() 

makeplot()