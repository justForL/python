# f = open(r'/Users/james/Desktop/python3/练习/data.txt','r')
# print(f.read())
# f.close()
import os
os.chdir('/Users/james/Desktop/python3/练习')
with open('name.txt','r',encoding='utf8') as f:
	for n in f:
		print(n)