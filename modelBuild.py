import pandas as pd
import numpy as np
import sys
import pickle

from sklearn.neighbors import KNeighborsClassifier
class model:
	def __init__(self):
		self.rand = np.random.RandomState(135)
		print("Initializing the random train and test splits....")
		self.loadData()
	
	def loadData(self):
	
		'''
			Loads the Xtrain, Xtest, Ytrain, and Ytest datasets into memory
		'''
		
		try:
			self.Xtrain = pickle.load(open("C:/Users/ryan/kaggleFacebook/Xtrain.p", "rb"))		
			self.Xtest = pickle.load(open("C:/Users/ryan/kaggleFacebook/Xtest.p", "rb"))
			self.Ytrain = pickle.load(open("C:/Users/ryan/kaggleFacebook/Ytrain.p", "rb"))		
			self.Ytest = pickle.load(open("C:/Users/ryan/kaggleFacebook/Ytest.p", "rb"))			
		except IOError as e:
			print("Error unable to load the dataset")
			print(e)
			sys.exit(1)
		except:
			print("Unknown Error: ")
			print(sys.exc_info()[0])
			sys.exit(1)
		else:
			print("Train and test Datasets were successfully loaded")
			
	def KNN(self):
		neigh = KNeighborsClassifier(n_neighbors = 3)
		neigh.fit(self.Xtrain[['x','y']], self.Ytrain) 

if __name__ == '__main__':
	Cls = model()