import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd
import csv
import statistics
 

def getTTicks():
	results = csv.reader(open(filename), delimiter=",")
	Ticks=[]
	
	for result in results:
		Ticks.append(float(result[0]))
	return Ticks


def getColumn(filename,parameter):
	results = csv.reader(open(filename), delimiter=",")
	ans=[]
	indx=getIndex(filename,parameter)
	for result in results:
		ans.append(float(result[indx]))
	return ans


def getIndex(filename,parameter):
	results = csv.reader(open(filename), delimiter=",")
	flag =0
	result=results[0]
	for i in  range(result):
		if(parameter==result[i]):
			return i
			flag+=1
	if flag!=1:
		print("No header of same name or too many")
		
def exportCSV(ans,Ticks,parameter ):
     with open(str(parameter+'.csv'),'w') as csvfile:
        fieldnames = ['Ticks',parameter]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(ans)):
             writer.writerow({'Ticks': Ticks[i], parameter: ans[i]})

def main():
	print("Hello World")



if __name__=='__main__':
	main()
