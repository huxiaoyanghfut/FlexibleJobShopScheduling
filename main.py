import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import copy
from initialization import initialization
from cal_objective import cal_objective
from neighboringX import neighboringX
from parse_data import parse_data
def main():
    job_machine, processing_time, machine_number, operation_number = parse_data()
    # 设置参数
    H = 50
    MAX_ITERATION = 1000000
    MAX_NO_IMPROVE = 0.03
    # 初始化当前解X，并计算其目标函数值makespan f(x)
    X = initialization(operation_number, job_machine)
    bestX = X
    objective_value_X = cal_objective(X, machine_number, operation_number, job_machine, processing_time)
    best_Cmax_time = objective_value_X
    history_list = [objective_value_X for i in range(H)]
    it = 0
    idle = 0
    trace_min = []
    trace_Y = []
    #循环过程
    while (it < MAX_ITERATION) and (idle < MAX_NO_IMPROVE*MAX_ITERATION):
        Y = neighboringX(X, job_machine, operation_number)
        #TODO 多邻域选择
        objective_value_Y = cal_objective(Y, machine_number, operation_number, job_machine, processing_time)
        if objective_value_Y >= objective_value_X:
            idle += 1
        else:
            idle = 0
        if objective_value_Y < best_Cmax_time:
            bestX = Y
            best_Cmax_time = objective_value_Y
            print('最优解的完工时间是：%d\n', best_Cmax_time)
        h = it % H
        if objective_value_Y < history_list[h] or objective_value_Y <= objective_value_X:
            X = Y
            objective_value_X = objective_value_Y
        if objective_value_Y < history_list[h]:
            history_list[h] = objective_value_Y
        it += 1
        trace_min.append(min(history_list))
        trace_Y.append(objective_value_Y)
        print("最优解的完工时间：%f\n", best_Cmax_time)
        print("最优解是：\n")
        print(bestX)

        mpl.rcParams['font.sans-serif'] = ['SimHei']
        mpl.rcParams['axes.unicode_minus'] = False
        plt.plot(trace_min)
        plt.plot(trace_Y)
        plt.title("算法曲线收敛图")
        plt.xlabel("迭代次数")
        plt.ylabel("最大完工时间")
if __name__ == '_main_':
    main()
