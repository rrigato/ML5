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
		truth = len(check_ins)*[0]
		for z in range(len(check_ins)):
			if(check_ins[z] == output.ix[i,2]):
				truth[z] = 1
		Denom =  np.array(range(1,(len(truth) + 1)), dtype= np.float)
		
		truth = np.array(truth, dtype = np.float)
		average_precisions[i] = truth/ Denom
	

	print("Your mean average precision is: \n")
			
	print(np.mean(average_precisions))
	

	

if __name__ == '__main__':

	#train = pd.read_csv("../train.csv")
	#test = pd.read_csv("../test.csv")
	#sample = pd.read_csv("../sample_submission.csv")
	
	row_id = [0, 1]
	check_in = ['000 001 002','003 004 005']

	actual = ['000', '004']
	sample = pd.DataFrame({ "Check In":check_in,  "ID": row_id,  "actual":actual})

	
	#reorder the columns
	sample = sample[[1,0,2]]
	

	#displayTop(train, test)
	meanPrecision(sample)
	