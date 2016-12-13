import os
import os.path
import pickle
os.chdir('/Users/james/Desktop/python3/练习/')
filename = 'data5.txt'
if os.path.isfile(filename):
	os.remove(filename)
namedict = {'lengjian':'james','anyanan':'anan','al':'love'}
with open(filename,'wb') as f:
	pickle.dump(namedict,f)
	f.flush()