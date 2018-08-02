import os
import bs4
import re


class file:
    name = ""
    # @name : name of the file
    # @depthFrmStartingDir : an Int telling the
    # file object how many units this file is
    # from the starting directory(since the program started)

    def __init__(self, name, depthFrmStartingDir=0):
        self.depth = depthFrmStartingDir
        self.name = name
        pass

    def rename(self):
        # get the file object
        # call the renaming app
        fileName = os.path.basename(self.name)
        directory = os.path.dirname(self.name)
        try:
            os.rename(self.name, os.path.join(
                directory, self.processStrings(fileName)))
            pass
        except FileExistsError as error:
            print(error.filename+" exists")
            return
        pass

    def attackFile(self):
        print("Attacking File", end='\r')
        soup = {}
        with open(self.name, 'r+', errors='ignore') as fileR:
            soup = bs4.BeautifulSoup(fileR.read(), "html.parser")
            fileR.close()
            pass
        with open(self.name, 'w', errors='ignore') as fileW:
            tagList = soup.find_all('link')
            scriptTagList = soup.findAll('script', {"src": True})
            for tag in tagList:
                stringToProcess = tag['href']
                tag['href'] = self.processStrings(stringToProcess)
                pass
            for scriptSrc in scriptTagList:
                if (not scriptSrc['src']):
                    continue
                stringToProcess = scriptSrc['src']
                scriptSrc['src'] = self.processStrings(stringToProcess)
                pass
            print("Writing To File", self.name, end='\r')
            fileW.write(soup.prettify())
            fileW.close()
            pass
        pass

    def processStrings(self, stringToProcess: str):
        if (stringToProcess.startswith("../")):
            return stringToProcess
        print('Processing file '+self.name, end='\r')
        regEx = re.compile(r'\.(.*?)\.')
        match = regEx.search(stringToProcess[::-1])
        if (match is None):
            return stringToProcess
        value = stringToProcess.replace(match.group(
        )[::-1], '.').replace("https://developer.cdn.mozilla.net/", '../'*self.depth)
        return value
    pass
