import glob, os
from dataBase.dataBase import dataBase

class parserSalaries(object):
	
	def __init__(self, directory):
		self.directory = directory
		self.dataBase = dataBase(directory)
		self.listNameFiles = self.getNameFiles()

	def miniDataToDataBase(self):
		for nameFile in self.getNameFiles:
			self.dataBase.creareTable(nameFile[:-4]) #name file without .csv

	def getNameFiles(self):
		listNameFiles = []
		os.chdir(self.directory)
		for nameFile in glob.glob('*mini.csv'):
			listNameFiles.append(nameFile)
		return sorted(listNameFiles)