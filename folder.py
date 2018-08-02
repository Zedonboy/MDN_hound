import os
import shutil
from file import file


class folder:
    def init(self, stackRef: list):
        print("Initializing "+self.name)
        dirContents = os.listdir(self.name)
        print("getting contents of "+self.name)
        for content in dirContents:
            # Checking if this particular name with the parent directory
            # is it a file
            if(os.path.isfile(os.path.join(self.name, content))):
                # Used when you want to change file names
                fileName = str(content)
                fileName = fileName.replace(".html", '')
                if (fileName.isdigit()):
                    self.deletefile(os.path.join(self.name, content))
                    continue
                self.listOfFiles.append(
                    file(os.path.join(self.name, content), self.depth))
                # Checking whether a file is an html file
                print("Gotten "+content, end='\r')

            elif(str(content).endswith("$revision") or str(content).endswith("$locales")):
                self.deletefolder(os.path.join(self.name, content))
                continue
            else:
                stackRef.append(
                    folder(os.path.join(self.name, content), self.depth))
                pass
            pass
        pass

    def tranverse(self):
        for file in self.listOfFiles:
            if (file.name.endswith(".html")):
                file.attackFile()
                # self.listOfFiles.remove(file)
            pass
        self.listOfFiles.clear()
        pass

    def deletefile(self, path: str):
        print("Deleting File" + path, end='\r')
        try:
            os.remove(path)
        except OSError:
            return
        pass

    def deletefolder(self, path: str):
        print("Deleting Folder" + path, end='\r')
        shutil.rmtree(path, ignore_errors=True)
        pass

    def __init__(self, name, depth=0):
        self.depth = depth + 1
        self.name = name
        pass
    name = ""
    listOfFiles = []
    pass
