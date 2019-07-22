def main():
    a = input('输入数字>>>')
    count = int(input('几个数字相加>>>'))
    ret = []
    for i in range(1, count + 1):
        ret.append(int(a * i))
        print(ret[i - 1])
    print(sum(ret))

if __name__ == '__main__':
    main()