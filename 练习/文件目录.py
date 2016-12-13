import os

os.chdir('/Users/james/Desktop/python3/练习')
filelist1 =os.listdir()
filelist2 =[f for f in filelist1 if f.endswith('.py')]
print(filelist2)