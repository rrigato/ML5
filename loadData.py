import pandas as pd
import numpy as np
import matplotlib as plt
import sys


class cluster():
	def __init__(self):
		print("Initializing the data....")
		self.readData("write")

		
	def readData(self, option):
		if option == 'write':
			try:
				file = open("C:/Users/Punkiehome1/Downloads/kaggleFacebook/train.csv","r")
			except IOError as e:
				print("The data has not been serialized I will do that now")
				self.train = pd.read_csv("C:/Users/Punkiehome1/Downloads/kaggleFacebook/train.csv")
				#pickle.dump(self.train, open("C:/Users/Punkiehome1/Downloads/kaggleFacebook/train.p",
				#	"wb"))
			except:
				print("Unknown Error: ")
				print(sys.exc_info()[0])
				sys.exit(1)
			else:
				file.close()
		elif option == 'read':
			print("hi")
			# try:
			# except:
			

if __name__ == "__main__":
	myCls = cluster()
