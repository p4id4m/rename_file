folder = 'file path here'
import os
pathiter = (os.path.join(root, filename)
    for root, _, filenames in os.walk(folder)
    for filename in filenames
)
for path in pathiter:
    newname =  path.replace('%20', ' ')
    newname1 =  path.replace('%27', ' ')
    newname2 =  path.replace('%5', ' ')
    if newname != path:
        os.rename(path,newname)
    if newname1 != path:
        os.rename(path,newname1)
    if newname2 != path:
        os.rename(path,newname2)
