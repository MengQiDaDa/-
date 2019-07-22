#切片法
def reverse1():
    s=input("请输入需要反转的内容：")
    return s[::-1]

#递归反转
def reverse2(s):
    if s=="":
        return s
    else:
        return reverse2(s[1:])+s[0]


if __name__ == '__main__':
    print(reverse1())
    print(reverse2("需要反转"))