import os
import subprocess

import globaldata as globaldata

def saveRepo():
	path = os.getcwd()
	if globaldata.isRepoStored() is False:
		print 'There is no repo to be saved' 
	else:
		repoName = globaldata.getRepoName()
		process = subprocess.Popen('mv "' + path + '/.data/repo" "' + path + '/' + repoName + '"', shell=True).wait()
		globaldata.clearRepoName()