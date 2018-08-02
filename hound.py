import os
from folder import folder
from file import file


def goThroughFolder(tree: folder):
    stack = []
    stack.append(tree)
    while (stack):
        tree = stack.pop()
        # THis call will add to the
        tree.init(stack)
        tree.tranverse()
        pass
    print("Am Done, Study well")
    pass


currDir = os.getcwd()
# directory = input("Type the directory Want To Attack ")
rootDir = folder(os.path.join(currDir, "en-US"), 0)
goThroughFolder(rootDir)
