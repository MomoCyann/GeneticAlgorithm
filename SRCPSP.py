import math
import random
import copy
#todo 1.随机产生种群
# 2.算适应度是一个解码的过程，比如 4 3 6 2，2是6的紧前，算到6时会检验2在不在紧前工序里，不在的话先把6抛入待进行，下一个，
#   这意味着每一个的检验过程还要顺带检验 “待进行‘ 里面的工序
#   成功的检验是：
#   先判定紧前是否在已进行里，此工序能否进行
#     这里直接不能的话就抛入待进行，下一个工序。
#     能的话下一步
#   再判定资源够不够，
#     能进行就抛入 正在进行 ，记录starttime，资源数量 减少相应的r1[i] r2[i]，判断下一个工序
#     不够就推迟时间一个单位，
#       时间推迟之后 判断 正在进行 列表内的工序是否完成， 判定此时时间是否是starttime+ duration
#         等于就标记完成，抛入已进行。资源量+=r1[i]
#         此刻检查待进行里的每一个工序
#           检查紧前
#             已经完成的话判定资源
#               够的话 抛入 记录starttime，资源数量 减少相应的r1[i] r2[i]，判断下一个工序
#               不够的话 时间推进
#           为空的话下一个工序
#         再重新判断资源
data = {
    1:[2,3,4,5],
    2:[6],
    3:[7],
    4:[8],
    5:[9],
    6:[10],
    7:[11],
    8:[11],
    9:[11],
    10:[12],
    11:[12],
    12:[],
}
duration = [0,3,4,2,6,3,2,3,4,3,2,0]
src = {
    [0,0],
    [2,0],
    [1,0],
    [1,0],
    [0,2],
    [0,3],
    [0,2],
    [2,0],
    [0,1],
    [3,0],
    [0,2],
    [0,0],
}
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

def fitnessfunction():
    fitness.clear()
    starttime=0
    endtime=0

    for i in range(len(popu)):
        d = 0
        for j in range(len(popu[i])-1):

        fitness.append(1/d)
    return fitness

#选择
def choose():
    #计算适应度总和
    fit_sum = 0
    for i in range(len(popu)):
        fit_sum += fitness[i]
    #计算每个染色体选择的概率
    for i in range(len(popu)):
        p.append(fitness[i]/fit_sum)
    #选择 - 轮盘赌
    popu_temp = []
    for i in range(popu_num):
        roll = random.uniform(0,1)
        p_sum = 0
        for j in range(len(popu)):
            p_sum += p[j]
            if roll <= p_sum:
                popu_temp.append(popu[j])
                break
    popu.clear()
    # popu = copy.deepcopy(popu_temp)
    for i in range(popu_num):
        popu.append([])
        for j in range(len(popu_temp[i])):
            popu[i].append(popu_temp[i][j])
    return popu

#突变 - 交换位置
def mutation():
    for i in range(len(popu)):
        for j in range(len(popu[i])-1):
            roll = random.uniform(0,1)
            if roll <= p_mut:
                tar = random.randrange(len(popu[i]))
                popu[i][j],popu[i][tar] = popu[i][tar],popu[i][j]        #有可能跟自己交换，等于不交换，实际降低了突变几率，但交换范围，最后一个不参与，因为是起点
    return popu

#重组 - 某段基因保持顺序加入另一个染色体某一段形成新染色体
def crossover():
    for i in range(len(popu)):
        roll = random.uniform(0,1)
        if roll <= p_cro:
            newchromo = []
            start = random.randrange(len(popu[i]))
            end = random.randrange(start,len(popu[i]))
            part = popu[i][start:end]
            tar = random.randrange(len(popu))
            #防止自交
            while tar == i:
                tar = random.randrange(len(popu))
            count = 0
            for j in popu[tar]:
                if count == start:
                    newchromo.extend(part)
                    count += 1
                if j not in part and j not in newchromo:
                    newchromo.append(j)
                    count += 1
            popu.append(newchromo)
        else:
            continue
    return popu

#设置参数
# min_x = 0         #变量范围
# max_x = 10
gen_num = 20   #迭代次数
popu_num = 10    #种群大小
p_mut = 0.05      #突变概率
#mut_wet = 0.5     #突变权重
p_cro = 0.5      #重组概率
data = {
    1:[2,3,4,5],
    2:[6],
    3:[7],
    4:[8],
    5:[9],
    6:[10],
    7:[11],
    8:[11],
    9:[11],
    10:[12],
    11:[12],
    12:[],
}
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



