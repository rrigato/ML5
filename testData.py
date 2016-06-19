import pandas as pd
import numpy as np
import sys
import pickle
class test:
	def __init__(self):
		self.rand = np.random.RandomState(135)
		print("Initializing the test data....")
		self.readData("write")
		self.readData("read")
		print(self.test.shape)
		
	def readData(self, option):
		'''
			Serializes the test.csv data if that has not been done already,
			reads that data into memory
		'''
		try:
			if option == 'write':
				try:
					file = open("C:/Users/ryan/kaggleFacebook/test.p","r")
				except IOError as e:
					print("The data has not been serialized I will do that now")
					self.test = pd.read_csv("C:/Users/ryan/kaggleFacebook/test.csv")
					pickle.dump(self.test, open("C:/Users/ryan/kaggleFacebook/test.p",
						"wb"))
					print("\n Data has been serialized at: ")
					print("C:/Users/ryan/kaggleFacebook/test.p")
				except:
					print("Unknown Error: ")
					print(sys.exc_info()[0])
					sys.exit(1)
				else:
					print("The Data has been serialized at C:/Users/ryan/kaggleFacebook/test.p")
					file.close()
			elif option == 'read':
				print("Reading Data from pickle object...")
				self.test = pickle.load(open("C:/Users/ryan/kaggleFacebook/test.p",
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
			
			
if __name__ == "__main__":
	tst = test()