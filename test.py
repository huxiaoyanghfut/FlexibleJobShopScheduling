# 1.解析数据得到JobMachine、ProcesscingTime、MachineNumber、OperationNumber
from types import ClassMethodDescriptorType
import pandas as pd
import numpy as np
import math
from cal_objective import cal_objective
from initialization import initialization
from main import main
from neighboring_cur import neighboring_cur
from parse_data import parse_data
from parse_data_new1 import parse_data_new1

# job_machine_tmp = pd.read_excel("排产输入数据样例.xlsx",sheet_name="工序可选机器表")
# processing_time_tmp = pd.read_excel("排产输入数据样例.xlsx",sheet_name="各工序加工时间")
# print(job_machine_tmp)
# print(processing_time_tmp)
# print(job_machine_tmp.loc[0,'工序4'])
# print(type(job_machine_tmp.loc[0,'工序4']))
# str1 = job_machine_tmp.loc[0,'工序4']
# print(str1.split(','))
# print(int(str1.split(',')[0]))
# print(job_machine_tmp.iloc[0]) #第一行数据，数据类型为series
# print(job_machine_tmp.iloc[[0, 1, 3]])  #截取子表，数据类型为dataFrame
# print(job_machine_tmp.iloc[:5])  #截取子表，数据类型为dataFrame
# print(job_machine_tmp.iloc[0:9, 1:7])
# str_tmp = "2,4"

# print(list(map(int, str_tmp.split(','))))

# 数据解析测试 OK
# job_machine, processing_time, machine_number, operation_number = parse_data()
# job_machine, processing_time, machine_number, operation_number = parse_data_new1()

# print('工序机器表：')
# print(job_machine)

# print('工序时间表：')
# print(processing_time)

# print('机器数量：')
# print(machine_number)

# print('各工件工序数量：')
# print(operation_number)

# 测试初始化结果 OK
# job_machine, processing_time, machine_number, operation_number = parse_data()
# job_machine, processing_time, machine_number, operation_number = parse_data_new1()
# cur = initialization(operation_number, job_machine)
# print(sum(operation_number))
# print(len(cur))
# print(cur)

# 测试计算目标函数值的计算调度工序部分 OK
# print("测试求目标函数")
# job_machine, processing_time, machine_number, operation_number = parse_data()
# job_machine, processing_time, machine_number, operation_number = parse_data_new1()
# cur = initialization(operation_number, job_machine)
# objective_value = cal_objective(cur, machine_number, operation_number, job_machine, processing_time)
# print(objective_value)

# 测试计算目标函数值的计算工序时间（每个工序的开工时间和完工时间）和最大完工时间 OK
# print("测试求目标函数")
# job_machine, processing_time, machine_number, operation_number = parse_data()
# cur = initialization(operation_number, job_machine)
# objective_value = cal_objective(cur, machine_number, operation_number, job_machine, processing_time)
# print(objective_value)

# 测试生成cur的邻域解 OK
# print("测试生成cur的邻域解")
# job_machine, processing_time, machine_number, operation_number = parse_data()
# job_machine, processing_time, machine_number, operation_number = parse_data_new1()
# cur = initialization(operation_number, job_machine)
# print("我是分割线=======================")
# print(cur)
# print("我是分割线=======================")
# next, index1, index2, index3 = neighboring_cur(cur, job_machine, operation_number)
# print(next)
# print("我是分割线=======================")
# total_operations = math.floor(len(cur)/2)
# print([cur[total_operations:len(cur)][index1],next[total_operations:len(next)][index1]])
# print([cur[index2],next[index2]])
# print([cur[index3],next[index3]])

# 测试主函数main OK
# main()