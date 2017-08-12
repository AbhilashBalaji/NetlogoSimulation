import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
#import pandas as pd
import csv
import statistics
#strategy , tick , attendance

def getColumn(filename, column,strat):
    results = csv.reader(open(filename), delimiter=",")
    ans=[]
    for result in results:
        for i in range(0,999):
            if result[column] ==strat: #?!?!?!?!?!
                ans.append(result[i,column])

    return ans

def PlotG():
    Strats = getColumn("El Farol Attendance-tableMultipleStrats.csv",0,1)
    Tick = getColumn("El Farol Attendance-tableMultipleStrats.csv",1,1)
    attendance = getColumn("El Farol Attendance-tableMultipleStrats.csv",2,1)
    print(Strats)
    plt.figure("avg/time")
    plt.xlabel("tick")
    plt.ylabel("attendance")
    plt.plot(Tick,attendance)
    plt.show()
    print(np.std(np.array(attendance).astype(np.float))) #SD
    print("mean = ",np.mean(np.array(attendance).astype(np.float)))#mean

PlotG()

# Generate some test data
