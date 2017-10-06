import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd
import csv
import statistics
import tkinter
 

def getTTicks(filename):
	results = csv.reader(open(filename), delimiter=",")
	next(results, None)
	Ticks=[]
	
	for result in results:
		Ticks.append(float(result[0]))
	return Ticks


def getColumn(filename,parameter):
	results = csv.reader(open(filename), delimiter=",")
	ans=[]
	indx=getIndex(filename,parameter)
	next(results, None)
	for result in results:
		ans.append(float(result[indx]))
	return ans


def getIndex(filename,parameter):
	results = csv.reader(open(filename), delimiter=",")
	for result in results:
		for i in  range(len(result)):
			if(parameter==result[i]):
				return i
				break
		break
		
def exportCSV(ans,Ticks,parameter ):
	with open(str(parameter+'.csv'),'w') as csvfile:
		fieldnames = ['Ticks',parameter]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for i in range(len(ans)):
			 writer.writerow({'Ticks': Ticks[i], parameter: ans[i]})

def getParameters(filename):
	results = csv.reader(open(filename), delimiter=",")
	headers=[]
	for result in results:
		headers=result
		break
	return headers

def main():
	filename=input("Enter Name of Csv file: ")
	print("Splitting Values...")
	headers=getParameters(filename)
	ans={}
	Ticks=getTTicks(filename)

	for header in headers:
		if header !="Ticks":
			ans[header]=set()
			for data in getColumn(filename,header):
				ans[header].add(data)
	#for header,values in ans.items():
	Perms=[]
	for header,data in ans.items():
		vals=[]
		for num in data:
			vals.append(num)
		Perms.append(vals)
	print(Perms[2])








if __name__=='__main__':
	main()