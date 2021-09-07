import math
import random
import copy

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