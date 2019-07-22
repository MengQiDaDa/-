def mian():
    s = input('请输入：')

    #创建字典来保存字符的个数
    d = {}
    for i in s:
        #查看字符出现的个数
        if i not in d: #第一次出现
            d[i] = 1    #将次数设置为1，创建键值对
        else:       # 不是第一次出现，更新次数
            d[i] += 1

    #打印字符出现过的次数
    for k in d:
        print(k, ':', d[k], '次')

if __name__ == '__main__':
    mian()