n = int(input('从键盘输入一个数：'))
sum = 0
for i in range(n):
    sum += i + 1
    print(i)
print('1到N求和结果:{}'.format(sum))