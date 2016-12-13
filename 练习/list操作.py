# l1 = ['Sun','Mon','Tue','Web','Thu','Fri','Sat']
# l2 = ['Sun','Mon','Tue','Thu','Fri']
# l3 = []
# for i in l1:
# 	if i not in l2:
# 		l3.append(i)
# print(l3)

namelist = ['stu1','stu2','stu3','stu4','stu5','stu6','stu7']
removelist = ['stu1','stu2','stu3','stu8','stu9'];
for i in removelist:
	if i in namelist:
		namelist.remove(i)
print(namelist)
