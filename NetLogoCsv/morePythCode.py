import pandas as pd 
import matplotlib.pyplot as plt
import random

df=pd.read_csv('EndMultipleRuns.csv')
#plt.plot(df[['number-strategies']],df[['std']],label='std')
plt.plot(df[['number-strategies']],df[['avg-attendance']],label='avg-attendance')
plt.axhline(y=60,C='red',label="Overcrowding Threshold")
plt.xlabel('Number of Strategies')
plt.ylabel('avg-attendance')

'''
# color => memory-size
#X => number-strategies
# Y => avg-attendance
df =pd.read_csv('EndMultipleRuns1.csv')
c=0
col=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
df=df.sort_values(by=['memory-size'])
for size in df['memory-size'].unique():
	plt.scatter(df[df['memory-size']==size]['number-strategies'],round(df[df['memory-size']==size][["std"]],4),color=random.choice(col),label=(str(size)+" memory-size"))

'''

plt.legend()
plt.show()