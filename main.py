import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import copy
from initialization import initialization
from cal_objective import cal_objective
from neighboring_cur import neighboring_cur
import time
from parse_data_new1 import parse_data_new1
from parse_data_new2 import parse_data_new2
a = time.time()
def main():
    job_machine, processing_time, machine_number, operation_number = parse_data_new1()
    # job_machine, processing_time, machine_number, operation_number = parse_data_new2()

    # 设置参数
    H = 5
    MAX_ITERATION = 1000000
    MAX_NO_IMPROVE = 0.02
    # 初始化当前解X，并计算其目标函数值makespan f(x)
    cur = initialization(operation_number, job_machine)
    bestX = cur
    objective_value_cur = cal_objective(cur, machine_number, operation_number, job_machine, processing_time)
    best_Cmax_time = objective_value_cur
    history_list = [objective_value_cur for i in range(H)]
    it = 0
    idle = 0
    trace_min = []
    trace_Y = []
    #循环过程
    while (it < MAX_ITERATION) and (idle < MAX_NO_IMPROVE*MAX_ITERATION):
        next = neighboring_cur(cur, job_machine, operation_number)
        #TODO 多邻域选择 
        objective_value_next = cal_objective(next, machine_number, operation_number, job_machine, processing_time)
        if objective_value_next >= objective_value_cur:
            idle += 1
        else:
            idle = 0
        if objective_value_next < best_Cmax_time:
            bestX = next
            best_Cmax_time = objective_value_next
            print('最优解的完工时间是：%f' % best_Cmax_time)
        h = it % H
        if objective_value_next < history_list[h] or objective_value_next <= objective_value_cur:
            cur = copy.deepcopy(next)
            objective_value_cur = objective_value_next
        if objective_value_next < history_list[h]:
            history_list[h] = objective_value_next
        it += 1
        trace_min.append(min(history_list))
        trace_Y.append(objective_value_next)
    b = time.time()
    seconds = b - a
    print("程序用时：%02d s" % seconds)
    print("最优解的完工时间：%f" %best_Cmax_time)
    print("最优解是:")
    print(bestX)
    
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # fig = plt.figure()
    x_axis = [i for i in range(it)]
    plt.plot(x_axis, trace_min, label='历史最优解')
    # plt.plot(x_axis, trace_Y, label='候选解')
    plt.title("算法曲线收敛图")
    plt.xlabel("迭代次数")
    plt.ylabel("最大完工时间")
    plt.legend()
    plt.show()
if __name__ == '__main__':
    main()