import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd
import csv
import statistics
#strategy , tick , attendance

def getColumn(filename, column,strat):
	results = csv.reader(open(filename), delimiter=",")
	ans=[]
	for result in results:
		#print(result[0])#each row
	#	print(strat,result[0])
		if strat == int(result[0])	: #?!?!?!?!?!
			#print(result[1])
			ans.append(float(result[column]))
	return ans

def PlotG():
	Strats = [getColumn("El Farol Attendance-tableMultipleStrats.csv",0,1),getColumn("El Farol Attendance-tableMultipleStrats.csv",0,5),getColumn("El Farol Attendance-tableMultipleStrats.csv",0,10)]
	Tick = [getColumn("El Farol Attendance-tableMultipleStrats.csv",1,1),getColumn("El Farol Attendance-tableMultipleStrats.csv",1,5),getColumn("El Farol Attendance-tableMultipleStrats.csv",1,10)]
	attendance = [getColumn("El Farol Attendance-tableMultipleStrats.csv",2,1),getColumn("El Farol Attendance-tableMultipleStrats.csv",2,5),getColumn("El Farol Attendance-tableMultipleStrats.csv",2,10)]
	#print(Tick)
	plt.figure("avg/time")
	plt.xlabel("tick")
	plt.ylabel("attendance")
	std=np.std(np.array(attendance[2]).astype(np.float))
	mean=np.mean(np.array(attendance[2]).astype(np.float))
	means=[]
	for i in range(0,1001):
		means.append(mean)
	#lt.plot(Tick[0],attendance[0],label="strat1")
	#plt.plot(radius, square, marker='o', linestyle='--', color='r', label='Square')
	plt.plot(Tick[2],attendance[2],label="strat5")
	plt.plot(Tick[2],means,label="average")
	print(mean)
	#plt.plot(Tick[2],attendance[2],label="strat10")
	plt.show()
	#ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
	#Data={'tick':np.array(Tick[0]).astype(np.float),'attendance':np.array(attendance[0]).astype(np.float)}
	#df=pd.DataFrame(data=Data)
	#df=df.cumsum()
	#df.plot()
	#plt.show(

PlotG()

# Generate some test data
