def main():
    year = int(input('请输入年份:'))
    y = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
    print(year, '年是闰年')

if __name__ == '__main__':
    main()