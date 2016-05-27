import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn import preprocessing, cross_validation, neighbors

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
	


def knnImplement(train, test):
	ids = train['row_id']
	train.drop(['row_id'], 1)
	X = np.array(train.drop(['place_id'],1))
	y = np.array(train['place_id'])
	
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=.2)
	
	clf = neighbors.KNeighborsClassifier()
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	
	probabailities = clf.predict_proba(X_test)
	
	print(probabilities.head)
	print(accuracy)
	return()
	
	
	

if __name__ == '__main__':

	train = pd.read_csv("../train.csv")
	#test = pd.read_csv("../test.csv")
	#sample = pd.read_csv("../sample_submission.csv")
	
	print(len(train))

	train2 = train.ix[0:3000000,:]
	
	test2 = train.ix[100:200,:]
#	train2= train.ix[0:(len(train)/2), :]
#	test2 = train.ix[(len(train)/2):(len(train)-1),:]
	
	group_by_response = train.groupby('place_id')
	
	group_by_response.head()
	
	#rows = 29118021
	#unique check ins = 108390

	print(len(np.unique(train['place_id'])) )
	knnImplement(train2,test2)




'''	row_id = [0, 1]
	check_in = ['000 001 002','003 004 005']

	actual = ['000', '004']
	sample = pd.DataFrame({ "Check In":check_in,  "ID": row_id,  "actual":actual})

	
	#reorder the columns
	sample = sample[[1,0,2]]
	

	#displayTop(train, test)
	meanPrecision(sample)
'''	