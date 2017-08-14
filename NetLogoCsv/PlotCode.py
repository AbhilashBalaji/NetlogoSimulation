import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd
import csv
import statistics


def getColumn(filename, column):
    results = csv.reader(open(filename), delimiter=",")
    return [result[column] for result in results]


def PlotG():
	Tick = getColumn("El Farol Attendance-table.csv",0)
	attendance = getColumn("El Farol Attendance-table.csv",1)
	plt.figure("avg/time")
	plt.xlabel("tick")
	plt.ylabel("attendance")
	plt.plot(Tick,attendance)
	plt.show()
	print(np.std(np.array(attendance).astype(np.float))) #SD

	print("mean = ",np.mean(np.array(attendance).astype(np.float)))#mean

PlotG()	

# Generate some test data
