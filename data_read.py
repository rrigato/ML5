import pandas as pd
import numpy as np
import matplotlib as plt


def displayTop(train, test):
	'''
		Shows the top and sample statistics of the train and test datasets
	'''
	
	print(train.describe())
	print(test.describe())
	
	print(train.head())
	print(test.head())
	
	return(train)
	
def meanPrecision(output):
	'''
		Calculates the Mean Average Percision @ 3
	'''
	average_precisions = list(range(len(output.index)))
	for i in range(0, len(output.index)):
		check_ins = output.ix[i,1].split(' ')

	np.mean(average_precisions)
	average_precisions[0:4] = .25
	print(average_precisions[0:4])
	print(len(average_precisions))

	

if __name__ == '__main__':

	#train = pd.read_csv("../train.csv")
	#test = pd.read_csv("../test.csv")
	#sample = pd.read_csv("../sample_submission.csv")
	
	row_id = [0, 1]
	check_in = ['000 001 002','003 004 005']

	actual = ['000', '004']
	sample = pd.DataFrame({ "Check In":check_in,  "ID": row_id,  "actual":actual})
	print(sample)
	print(sample.dtypes)
	
	columns = sample.columns.tolist()
	
	columns = columns[1] + columns[0] + columns[2]
	
	print(columns)
	
	
	print(sample)
	
	
	#displayTop(train, test)
	#meanPrecision(sample)
	