import os
import os.path
os.chdir('/Users/james/Desktop/python3/练习')
filename = 'data4.txt'
if  not os.path.exists(filename):
	print('data4 is not exists')
	f = open(filename,'w',encoding = 'utf8')
	f.flush()
else:
	print('data4 is exists')

	while True:
		str = input('请输入内容:\n')
		if str == 'stop':
			break
		else:
			f = open(filename,'a+',encoding = 'utf8')
			f.write(str+'\n')
		f.close()
