import re, urllib

# checks if a string is in the list
def inList(dlList, nextPage):
	isDownloaded = False
	for link in dlList:
		if link == nextPage:
			isDownloaded = True
	return isDownloaded

def writeToFile(baseDir, fileName, fileExtension, pgNum, strToWrite):
	f = open(baseDir + fileName + str(pgNum) + fileExtension, 'w')
	f.write(strToWrite);


currentURL = "http://www.roseindia.net/ejb/introduction/j2eeintroduction.shtml"
pgNum = 1
nextPage = ""
hasNext = True
dlList = []		#keep track of the pages we have downloaded so far

while(hasNext):	
	# get list of strings with anchor tag <a>
	for i in re.findall(r'.*>Next.*<', urllib.urlopen(currentURL).read(), re.I):
	# for i in re.findall(r'.*>Next.*<', string, re.I):
		links = re.findall(r'href=[\'"]?([^\'" >]+)', i, re.I);

		# iterate through list of links obtaind from string
		for j in range (len(links)):
			if len(links[j]) == 0: 		#not empty string
				hasNext = False;
			else:
				nextPage = links[j]
				isDownloaded = inList(dlList, nextPage)
				if isDownloaded:		#if this is not a new link
					hasNext = False
				else:
					# hasNext = True				
					dlList.append(nextPage)
			# print dlList

	if hasNext:
		nextURL = "http://www.roseindia.net" + nextPage
		currentURL = nextURL
		nextPgHTML =  urllib.urlopen(nextURL).read()		
		# f = open('C:\Users\kairen88\Desktop\J2EE_Introduction\J2EE_Tutorial_'+str(pgNum)+'.html', 'w')
		# f.write(nextPgHTML);
		writeToFile('C:\Users\kairen88\Desktop\J2EE_Introduction\\', 'J2EE_Tutorial_', '.html', pgNum, nextPgHTML)
		pgNum = pgNum + 1

