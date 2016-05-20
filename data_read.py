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
	
def meanPreciscion(output):
	'''
		Calculates the Mean Average Percision @ 3
	'''
	#for i in range(0, len(output.index)):
	output[.str.split(
	

if __name__ == '__main__':

	train = pd.read_csv("../train.csv")
	test = pd.read_csv("../test.csv")
	sample = read_csv("../sample_submission.csv")
	displayTop(train, test)
	meanPrecision(sample)
	