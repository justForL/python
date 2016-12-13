import re
phone = '2004-959-559 # 这是一个国外电话号码'
##清除python注释
num = re.sub(r'#.*$','',phone)
print(num)
##清除-只留下电话号
num = re.sub(r'\D','',num)
print(num)
#字符串的分割
url = 'www.baidu.com'
list = re.split('\.',url)
print(list)