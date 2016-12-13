#字符串转数字
# str = '123456'
#base是进制转换
# print(int(str,base=10))

import functools
int2 = functools.partial(int,base = 2)
x = int2('100000')
print(x)