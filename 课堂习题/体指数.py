height , weight = eval(input('请输入身高(米)和体重(公斤)【逗号隔开】：'))
bmi = weight / pow(height,2)
print("BMI指数为：{:.2f}".format(bmi))
who,nat = ' ', ' '
if bmi < 18:
    who, nat = '偏瘦', '偏瘦'
elif 18 <= bmi < 25:
    who, nat = '正常', '正常'
elif 25 <= bmi <27:
    who, nat = '超胖体重','超胖体重'
else:
    who, nat = '肥胖', '肥胖'
print("BMI 指标为：国际'{0}', 国内'{1}'".format(who, nat))