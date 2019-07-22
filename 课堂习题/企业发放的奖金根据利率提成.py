def pay_award():
    profit = int(input('净利润为：'))
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0,6):
        if profit > arr[idx]:
            # 当前区间的利润
            r += (profit - arr[idx]) * rat[idx]
            print('你的奖金为：', (profit - arr[idx]) * rat[idx])
            # 重置下一个区间起始奖金数量
            profit = arr[idx]
    return r

if __name__ == '__main__':
    result = pay_award()
    print('总数为：', result)