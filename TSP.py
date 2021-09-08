import math
import random
import copy
import matplotlib.pyplot as plt

#设置参数
# min_x = 0         #变量范围
# max_x = 10
gen_num = 20   #迭代次数
popu_num = 200    #种群大小
p_mut = 0.05      #突变概率
#mut_wet = 0.5     #突变权重 
p_cro = 0.5      #重组概率
data = [[10,75],[36,9],[91,78],[54,53],[8,51],[78,51]]
city_num = 6     #染色体长度

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
        for j in range(city_num):
            temp.append(j)
        random.shuffle(temp)
        start = temp[0]
        temp.append(start)
        #向种群加入打乱顺序的整数，表示随机顺序。 
        for k in range(len(temp)):
            popu[i].append(temp[k]) 
    return popu

#适应度函数
def fitnessfunction():
    fitness.clear()
    for i in range(len(popu)):
        d = 0
        for j in range(len(popu[i])-1):
            x1 = data[popu[i][j]][0]
            x2 = data[popu[i][j+1]][0]
            y1 = data[popu[i][j]][1]
            y2 = data[popu[i][j+1]][1]
            d += math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
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
                tar = random.randrange(len(popu[i])-1)
                popu[i][j],popu[i][tar] = popu[i][tar],popu[i][j]        #有可能跟自己交换，等于不交换，实际降低了突变几率，但交换范围，最后一个不参与，因为是起点
                #最后要保证首尾相同
                popu[i][-1]=popu[i][0]
    return popu

#重组 - 某段基因保持顺序加入另一个染色体某一段形成新染色体
def crossover():
    for i in range(len(popu)):
        roll = random.uniform(0,1)
        if roll <= p_cro:
            newchromo = []
            start = random.randrange(len(popu[i])-1)
            end = random.randrange(start,len(popu[i])-1)
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
            if newchromo[0] != newchromo[-1]:
                point = newchromo[0]
                newchromo.append(point)
            popu.append(newchromo)
        else:
            continue
    return popu

#主代码
popu = initialize()
for i in range(gen_num):
    fitness = fitnessfunction()
    
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
print(1/best_fit)

#可视化
for i in range(len(data)):
    plt.plot([data[best_chromo[i]][0],data[best_chromo[i+1]][0]],[data[best_chromo[i]][1],data[best_chromo[i+1]][1]])
    plt.scatter(data[best_chromo[i]][0],data[best_chromo[i]][1],color='b')

plt.show()