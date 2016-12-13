import os
os.chdir('/Users/james/Desktop/python3/练习/')
l = ['James','lengjian','anan','haha']
f = open('data2.txt','w+',encoding = 'utf8')
for n in l:
	f.write(str(n)+'\n')
f.flush()
f.close()
