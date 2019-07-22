
score = [0,0,0,0,0,0,0,0,0,0]
print("请输入10位评委对选手的打分（0～100分）：")
for i in range(0,10):
    score[i] = int(input("请输入第%d位评委的打分：" %(i+1)))
while score[i] < 0 or score[i] > 100:
    score[i] = int(input("打分错误，请重新打分：" %(i+1)))
    score.sort()
print("去掉一个最高分%d分，去掉一个最低分%d分,最终得分：%.2f" %(score[9],score[0],(sum(score)-score[0]-score[9])/8))

"""
scores =  []
count = int(input("清确认评委人数："))
print("请输入%d位评委对选手的打分（0～10分）：" %count)
for i in range(count):
    score = float(input("第%d位评委打分：" %(i+1)))
    while score < 0 or score >10:
        score = float(input("打分错误，请重新打分（0～10分）："))
    scores.append(score)
scores.sort()
print("去掉一个最高分%.2f分，去掉一个最低分%.2f分,最终得分：%.2f" %(scores[count-1],scores[0],(sum(scores)-scores[0]-scores[count-1])/(count-2)))
"""