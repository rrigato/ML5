import pandas as pd
import numpy as np
import matplotlib as plt
import sys
import pickle
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn import grid_search

class cluster():
	def __init__(self):
		self.rand = np.random.RandomState(135)
		print("Initializing the data....")
		self.readData("write")
		self.readData("read")
		print(self.train.head)

		
	def readData(self, option):
		'''
			Serializes the training data if that has not been done already,
			reads that data into memory
		'''
		try:
			if option == 'write':
				try:
					file = open("C:/Users/Punkiehome1/Downloads/kaggleFacebook/train.p","r")
				except IOError as e:
					print("The data has not been serialized I will do that now")
					self.train = pd.read_csv("C:/Users/Punkiehome1/Downloads/kaggleFacebook/train.csv")
					pickle.dump(self.train, open("C:/Users/Punkiehome1/Downloads/kaggleFacebook/train.p",
						"wb"))
					print("\n Data has been serialized at: ")
					print("C:/Users/Punkiehome1/Downloads/kaggleFacebook/train.p")
				except:
					print("Unknown Error: ")
					print(sys.exc_info()[0])
					sys.exit(1)
				else:
					print("The Data has been serialized at C:/Users/Punkiehome1/Downloads/kaggleFacebook/train.p")
					file.close()
			elif option == 'read':
				print("Reading Data from pickle object...")
				self.train = pickle.load(open("C:/Users/Punkiehome1/Downloads/kaggleFacebook/train.p",
						"rb"))
				print("Data is loaded")
				
		except pickle.PickleError as PE:
			print(PE)
			print("Exiting Python:")
			sys.exit(1)
		except AttributeError as AE:
			print(AE)
			print("Exiting Python")
			sys.exit(1)
		except:
			print("Unexpected Error: \n", sys.exc_info[0])
			print("Exiting Python")
			sys.exit(1)
			
	def splitData(self):
		'''
			Splits the data into train, test and validation sets.
		'''
		print("Splitting the data into train test and validation sets:")
		
		'''
			This first train_test_split splits the data into what will be train/test
			(self.Xfirst, self.Yfirst) and what will be the Validation set(self.Xholdout,
			self.Yholdout)
			
			Note: The validation dataset takes up 15% of the original dataset,
			while train/test will split the remaining 85 %
		'''
		self.Xfirst, self.Xholdout, self.Yfirst, self.Yholdout = train_test_split(
			self.train.ix[:,0:4], self.train['place_id'], test_size = .15,
			random_state = self.rand)
			
		'''
			This command splits the first dataset into train and test datasets
			The train dataset will comprise .8 * .85 = 68% of the original dataset
			While the test dataset will comprise of .2* .85 = 17% of the original dataset
		'''
		self.Xtrain, self.Xtest, self.Ytrain, self.Ytest = train_test_split(
			self.Xfirst, self.Yfirst, test_size = .2,
			random_state = self.rand)
			
			
		'''
			Testing to make sure the sum of the observations in train/test/holdout 
			equals the number of observations in the original training dataset
		'''
		if (len(self.Ytrain) + len(self.Ytest) + len(self.Yholdout)) != len(self.train):
			print("Error: Not all observations are in the train/test/validation sets:")
			sys.exit(1)
		if (len(self.Xtrain) + len(self.Xtest) + len(self.Xholdout)) != len(self.train):
			print("Error: Not all observations are in the train/test/validation sets:")
			sys.exit(1)			
		

	def writeData(self):		
			
		'''
			The files are a list with  the name each file extension will take 
			once it is serialized
			The datasets is a list of the corresponding train, test and validation to be serialized
		'''
		files = ['Xtrain', 'Xtest', 'Ytrain', 'Ytest', 'Xholdout', 'Yholdout']	
		datasets = [ self.Xtrain, self.Xtest, self.Ytrain, self.Ytest, self.Xholdout, self.Yholdout]
		
		'''
			This loop iterates over each of: train X and Y datasets, test X and Y datasets,
			and holdout X and Y datasets.
			
			The algorithm is that that for each iteration of the loop, the program checks to see 
			if that particular file has been serialized. If it has been serialized the file is 
			closed and the user is alerted of the files location. If the file does not exist,
			and IOError is caught and the data is written to a .p file
			
			Example:
				if array of X variables for train does not exist at 
				"C:/Users/Punkiehome1/Downloads/kaggleFacebook/Xtrain.p" then the
				an IOError is thrown and the data is written to that location from
				self.Xtrain
				
				Otherwise, the file connection is closed
		'''
		for file, dataset in zip(files, datasets):
			try:
				fConnect = open("C:/Users/Punkiehome1/Downloads/kaggleFacebook/" + file + ".p","r")
			except IOError as e:
				print("The data has not been serialized I will do that now")
				pickle.dump(dataset, open("C:/Users/Punkiehome1/Downloads/kaggleFacebook/" + file + ".p",
							"wb"))
				print("\n Data has been serialized at: ")
				print("C:/Users/Punkiehome1/Downloads/kaggleFacebook/" + file + ".p")
			except:
				print("Unknown Error: ")
				print(sys.exc_info()[0])
				sys.exit(1)
			else:
				print("The Data has been serialized at:")
				print("C:/Users/Punkiehome1/Downloads/kaggleFacebook/" + file + ".p")
				fConnect.close()			
		
if __name__ == "__main__":
	myCls = cluster()
	myCls.splitData()
	myCls.writeData()