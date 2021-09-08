import math
import random
import copy

#设置参数
# min_x = 0         #变量范围
# max_x = 10
gen_num = 20   #迭代次数
popu_num = 10    #种群大小
p_mut = 0.05      #突变概率
#mut_wet = 0.5     #突变权重
p_cro = 0.5      #重组概率
data = [[10,75],[36,9],[91,78],[54,53],[8,51],[78,51]]
proc_num = 12     #染色体长度

#创建空数组(种群)
popu = []
for i in range(popu_num):
        temp = []
        popu.append(temp)
#适应度
fitness = []
#选择概率
p = []
#答案
best_fit = 0
best_chromo = 0

#初始化
def initialize():
    #向空数组中加入不重复的随机数，表示城市顺序。
    for i in range(popu_num):
        #先按顺序生成城市个数的整数
        temp = []
        for j in range(1,proc_num+1):    #题目数字是1 到12
            temp.append(j)
        random.shuffle(temp)
        #向种群加入打乱顺序的整数，表示随机顺序。
        for k in range(proc_num):
            popu[i].append(temp[k])
    return popu






popu = initialize()
print(popu)