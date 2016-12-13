# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def now():
# 	print('outPut now')
# f = now
# f()

# 第一题 是在now函数前打印callBegin 结束前加callEnd
def printlog(func):
	def wrapper(*args,**kw):
		print('callBegin')
		def end(*args,**kw):
			func()
			return print('end')
		return end()
	return wrapper


@printlog
def now():
	print('outPut now')
f = now
f()