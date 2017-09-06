import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd
import csv
import statistics

def getColumn(filename):
	results = csv.reader(open(filename), delimiter=",")
	ans=[]
	for result in results:
		#print(result[0])#each row
	#	print(strat,result[0])
		if strat == int(result[0])	: #?!?!?!?!?!
			#print(result[1])
			ans.append(float(result[column]))
	return ans

def main():
    print("Hello World")



if __name__=='__main__':
    main()
