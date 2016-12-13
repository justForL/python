while True:
	txt = input("enter a num:\n")
	if txt =='stop':
		break
	elif not txt.isdigit():
		print('please input a num:\n')
	else:
		num = int(txt)
		if num > 20:
			print('too large')
		elif num < 20:
			print("too small")
		else:
			print("You are right!")
