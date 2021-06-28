import math
import random
import copy
#求解例2.1  函数 f(x)=x+10sin(5x)+7cos(4x) 在(0,10)最大值

#设置参数
min_x = 0         #变量范围
max_x = 10
# min_y = 0
# max_y = 10
gen_num = 100   #迭代次数
popu_num = 200    #种群大小
p_mut = 0.05      #突变概率
mut_wet = 0.5     #突变权重
chromo_len = 20   #染色体长度
p_cro = 0.5      #重组概率

#创建空数组(种群)
popu = []
for i in range(popu_num):
        temp = []
        popu.append(temp)
#适应度
fitness = []
fit_fix = 0
#选择概率
p = []
#答案
best_fit = 0
best_chromo = 0

#初始化
def initialize():
    #向空数组中加入随机数
    for i in range(popu_num):
        popu[i].append(random.uniform(min_x,max_x))
        #popu[i].append(random.uniform(min_y,max_y))
    return popu

#适应度函数
def fitnessfunction():
    fitness.clear()
    for i in range(len(popu)):
        chromo_temp = popu[i]
        x = chromo_temp[0]
        #y = chromo_temp[1]
        
        #函数关系
        fit_f = x + 10 * math.sin(5 * x) + 7 * math.cos(4 * x)
        fitness.append(fit_f)
    return fitness

# #适应度补正
# def fitnessfix(fitness):
#     global fit_fix
#     if min(fitness) < 0:
#         fit_fix = - min(fitness) 
#     else:
#         fit_fix = 0
#     for i in range(popu_num):
#         fitness[i] += fit_fix
#     return fitness

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

#突变
def mutation():
    for i in range(len(popu)):
        for j in range(len(popu[i])):
            roll = random.uniform(0,1)
            if roll <= p_mut:
                popu[i][j] += random.uniform(-mut_wet,mut_wet)
    return popu

#重组 - 算术交叉
def crossover():
    for i in range(len(popu)):
        roll = random.uniform(0,1)
        if roll <= p_cro:
            xa = popu[i][0]
            xb = popu[random.randrange(len(popu))][0]
            a = random.random()
            temp = []
            temp.append(a * xa + (1 - a) * xb)
            popu.append(temp)
        else:
            continue
    return popu

#主代码
popu = initialize()
for i in range(gen_num):
    fitness = fitnessfunction()
    #适应度补正  
    # if i == 0:
    # fitness = fitnessfix(fitness)
    
    #答案的储存、更新
    better_fit = max(fitness)
    better_chromo = popu[fitness.index(max(fitness))]
    if better_fit > best_fit:
        best_fit = better_fit 
        best_chromo = better_chromo  
    
    popu = choose()  
    popu = mutation()
    popu = crossover()
    
print(best_chromo)
print(best_fit)







