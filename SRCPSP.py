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


# 1.随机产生种群
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

