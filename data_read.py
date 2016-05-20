import pandas as pd
import numpy as np
import matplotlib as plt


def readIn():
	train = pd.read_csv("../train.csv")
	test = pd.read_csv("../test.csv")
	
	print(train.describe())
	print(test.describe())
	
	print(train.head())
	print(test.head())
	
	return(train)

if __name__ == '__main__':
	readIn()
	