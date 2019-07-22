a = int(input('请输入第一个数：'))
b = int(input('请输入第二个数：'))
c = int(input('请输入第三个数：'))
if a>b :
    if b>c:
        print(a>b>c)
    else:
        if a>c:
            print('a>c>b')
        else:
            print('c>b>a')
elif a<b:
    if b<c:
        print('c>b>a')
    else:
        if c > a:
            print('b>c>a')
        else:
            print('b>a>c')
