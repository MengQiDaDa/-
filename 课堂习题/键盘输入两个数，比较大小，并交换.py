a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
list = [a,b]
list.sort()
for i in range(len(list)):
    print(list[i])