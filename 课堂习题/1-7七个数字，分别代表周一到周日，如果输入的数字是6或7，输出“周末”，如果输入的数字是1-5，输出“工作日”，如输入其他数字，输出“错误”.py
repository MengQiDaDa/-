def main():
    day = int(input('请输入日期:'))
    print(day)
    if day == 6:
        print('周末')
    elif day == 7:
        print('周末')
    elif 1 <= day <= 5:
        print('工作日')
    else:
        print('错误')

if __name__ == '__main__':
    main()