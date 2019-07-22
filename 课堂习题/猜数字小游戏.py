import random   #导入random

def main():
    answer = random.randint(1, 100)  # 数字100以内随机数字
    counter = 0  # 初始
    while True:  # 循环
        counter += 1  # 到此+1
        number = int(input('请输入:'))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了！')
            break  # 结束循环
    print('你一共猜了', counter)
    if counter > 7:
        print('你智商欠费')

if __name__ == '__main__':
    main()
