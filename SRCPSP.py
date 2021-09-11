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
#todo     时间推迟之后 判断 正在进行 列表内的工序是否完成， 判定此时时间是否是starttime+ duration
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
    7:[10],
    8:[11],
    9:[11],
    10:[12],
    11:[12],
    12:[],
}
duration = [0,3,4,2,6,3,2,3,4,3,2,0]
src = [
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
    [0,0]
]
#设置参数
# min_x = 0         #变量范围
# max_x = 10
gen_num = 10   #迭代次数
popu_num = 10    #种群大小
p_mut = 0.05      #突变概率
#mut_wet = 0.5     #突变权重
p_cro = 0.5      #重组概率
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
best_fit = 999
best_chromo = 0
#初始化


def initialize():
    #向空数组中加入不重复的随机数，表示顺序。
    for i in range(popu_num):
        #先按顺序生成城市个数的整数
        temp = []
        for j in range(2,proc_num):    #题目数字是1 到12 这里只加入2到11
            temp.append(j)
        random.shuffle(temp)
        temp.insert(0,1)
        temp.append(12)
        #向种群加入打乱顺序的整数，表示随机顺序。
        for k in range(proc_num):
            popu[i].append(temp[k])
    return popu


#适应度计算
def fitnessfunction():
    fitness.clear()
    wat_proc = []
    wat_proc_tmp = []
    rdy_proc = []
    rdy_proc_tmp = []
    now_proc = []
    global starttime
    starttime = []
    endtime = []
    endtime_tmp = []
    for i in range(len(popu)):
        suc_proc = [1]
        endtime.clear()
        wat_proc.clear()
        rdy_proc.clear()
        now_proc.clear()
        starttime.clear()
        r1 = 3
        r2 = 4
        time = 0
        finaltime = 0
        for j in popu[i]:#每个工序
            if j == 1:
                continue
            for k,v in data.items():
                #判断紧前工序
                if j in v:
                    if k not in suc_proc:#紧前工序还没完成
                        if j not in wat_proc:   #工序进入  “待进行”里一次就行了
                            wat_proc.append(j)
                            continue
                        else:
                            continue
                    else:
                        if j in wat_proc:#有可能存在另一个已完成的紧前工序
                            rdy_proc.append(j)
                            wat_proc.remove(j)
                        rdy_proc.append(j)
                        break
            while rdy_proc:
                # 先判断“待进行”是否为空，比如 62374   6一开始不能进行，一开始会被抛入待进行，然后遍历2，会被加入rdy_proc，此时while判定成功，判断资源，资源够
                # 之后记录时间，加入now 直接break,就开始遍历3了，3一看紧前完成，进入“准备中”，进入while，遍历wat，6并不能加入，往下走
                # 3也能进行资源也够，此时now就有2和3，while rdy 空了 下一个
                # 然后是7 紧前未完成 加入wat rdy没有 （time=0
                # 4，紧前完成 加入rdy while里面，检查wat 67的紧前均未完成
                #4资源不够 time+1   endtime = [[2,3],[3,4]]
                #一直到time=3 2完成了，资源变成2，4
                wat_proc_tmp.clear()
                wat_proc_tmp = list(wat_proc)
                for n in wat_proc_tmp:
                    for o, p in data.items():
                        # 判断紧前工序
                        if n in p:
                            if o not in suc_proc:  # 紧前工序还没完成
                                continue
                            else:
                                wat_proc.remove(n)
                                rdy_proc.append(n)
                                break
                    # if r1 >= src[n - 1][0] and r2 >= src[n - 1][1]:
                    #     # 判定足够，记录时间
                    #     starttime.append([n, time])
                    #     endtime.append([n, starttime + duration[n]])
                    #     r1 -= src[n - 1][0]
                    #     r2 -= src[n - 1][1]
                    #     wat_proc.remove(n)
                #这里是工序前序判定完成，本工序可以进行，所以进入了“rdy”，逐一判断“rdy”的工序 资源够不够
                rdy_proc_tmp.clear()
                rdy_proc_tmp = list(rdy_proc)
                for g in rdy_proc_tmp:
                    if r1 >= src[g-1][0] and r2 >= src[g-1][1]:
                        #判定足够，记录时间，加入now
                        starttime.append([g,time])
                        endtime.append([g,time + duration[g-1]])
                        if finaltime < time + duration[g-1]:
                            finaltime = time + duration[g-1]
                        r1 -= src[g-1][0]
                        r2 -= src[g-1][1]
                        rdy_proc.remove(g)
                        now_proc.append(g)
                        break
                    else:
                        #资源不够，只能推迟时间单位，等其他工序完成，资源回复
                        mark = 0
                        while mark == 0:
                            time+=1
                            #时间推进之后检查now是否有工序已经完成
                            endtime_tmp.clear()
                            endtime_tmp = list(endtime)
                            for k in range(len(endtime)):
                                if time == endtime_tmp[k][1]:
                                    for l in now_proc:
                                        if l == endtime_tmp[k][0]: #找到满足结束时间的工序号
                                            now_proc.remove(l)
                                            suc_proc.append(l)
                                            r1 += src[l-1][0]
                                            r2 += src[l-1][1] #资源回复
                                            endtime.pop(endtime.index([l,endtime_tmp[k][1]]))
                                            mark = 1
                                            #确保任务完成了 才去看其他的

                        #这里应该把能完成的全部处理完了
                        #如果时间不满足，会继续判定while，now_proc是否为空，只要不为空，就会再次进行，判断资源，
                #如果while不满足，说明now_proc为空
        fitness.append(finaltime)
        betterstarttime=starttime
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
                if j not in part:
                    newchromo.append(j)
                    count += 1
            popu.append(newchromo)
        else:
            continue
    return popu


# 主代码
popu = initialize()
for i in range(gen_num):
    fitness = fitnessfunction()

    # 答案的储存、更新
    better_fit = min(fitness)
    better_chromo = popu[fitness.index(min(fitness))]
    if better_fit < best_fit:
        best_fit = better_fit
        best_chromo = better_chromo

    popu = choose()
    popu = mutation()
    popu = crossover()

print(best_chromo)
print(best_fit)