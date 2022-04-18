import os
import datetime
import shutil

def archiver(file, targetFolder, archiveName):
	"""Transfers file from targetFolder to archiveName"""
	#'file' format: 'NetscapeNavigator.csv'
	#'targetFolder' format: '\\\windows95\\mydocuments\\AIMchatlogs\\'   -Use empty quotes if current folder
	#'archiveName' format:  'Archive_AIMchatlogs'



	currentDateTime = datetime.datetime.now()
	currentDate = str(currentDateTime.strftime('%Y-%m-%d'))
	currentDateTimeLog = str(currentDateTime.strftime('%Y-%m-%d_%H%M'))


	archFolder = targetFolder + archiveName
	archFile = targetFolder + file
	fileWithDate = currentDate + ' ' + file
	if not os.path.exists(archFolder):
		os.makedirs(archFolder)

	shutil.copy(archFile, archFolder)
	shutil.move(targetFolder + archiveName + '\\' + file, targetFolder 
		+ archiveName + '\\' + fileWithDate)

		