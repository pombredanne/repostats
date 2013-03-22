import os
import subprocess

# repoIsStored checks if the .helpers/global.txt contains a repo name
def repoIsStored():
	path = os.getcwd()
	with open(path + '/.helpers/global.txt', 'r') as repoNameFile:
		line = repoNameFile.readline()
		line = line[1:]

		if len(line) == 0:
			return False
		else:
			return True

	return False

# clearRepoNames clears the .helpers/global.txt file
def clearRepoName():
	storeRepoName('')

# storeRepoName stores a repo name in .helpers.global.txt files
def storeRepoName(repoName):
	path = os.getcwd()
	with open(path + '/.helpers/global.txt', 'r+') as repoNameFile:
		repoNameFile.seek(0)
		repoNameFile.write(repoName)
		repoNameFile.truncate()

# returns the name of the repo in the .helpers/global.txt file
def getRepoName():
	path = os.getcwd()
	with open(path + '/.helpers/global.txt', 'r') as repoNameFile:
		return repoNameFile.readline()

# saveRepo moves the repo from .data to the repostats directory and clears the repo name in .helpers/global.txt
def saveRepo():
	path = os.getcwd()
	if repoIsStored() is False:
		print 'There is no repo to be saved' 
	else:
		repoName = getRepoName()
		process = subprocess.Popen('mv "' + path + '/.data/repo" "' + path + '/' + repoName + '"', shell=True).wait()
		clearRepoName()

# clearRepo clears in .data and the repo name in .helpers/global.txt
def clearRepo():
	path = os.getcwd()
	if repoIsStored() is False:
		print 'There is no repo to clear.' 
	else:
		repoName = getRepoName()
		process = subprocess.Popen('rm -rf "' + path + '/.data/repo"', shell=True).wait()
		clearRepoName()

# loadRepo takes a github url and loads and saves the repo to the .data directory
def loadRepo(repo):
	if repoIsStored() is True:
		if theyWantToClearOldRepo() is False:
			print "No repository loaded."
			return
		else:
			clearRepo()

	os.chdir('.data/')
    
	repo = completeURL(repo)
	if URLIsValid(repo) is False:
		print 'Could not resolve url: ' + repo
		return


	index = repo.rfind('/')
	if (index == repo.__len__() - 1):
		repo = repo.rstrip('/')
		index = repo.rfind('/')
	repo_name = repo[index + 1:]

	# Clone and move to .data
	process = subprocess.Popen('git clone ' + repo, shell=True).wait()
	# HHHHHHHHHHHHHHHHHEEEEEEEEEEE****************************RRRRRRRRRRRRRRRRRRRRRRRRR
	process = subprocess.Popen('mv ' + repo_name + '/ repo/', shell=True).wait()

	os.chdir('../')
    
    # store repo
	storeRepoName(repo_name)


def completeURL(repoURL):
	if (repoURL.find('github.com') == -1):
		if (repoURL[0] != '/'):
			repoURL = '/' + repoURL
		repoURL = 'github.com' + repoURL
	if (repoURL.find('https://') == -1 and repoURL.find('http://') == -1):
		repoURL = 'https://' + repoURL
	return repoURL

def URLIsValid(githubURL):
	try:
		urllib2.urlopen(githubURL,timeout=3)
		return True
	except urllib2.URLError as err: pass
	return False


def theyWantToClearOldRepo():
	valid = {'y':True, 'ye':True, 'yes':True, 'n':False, 'no':False}
	while True:
		response = raw_input("You already have a repo stored. Would you like to clear it? [y/n]: ").lower()
		if response in valid:
			return valid[response]
		else:
			print "Please respond with yes or no."









