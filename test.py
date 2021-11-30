#1.解析数据得到JobMachine、ProcesscingTime、MachineNumber、OperationNumber
from types import ClassMethodDescriptorType
import pandas as pd
import numpy as np

from parse_data import parse_data
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
job_machine, processing_time, machine_number, operation_number = parse_data()
print('\n')
print(job_machine)
print('\n')
print(processing_time)
print('\n')
print(machine_number)
print('\n')
print(operation_number)
print('\n')