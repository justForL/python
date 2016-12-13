L = []
L = [x * x for x in range(1,11)]
print(L)
    
#添加限定条件
L = [x * x for x in range(1,11) if x%2 == 0]
print(L)